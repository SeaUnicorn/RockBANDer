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

def DegToRad(angleDeg):
    return (angleDeg*3.1416)/180

def RadToDeg(angleRad):
    return (angleRad*180)/3.1416
