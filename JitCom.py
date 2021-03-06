import helper #switch-case 
import math   #sin/cos
import PointMod #point (position) and point modification

def printer(point, vel, numberN):                                                       #a JITstring[] former
    numberN = numberN + 10
    return ('N'+ str(numberN) + ' G01' + ' X=' + str(point.X) +
                    ' Y=' + str(point.Y) + ' Z=' + str(point.Z) +
                    ' A=' + str(point.A) + ' B=' + str(point.B) +
                    ' C=' + str(point.C) +' F' + str(vel)+ ' \n' )

def JITMaker(mode, numberN, angleZX, angleZY, point, vel, crossing): #crossing is a integer, using to make lazy string crossing (without too many actions)
    pointShift = PointMod.pointShift(0,0,10)                                              #just creating an obj
    #if crossing  == 0 :
    point = PointMod.Modification(point, pointShift, angleZX, angleZY)
    jit = ''
    for case in helper.switch(mode):
        
        if case('D'):
            if crossing == 1 or crossing == 2 :
                jit = jit + printer(point, vel, numberN) #string coord + z +10 mm
            if crossing != 2:
                pointShift.__edit__(5, 0, -10)                                    #a pick goes down/ shift (dependes on the strings' positions)
                jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)#creating new JITstring[] about new pick_position
                pointShift.__edit__(0, 0, -5)
                jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
                pointShift.__edit__(-10, 0, 10)
                jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
            break;
    
        if case('U'):
            if crossing == 1 or crossing == 2 :
                jit = jit + printer(point, vel, numberN) #string coord + z +10 mm
            if crossing != 2:
                pointShift.__edit__(-5, 0, -10)                                   #a pick goes up/ shift (dependes on the strings' positions)
                jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
                pointShift.__edit__(0, 0, -5)
                jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
                pointShift.__edit__(10, 0, 10)
                jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
            break;
    
        if case('DU'):
            if crossing == 1 or crossing == 2 :
                jit = jit + printer(point, vel, numberN) #string coord + z +10 mm
            if crossing != 2:
                pointShift.__edit__(5, 0, -10)                                    #a pick goes downup/ shift (dependes on the strings' positions)
                jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)#creating new JITstring[] about new pick_position
                pointShift.__edit__(0, 0, -7.5)                                   #a pick goes down then goes up
                jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
                pointShift.__edit__(-10, 0, 0)
                jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
                pointShift.__edit__(10, 0, 13.5)
                jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
            break;
        if case():
            print('Exeption')                                                    #expecting default or exeption
            break

    
    return jit                                                                           #for tests. Expects 'return 0'




