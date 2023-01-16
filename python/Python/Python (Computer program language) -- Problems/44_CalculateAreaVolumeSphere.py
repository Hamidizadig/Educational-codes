class Sphere:
    PI = 3.1415
    r = 0

    def __init__(self, r):
        if r > 0:
            self.r = r
        else:
            self.r = 0

    def Volume(self):
        return(4.0/3) * self.r ** 3 * self.PI

    def Area(self):
        return 4.0 * self.r ** 2 * self.PI
    r = int(input('Enter r : '))
    s = Sphere(r)
    print('Volume is', s.Volume(), '    Area is : ', s.Area())
