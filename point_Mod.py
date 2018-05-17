import math
class point: #geom.point
      def __init__(self, X, Y, Z, A, B, C):
          self.X = X
          self.Y = Y
          self.Z = Z
          self.A = A #Euler angles
          self.B = B #
          self.C = C #
      def __edit__(self, X, Y, Z):
          self.X = X
          self.Y = Y
          self.Z = Z  
class pointShift:
      def __init__(self, Lx, Ly, Lz): #point shift linear
        self.Lx = Lx
        self.Ly = Ly
        self.Lz = Lz
      def __edit__(self, Lx, Ly, Lz):
        self.Lx = Lx
        self.Ly = Ly
        self.Lz = Lz

def modification(point, pointShift, angleZX, angleZY): #point rotation
    cosA = math.cos(DegToRad(angleZX)); #Y-rot
    sinA = math.sin(DegToRad(angleZX));
    cosT = math.cos(DegToRad(angleZY)); #X-rot
    sinT = math.sin(DegToRad(angleZY));
    
    point.X = (point.X + pointShift.Lx*cosA*cosT -
               pointShift.Ly*sinA*sinT +
               pointShift.Lz*sinA)

    point.Y = (point.Y + pointShift.Lx*sinT -
               pointShift.Ly*cosT)

    point.Z = (point.Z - pointShift.Lx*sinA*cosT +
               pointShift.Ly*sinA*sinT +
               pointShift.Lz*cosA)
    
    return point


def DegToRad(angleDeg): #degrees to radians
    return (angleDeg*3.1416)/180

def RadToDeg(angleRad): #radians to degrees
    return (angleRad*180)/3.1416
