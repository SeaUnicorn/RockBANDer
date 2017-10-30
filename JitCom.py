import helper #switch-case 
import math   #sin/cos
import PointMod #point (position) and point modification

def printer(point, vel, numberN):                                                       #a JITstring[] former
    numberN = numberN+10
    return ('N'+ str(numberN) + ' G01' + ' X=' + str(point.X) +
                    ' Y=' + str(point.Y) + ' Z=' + str(point.Z) +
                    ' A= ' + str(point.A) + ' B= ' + str(point.B) +
                    ' C =' + str(point.C) +' F' + str(vel)+ ' \n' )

def JITMaker(mode, numberN, angleZX, angleZY, point, vel):
    f = open('jit.txt', 'w')                                                             #open text-file for JITs
    pointShift = PointMod.pointShift(0,0,0)                                              #just creating an obj
    jit = 'OK \n'
    for case in helper.switch(mode):
        if case('D'): pointShift.__edit__(10, 0, -30)                                    #a pick goes down/ shift (dependes on the strings' positions)
        jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)#creating new JITstring[] about new pick_position 
        pointShift.__edit__(-20, 0, 10)
        jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
        pointShift.__edit__(10, 0, 20)
        jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
        break
        if case('U'): pointShift.__edit__(-10, 0, -30)                                   #a pick goes up/ shift (dependes on the strings' positions)
        jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN) 
        pointShift.__edit__(20, 0, 10)
        jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
        pointShift.__edit__(-10, 0, 20)
        jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
        break
        if case('DU'): pointShift.__edit__(10, 0, -30)                                   #a pick goes down then goes up
        jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
        pointShift.__edit__(-20, 0, 10)
        jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
        pointShift.__edit__(0, 0, -10)
        jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
        pointShift.__edit__(20, 0, 10)
        jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
        pointShift.__edit__(-10, 0, 20)
        jit = jit + printer(PointMod.Modification(point, pointShift, angleZX, angleZY), vel, numberN)
        break
        if case():  print('Exeption')                                                    #expecting default or exeption 

    f.write(jit);                                                                        #writing JITs down to the file
    f.close();
    return jit                                                                           #for tests. Expects 'return 0'



def Tester():
    pointT = PointMod.point(40, 0, 35, 0, 0, 0)
    JITMaker('D', 10, 0, 0, pointT, 10000)
    print('OK')
