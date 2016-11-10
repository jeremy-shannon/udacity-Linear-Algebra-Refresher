from math import sqrt, acos, pi
from decimal import getcontext, Decimal

getcontext().prec = 30


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        out = []
        for item in self.coordinates:
            out.append(str(item.quantize(Decimal('.0001'))))
        return str(out)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
        
    def __add__(self, v):
        newCoords = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(newCoords)

    def __sub__(self, v):
        newCoords = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(newCoords)

    def __mul__(self, x):
        newCoords = [Decimal(x) * y for y in self.coordinates]
        return Vector(newCoords)

    def mag(self):
        sum = 0
        for value in self.coordinates:
            sum += value**2
        sum = sqrt(sum)
        return Decimal(sum)

    def norm(self):
        newCoords = []
        try:
            for value in self.coordinates:
                newCoords.append(Decimal(value)/self.mag())
        except ZeroDivisionError:
            raise Exception("Cannot normalize zero vector")
        return Vector(newCoords)

    def dot(self, v):
        return sum(x * y for x,y in zip(self.coordinates, v.coordinates))

    def angleBetween(self, v):
        try:
            mag1 = self.mag()
            mag2 = v.mag()
        except ZeroDivisionError:
            raise Exception("Cannot calcluate angle with zero vector")
        ratio = Decimal(self.dot(v))/Decimal(mag1*mag2)
        if ratio < -1:
            ratio = -1.
        elif ratio > 1:
            ratio = 1.
        return Decimal(acos(ratio))

    def isZero(self):
        return self.mag() < 1e-10

    def testOrthogonal(self, v):
        return (self.isZero() or 
                v.isZero() or 
                abs(self.dot(v)) < 1e-10)

    def testParallel(self, v):
        return (self.isZero() or 
                v.isZero() or 
                self.angleBetween(v) == 0 or
                self.angleBetween(v) == pi)

    def proj(self, v):
        return v.norm() * self.dot(v.norm())

    def orth(self, v):
        return (self - self.proj(v))

    def cross(self, v):
        if self.dimension == 2 and v.dimension == 2:
            return Vector([0., 
                           0., 
                           (self.coordinates[0] * v.coordinates[1] - self.coordinates[1] * v.coordinates[0])])
        elif self.dimension == 3 and v.dimension == 3:
            return Vector([(self.coordinates[1] * v.coordinates[2] - self.coordinates[2] * v.coordinates[1]),
                           (self.coordinates[2] * v.coordinates[0] - self.coordinates[0] * v.coordinates[2]),
                           (self.coordinates[0] * v.coordinates[1] - self.coordinates[1] * v.coordinates[0])])
        else:
            return Vector([0.,0.,0.])

