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

def Crossing(Strings, PositionLast, PositionNext):
    for i in Strings:
        k = (i.Y - PositionLast.Y)/(i.X - PositionLast.X)
        b = i.Y - k*i.X
        if b-k*PositionNext.X - PositionNext.Y > 0:
            return 1
    return 0

def Play(stringNum, angleZX, angleZY, NumberN, mode, point):
    FirstString = copy.deepcopy(point) # set first point here(highest string)
    S = Strings(FirstString, angleZX, angleZY)
    for case in helper.switch(stringNum):
        
        if case(1):
            JitCom.JITMaker(mode, NumberN, angleZX, angleZY, S[0], 10000) #the angle changes clockwise
            break;
        if case(2):
            JitCom.JITMaker(mode, NumberN, angleZX, angleZY, S[1], 10000) #the angle changes clockwise
            break;
        if case(3):
            JitCom.JITMaker(mode, NumberN, angleZX, angleZY, S[2], 10000) #the angle changes clockwise
            break;
        if case(4):
            JitCom.JITMaker(mode, NumberN, angleZX, angleZY, S[3], 10000) #the angle changes clockwise
            break;
    PositionLast = PointMod.point(45, 0, 45, 0, 0, 0) # set first point here(highest string)
    PositionNext = PointMod.point(20, 0, 55, 0, 0, 0) # set first point here(highest string)
    return Crossing(S, PositionLast, PositionNext)
    




