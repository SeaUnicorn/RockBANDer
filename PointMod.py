import math
class point:
      def __init__(self, X, Y, Z, A, B, C):
          self.X = X
          self.Y = Y
          self.Z = Z
          self.A = A
          self.B = B
          self.C = C
class pointShift:
      def __init__(self, Lx, Ly, Lz):
        self.Lx = Lx
        self.Ly = Ly
        self.Lz = Lz
      def __edit__(self, Lx, Ly, Lz):
        self.Lx = Lx
        self.Ly = Ly
        self.Lz = Lz

def Modification(point, pointShift, angleZX, angleZY):
    cosZX = math.cos(DegToRad(angleZX));
    sinZX = math.sin(DegToRad(angleZX));
    cosZY = math.cos(DegToRad(angleZY));
    sinZY = math.sin(DegToRad(angleZY));
    
    point.X = (point.X + pointShift.Lx*cosZY +
               pointShift.Ly*sinZY*sinZX +
               pointShift.Lz*sinZY*cosZX)

    point.Y = (point.Y + pointShift.Ly*cosZX -
               pointShift.Lz*sinZX)

    point.Z = (point.Z - pointShift.Lx*sinZX +
               pointShift.Ly*cosZY*sinZX +
               pointShift.Lz*cosZY*cosZX)
    
    return point


def DegToRad(angleDeg):
    return (angleDeg*3.1416)/180

def RadToDeg(angleRad):
    return (angleRad*180)/3.1416
