import helper #switch-case 
import point_Mod #point (position) and point modification


class guitar_Info: #geom.point
      def __init__(self, tabs, angle_ZX, angle_ZY, JIT_N, mode, first_point, duration):
          self.tabs = tabs
          self.angle_ZX = angle_ZX
          self.angle_ZY = angle_ZY
          self.JIT_N = JIT_N 
          self.mode = mode #
          self.first_point = first_point #
          self.duration = duration #(tackt)
          

def printer(point, velocity, numberN):                                                       #a G_string[] former
    numberN = numberN + 10
    return ('N'+ str(numberN) + ' G01' + ' X=' + str(round(point.X, 3)) +
                    ' Y=' + str(round(point.Y, 3)) + ' Z=' + str(round(point.Z, 3)) +
                    #' A=' + str(point.A) + ' B=' + str(point.B) +
                    #' C=' + str(point.C) +
                     ' \n' )
def printerSpl (point):
    return ('G1 Z' + str(round(point.Z, 3)) + ' X' + str(round(point.X, 3)) + ' \n')

def printerCircus(direction, point, angle, numberN):
    numberN = numberN + 10
    return ('N'+ str(numberN) + ' ' + str(direction)+ ' G161' + ' I'+ str(round(point.X, 3)) + ' K' + str(round(point.Z, 3)) + ' H' +str(angle)+ ' \n')

def printerRadius(point, radius):
    return ('G161 ' +'X'+str(round(point.X, 3)) + ' Z'+ str(round(point.Z, 3))+ ' R=' + str(radius) + ' \n')  

def crossing(mode, NumberN, angleZX, angleZY, string, stringL, Velocity):
    G_CMD = '' #resulting string
    pointShift = point_Mod.pointShift(0,0,0)
    point_Mod.modification(string, pointShift, angleZX, angleZY)
    if string!= stringL:
      print('string X = ' + str(string.X) + ' Z = ' + str(string.Z))
      for case in helper.switch(mode):
        if case('D'):
            pointShift.__edit__(10, 0, 0)
            point_Mod.modification(string, pointShift, angleZX, angleZY)
            R = round((helper.distance(string, stringL))*(25/30), 3)
            G_CMD = G_CMD + 'G02 ' + printerRadius(string, R) 
            
            print('start D X = ' + str(string.X) + ' Z = ' + str(string.Z))
            print('before X = ' + str(stringL.X) + ' Z = ' + str(stringL.Z))
            break
        if case('U'):
            pointShift.__edit__(-10, 0, 0)
            point_Mod.modification(string, pointShift, angleZX, angleZY)
            R = round((helper.distance(string, stringL))*(25/30), 3)
            G_CMD = G_CMD + 'G03 ' + printerRadius(string, R)
            print('start U X = ' + str(string.X) + ' Z = ' + str(string.Z))
            print('before X = ' + str(stringL.X) + ' Z = ' + str(stringL.Z))
            break
        
    
    return G_CMD

def jump(point_last, mode_last, point, mode, angleZX, angleZY, jump_mode):
    G_CMD = '' #resulting string
    pointShift = point_Mod.pointShift(0,0,0)                                              #just creating an obj
    point = point_Mod.modification(point, pointShift, angleZX, angleZY)

    point_last = point_Mod.modification(point_last, pointShift, angleZX, angleZY)
    
    for case in helper.switch(mode_last):
        if case('D'):
            pointShift.__edit__(-10, 0, 0)
            point_last = point_Mod.modification(point_last, pointShift, angleZX, angleZY)
        if case('U'):
            pointShift.__edit__(10, 0, 0)
            point_last = point_Mod.modification(point_last, pointShift, angleZX, angleZY)
            
    for case in helper.switch(mode):
        
        if case('D'):
            pointShift.__edit__(-10, 0, 0)
            point = point_Mod.modification(point, pointShift, angleZX, angleZY)
        if case('U'):
            pointShift.__edit__(10, 0, 0)
            point = point_Mod.modification(point, pointShift, angleZX, angleZY)
    if helper.distance(point, point_last) > 10:
        R = round(helper.distance(point, point_last)*(25/30), 3)
        if R < 11: R = 11
        if jump_mode == 1:
           G_CMD = G_CMD + 'G02 ' + printerRadius(point, R)  
        else:
           G_CMD = G_CMD + 'G03 ' + printerRadius(point, R) 
    
    
    return G_CMD
    

def startPoint(numberN, angleZX, angleZY, point, velocity):
    G_CMD = '' #resulting string
    pointShift = point_Mod.pointShift(0,0,0)    #just creating an obj
    point = point_Mod.modification(point, pointShift, angleZX, angleZY)
    G_CMD = G_CMD + printer(point_Mod.modification(point, pointShift, angleZX, angleZY), velocity, numberN) 
    pointShift.__edit__(10, 0, 0)
    G_CMD = G_CMD + printer(point_Mod.modification(point, pointShift, angleZX, angleZY), velocity, numberN) 
    return G_CMD                
    
     
        

def g_maker(mode, numberN, angleZX, angleZY, point, velocity, crossing, string, note): #crossing is a integer, using to make lazy string crossing (without too many actions)
    
    pointShift = point_Mod.pointShift(0,0,0)                                              #just creating an obj
    point = point_Mod.modification(point, pointShift, angleZX, angleZY)
    G_CMD = '' #resulting string
    

    for case in helper.switch(mode):
        
        if case('D'):
            #pointShift.__edit__(10, 0, 0)
            #G_CMD = G_CMD + printer(point_Mod.modification(point, pointShift, angleZX, angleZY), velocity, numberN) 
            pointShift.__edit__(-10, 0, 0)
            point = point_Mod.modification(point, pointShift, angleZX, angleZY)
            if note != 0 :  G_CMD = G_CMD + ('N'+ str(numberN) + ' ') +(str('M'+str(string*100 + note) + ' \n')) 
            G_CMD = G_CMD + 'G03 ' + printerRadius(point, 50)
            break
    
        if case('U'):
            #pointShift.__edit__(-10, 0, 0)
            #G_CMD = G_CMD + printer(point_Mod.modification(point, pointShift, angleZX, angleZY), velocity, numberN) #string coord + z +10 mm
            pointShift.__edit__(10, 0, 0)
            point = point_Mod.modification(point, pointShift, angleZX, angleZY)
            if note != 0 :  G_CMD = G_CMD + ('N'+ str(numberN) + ' ') +(str('M'+str(string*100 + note) + ' \n')) 
            G_CMD = G_CMD + 'G02 ' + printerRadius(point, 50)
            break
    
        
        if  case('P'):
            if note!=0: G_CMD = G_CMD + ('N'+ str(numberN) + ' ') +(str('M'+str(string*100 + note) + ' \n'))
        
           
    return G_CMD                                                                           #for tests. Expects 'return 0'




