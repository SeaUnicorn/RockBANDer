import helper #switch-case 
import math   #sin/cos
import PointMod #point (position) and point modification

def printer(point, vel, numberN):                                                       #a G_string[] former
    numberN = numberN + 10
    return ('N'+ str(numberN) + ' G01' + ' X=' + str(round(point.X, 3)) +
                    ' Y=' + str(round(point.Y, 3)) + ' Z=' + str(round(point.Z, 3)) +
                    #' A=' + str(point.A) + ' B=' + str(point.B) +
                    #' C=' + str(point.C) +
                    ' F' + str(vel)+ ' \n' )

def G_Maker(mode, numberN, angleZX, angleZY, point, vel, crossing, string, note): #crossing is a integer, using to make lazy string crossing (without too many actions)
    pointShift = PointMod.pointShift(0,0,10)                                              #just creating an obj
    point = PointMod.Modification(point, pointShift, angleZX, angleZY)
    G_CMD = '' #resulting string
    for case in helper.switch(mode):
        
        if case('D'):
            if crossing == 1 or crossing == 2 :
                G_CMD = G_CMD + printer(point, vel, numberN) #string coord + z +10 mm
            if crossing != 2:
                pointShift.__edit__(5, 0, -10)                                    #a pick goes down/ shift (dependes on the strings' positions)
                G_CMD = G_CMD + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)#creating new JITstring[] about new pick_position
                #
                G_CMD = G_CMD + ('N'+ str(numberN) + ' ') +(str('M'+str(string*100 + note) + ' \n'))
                #
                pointShift.__edit__(0, 0, -5)
                G_CMD = G_CMD + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
                pointShift.__edit__(-10, 0, 10)
                G_CMD = G_CMD + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
            break;
    
        if case('U'):
            if crossing == 1 or crossing == 2 :
                G_CMD = G_CMD + printer(point, vel, numberN) #string coord + z +10 mm
            if crossing != 2:
                pointShift.__edit__(-5, 0, -10)                                   #a pick goes up/ shift (dependes on the strings' positions)
                G_CMD = G_CMD + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
                #
                G_CMD = G_CMD + ('N'+ str(numberN) + ' ') +(str('M'+str(string*100 + note) + ' \n'))
                #
                pointShift.__edit__(0, 0, -5)
                G_CMD = G_CMD + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
                pointShift.__edit__(10, 0, 10)
                G_CMD = G_CMD + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
            break;
    
        if case('DU'):
            if crossing == 1 or crossing == 2 :
                G_CMD = G_CMD + printer(point, vel, numberN) #string coord + z +10 mm
            if crossing != 2:
                pointShift.__edit__(5, 0, -10)                                    #a pick goes downup/ shift (dependes on the strings' positions)
                G_CMD = G_CMD + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)#creating new JITstring[] about new pick_position
                pointShift.__edit__(0, 0, -7.5)                                   #a pick goes down then goes up
                G_CMD = G_CMD + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
                #
                G_CMD = G_CMD + ('N'+ str(numberN) + ' ') +(str('M'+str(string*100 + note) + ' \n'))
                #

                pointShift.__edit__(-10, 0, 0)
                G_CMD = G_CMD + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
                pointShift.__edit__(10, 0, 13.5)
                G_CMD = G_CMD + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
            break;
        if case():
            print('Exeption')                                                    #expecting default or exeption
            break

    
    return G_CMD +'\n'                                                                           #for tests. Expects 'return 0'




