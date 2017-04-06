import numbers

class Fraction(object):
    ''' Makes a fraction object '''

    def __init__(self, num=0, denom=1):
        ''' runs when object instantiated '''
        self.num = num
        self.denom = denom

    def __str__(self):
        ''' tells python how to represent the object
        NOTE: This should be some sort of pretty print output whereas repr
          should return useful logging information.  If only one magic method
          is implemented, always implement repr
        '''
        return "{0}/{1}".format(self.num, self.denom)

    def __repr__(self):
        ''' tells python how to represent the object '''
        return "Fraction({0}, {1})".format(self.num, self.denom)

    def __add__(self, other):
        ''' overload the + operator
        NOTE: This should ALWAYS return a new object and not modify the current
          object in place
        '''
        if isinstance(other, Fraction):
            return Fraction((self.num*other.denom) + (other.num*self.denom),
                            self.denom*other.denom)
        elif isinstance(other, numbers.Real):
            return Fraction(self.num + (other*self.denom), self.denom)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other


if __name__ == '__main__':
    f1 = Fraction(num=2, denom=3)
    f2 = Fraction(num=1, denom=4)
