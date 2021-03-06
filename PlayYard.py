import helper #switch-case 
import math   #sin/cos, abs
import PointMod #point (position) and point modification
import G_Com
import copy

S = list()
duration = 0
CMDs = list()

def Strings(point1, angleZX, angleZY):
    pointShift = PointMod.pointShift(-20, 0, 0)
    point2 = PointMod.Modification(copy.deepcopy(point1), pointShift, angleZX, angleZY)
    point3 = PointMod.Modification(copy.deepcopy(point2), pointShift, angleZX, angleZY)
    point4 = PointMod.Modification(copy.deepcopy(point3), pointShift, angleZX, angleZY)
    return [point1, point2, point3, point4]

class Pick: #current position
    def __init__(self, X, Y, Z, String, mode):
        self.CurrentPoint = PointMod.point(X, Y, Z, 0, 0, 0)
        self.String = String
        self.mode = mode
    def __edit__(self, X, Y, Z, String, mode):
        self.CurrentPoint = PointMod.point.__edit__(X, Y, Z)
        self.String = String
        self.mode = mode

def Crossing(Strings, PositionLast, PositionNext):
    for i in Strings:
        k = (i.Y - PositionLast.Y)/(i.X - PositionLast.X)
        b = i.Y - k*i.X
        if b-k*PositionNext.X - PositionNext.Y > 0:
            return 1
    return 0
def Load(angleZX, angleZY, mode, point):
     global S
     FirstString = copy.deepcopy(point) # set first point here(highest string)
     S = Strings(FirstString, angleZX, angleZY)
     pick = Pick(point.X, point.Y, point.Z, 1, mode)

def Play(stringNum, angleZX, angleZY, mode, point, crossing):
    G_CMD = ''
    Load(angleZX, angleZY, mode, point)
    G_CMD = G_CMD + G_Com.G_Maker(mode, angleZX, angleZY, S[int(stringNum)-1], 20000, crossing) #the angle changes clockwise
    return G_CMD
    

def TabsProc(tabs, angleZX, angleZY,  mode, point):
    Load(angleZX, angleZY,  mode, point)
    G_CMD  = ''
    crossing = 1
    for x in range(0, len(tabs)):
            #jit = jit+ str(tabs[x]) +'\n'
            G_CMD  = G_CMD  + G_Com.G_Maker(mode,  angleZX, angleZY, S[tabs[x]-1], 20000, crossing) #the angle changes clockwise
            if x < (len(tabs)-1):
                while math.fabs(tabs[x+1] - tabs[x])>1:
                    tabs[x] = int(math.copysign(1,(tabs[x+1] - tabs[x]))*1+tabs[x])
                    crossing = 2
                    G_CMD  = G_CMD  + G_Com.G_Maker(mode, angleZX, angleZY, S[tabs[x]-1], 20000, crossing) #the angle changes clockwise
                    crossing = 0
            if x == 0: crossing = 0
    return G_CMD




class CMD_TAB:
    def __init__(self, note, string):
          self.note = note
          self.string = string
          self.duration = 0
          self.crossing = 1
    def __edit__(self, duration):
          self.duration = duration
    def __crossing__(self, crossing):
          self.crossing = crossing
          
    
    
def CheckForNote(strings):
    modeCh = 1 #start
    global duration
    global CMDs
    for l in range(0, len(strings[0])):
        for x in range(0, len(strings[0][l])):
            for case in helper.switch(modeCh):
                
                if case(2):
                    
                    
                    for y in range(0, 4): #calculating duration
                        temp = strings[y][l]
                        if temp[x].isdigit() == True or (x == len(strings[y][l])-1 and l == len(strings[0])-1) and CMDs[len(CMDs)-1].duration == 0:
                            
                            if y > (CMDs[len(CMDs)-1].string -1):
                                duration = duration - (y - (4 - CMDs[len(CMDs)-1].string))*25
                            duration = int(duration/100)
                            for case in helper.switch(duration):
                                if case(6):
                                    CMDs[len(CMDs)-1].__edit__(4000) #semibreve
                                    break
                                if case(5):
                                    CMDs[len(CMDs)-1].__edit__(2000) #minim
                                    break
                                if case(4):
                                    CMDs[len(CMDs)-1].__edit__(1000) #crotchet
                                    break
                                if case(3):
                                    CMDs[len(CMDs)-1].__edit__(500)  #quaver
                                    break
                                if case(2):
                                    CMDs[len(CMDs)-1].__edit__(250)  #semiquaver
                                    break
                                if case():
                                    CMDs[len(CMDs)-1].__edit__(4000)
                                    break 
                            duration = 0
                            modeCh = 1                
                            
                        else:
                             duration = duration + 25
                             

                            
                                        
                if case(1):                         #found the note
                    for y in range(0, 4):
                        temp = strings[y][l]
                        if temp[x].isdigit() == True:
                           CMDs.append(CMD_TAB(int(temp[x]), 4 - y))
                           modeCh = 2
                           #if len(CMDs)>1 and CMDs[len(CMDs)-2].string - CMDs[len(CMDs)-1].string == 1:
                            #   CMDs[len(CMDs)-2].crossing == 0
                           break
                    break
                if case():
                    pass                                                  #expecting default or exeption
                    break
            
def PlayTabs(strings, angleZX, angleZY, mode, point):
    global CMDs
    CMDs = list()
    G_CMD ='G101 J0=90 J1=-31 J2=106 J3=0 J4=-51 J5=0 F20000\nG01 A= -82 B= 0 C= 90 F20000\nLOOP\n'
    pick_time = 200 #vel 20 000,  two sound points
    CheckForNote(strings)
    picks = list()
    for item in CMDs:
        picks.append(item.string)
        
    for item in range(0, len(CMDs)):
        G_CMD = G_CMD  +(str('M'+str(CMDs[item].string*100 + CMDs[item].note) + '\n'))
        G_CMD = G_CMD + (Play(CMDs[item].string, angleZX, angleZY, mode, point, CMDs[item].crossing))
        G_CMD = G_CMD  + (str('G04 ' + str((CMDs[item].duration - pick_time)/1000)+ ' \n'))
    G_CMD = G_CMD + 'ENDLOOP'

    return G_CMD


