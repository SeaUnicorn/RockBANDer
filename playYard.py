import helper #switch-case 
import point_Mod #point (position) and point modification
import g_cmd
import copy

S = list()
duration = 0
CMDs = list()
#point[5][2][2]
Velocity = 5000


class CMD_TAB:
    def __init__(self, note, string):
          self.note = note
          self.string = string
          self.duration = 0
    def __edit__(self, duration):
          self.duration = duration
    def edit_note (self, note, string):
          self.note = note
          self.string = string

          

def Strings(point1, angleZX, angleZY):
    pointShift = point_Mod.pointShift(-20, 0, 0)
    point2 = point_Mod.modification(copy.deepcopy(point1), pointShift, angleZX, angleZY)
    point3 = point_Mod.modification(copy.deepcopy(point2), pointShift, angleZX, angleZY)
    point4 = point_Mod.modification(copy.deepcopy(point3), pointShift, angleZX, angleZY)
    return [point1, point2, point3, point4]

#def points(p):
 #   global point
    #for item in range(0, 5):
        
        
        
    

class Pick: #current position
    def __init__(self, X, Y, Z, String, mode):
        self.CurrentPoint = point_Mod.point(X, Y, Z, 0, 0, 0)
        self.String = String
        self.mode = mode
    def __edit__(self, X, Y, Z, String, mode):
        self.CurrentPoint = point_Mod.point.__edit__(X, Y, Z)
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
     #pick = Pick(point.X, point.Y, point.Z, 1, mode)

def play(stringNum, angleZX, angleZY, NumberN, mode, point, crossing, string, note):
    G_CMD = ''
    Load(angleZX, angleZY, NumberN, mode, point)
    G_CMD = G_CMD + g_cmd.g_maker(mode, NumberN, angleZX, angleZY, S[int(stringNum)-1], Velocity, crossing, string, note) #the angle changes clockwise  Velocity
    return G_CMD

def playStart(stringNum, angleZX, angleZY, NumberN, mode, point, crossing, string, note):
    Load(angleZX, angleZY, NumberN, mode, point)
    return str(g_cmd.startPoint(mode, NumberN, angleZX, angleZY, S[int(stringNum)-1], Velocity, crossing, string, note)) #the angle changes clockwise  Velocity

def jump(string, stringL, mode,  angleZX, angleZY, NumberN, point):
    G_CMD = ''
    Load(angleZX, angleZY, NumberN, mode, point)
    G_CMD = G_CMD + g_cmd.crossing(mode, NumberN, angleZX, angleZY, S[int(string)-1], S[int(stringL)-1], Velocity) #the angle changes clockwise  Velocity
    return G_CMD
   
    
def g_form_cmd(tabs):
    
    
    global CMDs
    
    for tact in range(0, len(tabs[0])):
        x = 0 
        duration = 0
        
        CMDs.append(CMD_TAB(999, 0)) #empty note 
        measure = len(tabs[0][tact]) #tact duration
        phase = 2
        
        while x < len(tabs[0][tact])-1:
            for case in helper.switch(phase):
                if case(2):           #calculating duration phase
                    measure = len(tabs[0][tact]) #tact duration
                    i = 0
                    while (x + i) < measure and phase == 2:
                        for y in range(0, 4): 
                            temp = tabs[y][tact]
                            
                            if temp[(x + i)] != '-' or (x + i) == measure-1:
                                duration = i
                                x = x + i
                                if i > 0: 
                                    CMDs[len(CMDs)-1].__edit__(float((duration+1)/measure)) 
                                else:
                                    del CMDs[len(CMDs)-1] 
                                
                                i = 0
                                phase = 1
                                break
                        i += 1
                    duration = 0      
                    phase = 1
                if case(1):                         #find the note
                    for y in range(0, 4):
                        temp = tabs[y][tact]
                        tonality = ' '    #number of "lad"
                        if temp[x].isdigit() == True:
                            tonality = temp[x] 
                            if temp[x+1].isdigit() == True: 
                                tonality += temp[x+1]
                                x +=1
                            CMDs.append(CMD_TAB(int(tonality), 4 - y))
                            phase = 2
                            break
                        if temp[x] == 'P' or temp[x] == 'p':
                            tonality = '999'
                            CMDs.append(CMD_TAB(int(tonality), 4 - y))
                            phase = 2
                            break
                        #if x == len(tabs[0][tact])- 1 and y == 3:
                         #   CMDs.append(CMD_TAB(50, 0))
                          #  CMDs[len(CMDs)-1].__edit__(1)
                    x += 1   
                    break
                if case():
                    pass                                                  #expecting default or exeption
                    break
            
    
def g_check_note(tabs):
    phase = 1 #start
    duration = 0
    global CMDs
    
    
    for tact in range(0, len(tabs[0])):
        x = 0
        
        while x < len(tabs[0][tact])-1:
            for case in helper.switch(phase):
                
                if case(2):
                    measure = len(tabs[0][tact]) #tact duration
                    i = 0
                    while (x + i) < measure and phase == 2:
                        for y in range(0, 4): #calculating duration
                            temp = tabs[y][tact]
                            
                            if temp[(x + i)] != '-' or (x + i) == measure-1:
                                duration = i
                                x = x + i
                                i = 0
                                CMDs[len(CMDs)-1].__edit__(float((duration+1)/measure)) 
                                phase = 1
                                break
                        i += 1
                    duration = 0      
                    phase = 1
                   
                if case(1):                         #find the note
                    for y in range(0, 4):
                        temp = tabs[y][tact]
                        tonality = ' '
                        if temp[x].isdigit() == True:
                            tonality = temp[x] 
                            if temp[x+1].isdigit() == True: 
                                tonality += temp[x+1]
                                x +=1
                            CMDs.append(CMD_TAB(int(tonality), 4 - y))
                            phase = 2
                            break
                        #if x == len(tabs[0][tact])- 1 and y == 3:
                         #   CMDs.append(CMD_TAB(50, 0))
                          #  CMDs[len(CMDs)-1].__edit__(1)
                    x += 1   
                    break
                if case():
                    pass                                                  #expecting default or exeption
                    break
            
            
def play_TABs(g_Inf):
    global CMDs
    CMDs = list()
    mode = 'D'
    G_CMD ='N10 M499 \nN10 G101 J0=90 J1=-47 J2=88 J4=-73 F5000 \nM500 \nG18 \ndef UDINT duration \nduration = ' + str(g_Inf.duration*1000) +' \n Loop \n'
    #g_check_note(g_Inf.tabs)
    g_form_cmd(g_Inf.tabs)
    #CMD
    
    for item in range(0, len(CMDs)):
        if item  > 0 and CMDs[item].string > CMDs[item-1].string:
            mode = 'D'
        elif item  > 0 and CMDs[item].string == CMDs[item-1].string:
            if mode == 'U' : mode = 'D'
            else: mode = 'U'
        else:
            mode = 'U'
        
        if g_Inf.mode  == 'P' or CMDs[item].note == 999: mode = 'P'
        if item == 0:
            if CMDs[item].string > CMDs[item + 1].string:
                mode == 'D'
            print(mode)
            G_CMD = G_CMD + (playStart(CMDs[item].string, g_Inf.angle_ZX, g_Inf.angle_ZY, g_Inf.JIT_N, mode, g_Inf.first_point, 1, CMDs[item].string, CMDs[item].note))
        else:
            print(mode)
            G_CMD = G_CMD + (jump(CMDs[item].string, CMDs[item-1].string, mode,  g_Inf.angle_ZX, g_Inf.angle_ZY, g_Inf.JIT_N, g_Inf.first_point))  
           
        
        
        G_CMD = G_CMD + (play(CMDs[item].string, g_Inf.angle_ZX, g_Inf.angle_ZY, g_Inf.JIT_N, mode, g_Inf.first_point, 1, CMDs[item].string, CMDs[item].note))
        G_CMD = G_CMD + ('N'+ str(g_Inf.JIT_N) + ' ') + (str('M' + str(500 + int(CMDs[item].duration*64))+ '\n \n'))
    G_CMD = G_CMD + 'N10 M100 \nN10 M200 \nN10 M300 \nN10 M400 \n'
    G_CMD = G_CMD + 'N10 G101 J0=90 J1=-47 J2=88 J4=-73 \n'
    G_CMD = G_CMD + 'ENDLOOP \n'

    return G_CMD


