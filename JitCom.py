import helper #switch-case 
import math   #sin/cos
import PointMod #point (position) and point modification

def printer(point, vel, numberN):                                                       #a JITstring[] former
    numberN = numberN+10
    return ('N'+ str(numberN) + ' G01' + ' X=' + str(point.X) +
                    ' Y=' + str(point.Y) + ' Z=' + str(point.Z) +
                    ' A=' + str(point.A) + ' B=' + str(point.B) +
                    ' C=' + str(point.C) +' F' + str(vel)+ ' \n' )

def JITMaker(mode, numberN, angleZX, angleZY, point, vel):
    f = open('jit.txt', 'w')                                                             #open text-file for JITs
    pointShift = PointMod.pointShift(0,0,0)                                              #just creating an obj
    #jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
    jit = '\n'
    for case in helper.switch(mode):
        
        if case('D'):
            jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN) #string coord + z +10 mm
            jit = jit + ('N'+ str(numberN) + ' LOOP \n')
            pointShift.__edit__(5, 0, -10)                                    #a pick goes down/ shift (dependes on the strings' positions)
            jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)#creating new JITstring[] about new pick_position
            pointShift.__edit__(0, 0, -5)
            jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
            pointShift.__edit__(-10, 0, 10)
            jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
            jit = jit + ('N'+ str(numberN) + ' ENDLOOP \n')
            break;
    
        if case('U'):
            jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN) #string coord + z +10 mm
            jit = jit + ('N'+ str(numberN) + ' LOOP \n')
            pointShift.__edit__(-5, 0, -10)                                   #a pick goes up/ shift (dependes on the strings' positions)
            jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
            pointShift.__edit__(0, 0, -5)
            jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
            pointShift.__edit__(10, 0, 10)
            jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
            jit = jit + ('N'+ str(numberN) + ' ENDLOOP \n')
            break;
    
        if case('DU'):
            jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN) #string coord + z +10 mm
            pointShift.__edit__(5, 0, -10)                                    #a pick goes downup/ shift (dependes on the strings' positions)
            jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)#creating new JITstring[] about new pick_position
            jit = jit + ('N'+ str(numberN) + ' LOOP \n')
            pointShift.__edit__(0, 0, -2.5)                                   #a pick goes down then goes up
            jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
            pointShift.__edit__(-10, 0, 0)
            jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
            jit = jit + ('N'+ str(numberN) + ' ENDLOOP \n')
            break;
        if case():
            print('Exeption')                                                    #expecting default or exeption
            break

    f.write(jit)                                                                        #writing JITs down to the file
    f.close()
    return jit                                                                           #for tests. Expects 'return 0'



def Tester():
    FirstString = PointMod.point(50, 0, 50, 0, 0, 0) # set first point here(highest string)
    #SecondString = PointMod.Modification(FirstString, PointMod.pointShift(-20,0,0), -45,0) #distance between strings - 2 sm
    #ThirdString = PointMod.Modification(FirstString, PointMod.pointShift(-40,0,0), -45,0)
    #ForthString = PointMod.Modification(FirstString, PointMod.pointShift(-60,0,0), -45,0)
    NumberN = 10;
    JITMaker('DU', NumberN, -45, 0, FirstString, 10000) #the angle changes clockwise
    print('OK')
