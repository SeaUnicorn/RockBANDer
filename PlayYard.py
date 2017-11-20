import helper #switch-case 
import math   #sin/cos, abs
import PointMod #point (position) and point modification
import JitCom
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
def Load(angleZX, angleZY, NumberN, mode, point):
     global S
     FirstString = copy.deepcopy(point) # set first point here(highest string)
     S = Strings(FirstString, angleZX, angleZY)
     pick = Pick(point.X, point.Y, point.Z, 1, mode)

def Play(stringNum, angleZX, angleZY, NumberN, mode, point, crossing):
    jit = ''
    Load(angleZX, angleZY, NumberN, mode, point)
    jit = jit + JitCom.JITMaker(mode, NumberN, angleZX, angleZY, S[int(stringNum)-1], 10000, crossing) #the angle changes clockwise
    return jit
    

def TabsProc(tabs, angleZX, angleZY, NumberN, mode, point):
    Load(angleZX, angleZY, NumberN, mode, point)
    jit = ''
    crossing = 1
    for x in range(0, len(tabs)):
            #jit = jit+ str(tabs[x]) +'\n'
            jit = jit + JitCom.JITMaker(mode, NumberN, angleZX, angleZY, S[tabs[x]-1], 10000, crossing) #the angle changes clockwise
            if x < (len(tabs)-1):
                while math.fabs(tabs[x+1] - tabs[x])>1:
                    tabs[x] = int(math.copysign(1,(tabs[x+1] - tabs[x]))*1+tabs[x])
                    crossing = 2
                    jit = jit + JitCom.JITMaker(mode, NumberN, angleZX, angleZY, S[tabs[x]-1], 10000, crossing) #the angle changes clockwise
                    crossing = 0
            if x == 0: crossing = 0
    return jit




class CMD_TAB:
    def __init__(self, note, string):
          self.note = note
          self.string = string
          self.duration = 0
    def __edit__(self, duration):
          self.duration = duration
          
    
    
def CheckForNote(strings):
    modeCh = 1 #start
    global duration
    global CMDs
    for l in range(0, len(strings[0])):
        for x in range(0, len(strings[0][l])):
            for case in helper.switch(modeCh):
                
                if case(2):
                    
                    
                    for y in range(0, 4):
                        temp = strings[y][l]
                        if temp[x].isdigit() == True or (x == len(strings[y][l])-1 and l == len(strings[0])-1) and CMDs[len(CMDs)-1].duration == 0:
                            
                            if y > (CMDs[len(CMDs)-1].string -1):
                                duration = duration - (y - (4 - CMDs[len(CMDs)-1].string))*25
                            duration = int(duration/100)
                            for case in helper.switch(duration):
                                if case(6):
                                    CMDs[len(CMDs)-1].__edit__(4000)
                                    break
                                if case(5):
                                    CMDs[len(CMDs)-1].__edit__(2000)
                                    break
                                if case(4):
                                    CMDs[len(CMDs)-1].__edit__(1000)
                                    break
                                if case(3):
                                    CMDs[len(CMDs)-1].__edit__(500)
                                    break
                                if case(2):
                                    CMDs[len(CMDs)-1].__edit__(250)
                                    break
                                if case():
                                    CMDs[len(CMDs)-1].__edit__(4000)
                                    break 
                            duration = 0
                            modeCh = 1                
                            
                        else:
                             duration = duration + 25
                             

                            
                                        
                if case(1):
                    for y in range(0, 4):
                        temp = strings[y][l]
                        if temp[x].isdigit() == True:
                           CMDs.append(CMD_TAB(int(temp[x]), 4 - y))
                           modeCh = 2
                           
                           break
                    break
                if case():
                    pass                                                  #expecting default or exeption
                    break
            
def PlayTabs(strings, angleZX, angleZY, NumberN, mode, point):
    global CMDs
    CMDs = list()
    jit =''
    CheckForNote(strings)
    picks = list()
    for item in CMDs:
        picks.append(item.string)
        
    for item in range(0, len(CMDs)):
        jit = jit + (str('M'+str(CMDs[item].string*100 + CMDs[item].note) + ' \n'))
        jit = jit + (Play(CMDs[item].string, angleZX, angleZY, NumberN, mode, point, 1))
        jit = jit + (str('MW1 = X M' + str(CMDs[item].duration)+ ' \n'))

    return jit


