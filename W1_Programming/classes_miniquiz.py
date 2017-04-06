class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

    def distance(self, other):
        x_distance = abs(self.x - other.x)
        y_distance = abs(self.y - other.y)
        return (x_distance**2 + y_distance**2)**.5

class Triangle(object):
    '''INPUT: three Point objects
    '''
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.d12 = self.p1.distance(self.p2)
        self.d23 = self.p2.distance(self.p3)
        self.d31 = self.p3.distance(self.p1)

    def __repr__(self):
        return'Triangle({}, {}, {})'.format(self.p1, self.p2, self.p3)

    def perimeter(self):
        return self.d12 + self.d23 + self.d31

    def is_line(self):
        if self.perimeter == 2*max(self.d12, self.d23, self.d31):
            return True
        else:
            return False
