import math

class switch(object):
    def __init__(self, value):
        self.value = value  # 
        self.fall = False   # 

    def __iter__(self):     # returns one methods only
       
        yield self.match
        raise StopIteration

    def match(self, *args):
        
        if self.fall or not args:
            # if your case is empty, type "pass" in case-block
            return True
        elif self.value in args:
            self.fall = True
            return True
        return False
    def case(*args):
        return any((arg == switch.value for arg in args))
def distance(point1, point2):
    return math.sqrt((point1.X - point2.X)*(point1.X - point2.X) + (point1.Y - point2.Y)*(point1.Y - point2.Y) + (point1.Z - point2.Z)*(point1.Z - point2.Z) )
