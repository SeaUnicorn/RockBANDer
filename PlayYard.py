import helper #switch-case 
import math   #sin/cos
import PointMod #point (position) and point modification
import JitCom
import copy



def Strings(point1, angleZX, angleZY):
    pointShift = PointMod.pointShift(-20, 0, 0)
    point2 = PointMod.Modification(copy.deepcopy(point1), pointShift, angleZX, angleZY)
    point3 = PointMod.Modification(copy.deepcopy(point2), pointShift, angleZX, angleZY)
    point4 = PointMod.Modification(copy.deepcopy(point3), pointShift, angleZX, angleZY)
    return [point1, point2, point3, point4]

def Play(stringNum, angleZX, angleZY, NumberN, mode):
    FirstString = PointMod.point(100, 0, 100, 0, 0, 0) # set first point here(highest string)
    S = Strings(FirstString, 0, 0)
    for case in helper.switch(stringNum):
        
        if case(1):
            JitCom.JITMaker(mode, NumberN, angleZX, angleZX, S[0], 10000) #the angle changes clockwise
            break;
        if case(2):
            JitCom.JITMaker(mode, NumberN, angleZX, angleZX, S[1], 10000) #the angle changes clockwise
            break;
        if case(3):
            JitCom.JITMaker(mode, NumberN, angleZX, angleZX, S[2], 10000) #the angle changes clockwise
            break;
        if case(4):
            JitCom.JITMaker(mode, NumberN, angleZX, angleZX, S[3], 10000) #the angle changes clockwise
            break;

def Test():
    FirstString = PointMod.point(100, 0, 100, 0, 0, 0) # set first point here(highest string)
    Play(2, 0, 0, 10, 'D')
