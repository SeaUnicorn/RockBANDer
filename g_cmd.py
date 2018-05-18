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
                    ' F' + str(velocity)+ ' \n' )

def g_maker(mode, numberN, angleZX, angleZY, point, velocity, crossing, string, note): #crossing is a integer, using to make lazy string crossing (without too many actions)
    pointShift = point_Mod.pointShift(0,0,10)                                              #just creating an obj
    point = point_Mod.modification(point, pointShift, angleZX, angleZY)
    G_CMD = '' #resulting string
    for case in helper.switch(mode):
        
        if case('D'):   
            if crossing == 1 or crossing == 2 :
                G_CMD = G_CMD + printer(point, velocity, numberN) #string coord + z +10 mm
            if crossing != 2:
                pointShift.__edit__(5, 0, -10)                                    #a pick goes down/ shift (dependes on the strings' positions)
                G_CMD = G_CMD + printer(point_Mod.modification(point, pointShift, angleZX, angleZY), velocity, numberN)#creating new JITstring[] about new pick_position
                #
                if note != 0 :  G_CMD = G_CMD + ('N'+ str(numberN) + ' ') +(str('M'+str(string*100 + note) + ' \n')) 
                #
                pointShift.__edit__(0, 0, -5)
                G_CMD = G_CMD + printer(point_Mod.modification(point, pointShift, angleZX, angleZY), velocity, numberN)
                pointShift.__edit__(-10, 0, 10)
                G_CMD = G_CMD + printer(point_Mod.modification(point, pointShift, angleZX, angleZY), velocity, numberN)
            break;
    
        if case('U'):
            if crossing == 1 or crossing == 2 :
                G_CMD = G_CMD + printer(point, velocity, numberN) #string coord + z +10 mm
            if crossing != 2:
                pointShift.__edit__(-5, 0, -10)                                   #a pick goes up/ shift (dependes on the strings' positions)
                G_CMD = G_CMD + printer(point_Mod.modification(point, pointShift, angleZX, angleZY), velocity, numberN)
                #
                if note!=0: G_CMD = G_CMD + ('N'+ str(numberN) + ' ') +(str('M'+str(string*100 + note) + ' \n'))
                #
                pointShift.__edit__(0, 0, -5)
                G_CMD = G_CMD + printer(point_Mod.modification(point, pointShift, angleZX, angleZY), velocity, numberN)
                pointShift.__edit__(10, 0, 10)
                G_CMD = G_CMD + printer(point_Mod.modification(point, pointShift, angleZX, angleZY), velocity, numberN)
            break;
    
        if case('DU'):
            if crossing == 1 or crossing == 2 :
                G_CMD = G_CMD + printer(point, velocity, numberN) #string coord + z +10 mm
            if crossing != 2:
                pointShift.__edit__(5, 0, -10)                                    #a pick goes downup/ shift (dependes on the strings' positions)
                G_CMD = G_CMD + printer(point_Mod.modification(point, pointShift, angleZX, angleZY), velocity, numberN)#creating new JITstring[] about new pick_position
                pointShift.__edit__(0, 0, -7.5)                                   #a pick goes down then goes up
                G_CMD = G_CMD + printer(point_Mod.modification(point, pointShift, angleZX, angleZY), velocity, numberN)
                #
                if note!=0: G_CMD = G_CMD + ('N'+ str(numberN) + ' ') +(str('M'+str(string*100 + note) + ' \n'))
                #

                pointShift.__edit__(-10, 0, 0)
                G_CMD = G_CMD + printer(point_Mod.modification(point, pointShift, angleZX, angleZY), velocity, numberN)
                pointShift.__edit__(10, 0, 13.5)
                G_CMD = G_CMD + printer(point_Mod.modification(point, pointShift, angleZX, angleZY), velocity, numberN)
            break;
           
    return G_CMD                                                                           #for tests. Expects 'return 0'




