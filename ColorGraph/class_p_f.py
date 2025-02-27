import math


class point:
    def __init__(self,x,y,z):
        self.x =x
        self.y =y
        self.z = z
        
class face:
    def __init__(self, v1,v2,v3, list_point):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.S = self.get_S(list_point)
    def get_S(self, list_point):
        p1 = list_point[self.v1-1]
        p2 = list_point[self.v2-1]
        p3 = list_point[self.v3-1]
        v1v2 = math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2 + (p1.z-p2.z)**2)
        v1v3 = math.sqrt((p1.x-p3.x)**2 + (p1.y-p3.y)**2 + (p1.z-p3.z)**2)
        v2v3 = math.sqrt((p2.x-p3.x)**2 + (p2.y-p3.y)**2 + (p2.z-p3.z)**2)
        P = .5*(v1v2+v1v3+v2v3)
        return  math.sqrt(P*(P-v1v3)*(P-v1v2)*(P-v2v3))