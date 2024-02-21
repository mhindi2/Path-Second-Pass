import math

tolerance = 1e-12


# some simple 2D geometrical objects
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceTo(self, point):
        return math.sqrt((self.x - point.x)*(self.x - point.x) +
                         (self.x - point.x)*(self.x - point.x))

    def projectionOn(self, line2D):
        pv = Vector2D(self.x, self.y)  # make vector out of point
        p0v = Vector2D(line2D.p0.x, line2D.p0.y)  # make vector out of line start
        p0p = pv - p0v  # vector from fist point to this point
        uline = line2D.direction() # unit vector along line
        vproj = p0v + p0p.dot(uline) * uline
        return Point2D(vproj.x, vproj.y)

    def vector(self):
        return Vector2D(self.x, self.y)

    def __str__(self):
        return f"Point2D({self.x}, {self.y})"


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.x*self.x+self.y*self.y)

    def angle(self):
        return math.atan2(self.y, self.x)

    def unit(self):
        length = self.length()
        if length == 0:
            return None
        else:
            return Vector2D(self.x/length, self.y/length)

    def perpTo(self):
        return Vector2D(self.y, -self.x)

    def normalize(self):
        length = self.length()
        if length > 0:
            self.x = self.x/length
            self.y = self.y/length
            return self
        else:
            return None

    def point(self):
        return Point2D(self.x, self.y)

    def dot(self, v2):
        return self.x*v2.x + self.y*v2.y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x*scalar, self.y*scalar)

    def __rmul__(self, scalar):
        return self*scalar

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"


class Line2D:
    def __init__(self, p0, p1):
        # end points p0, p1
        self.p0 = p0
        self.p1 = p1

    def length(self):
        return math.sqrt((self.p1.x - self.p0.x)**2 +
                         (self.p1.y - self.p0.y)**2)

    def direction(self):
        v = Vector2D(self.p1.x - self.p0.x, self.p1.y - self.p0.y)
        return v.unit()

    def intersectionPoint(self, other):
        # return the intersection of this line with another line

        t1, t2 = self.intersectionParameters(other)
        pv = self.p0.vector() + t1*(self.p1.vector() - self.p0.vector())
        return pv.point()

    def intersectionParameters(self, other):
        # return intersection parameters t1, t2
        # parameteric equation of line:
        # r = p0 + t(p1-p0)
        # common point of two lines is obtained by solving
        # r = self.p0 + t1(self.p1 - self.p0) =
        #      other.p0 + t2(other.p1 - other.p0)

        # solutions are :
        # t1 = other.p0 - self.p0.u2perp/(p1-p0).u2perp
        # t2 = p0 - other.p0.u1perp/(other.p1-other.p0).u1perp

        u1 = self.direction()
        u2 = other.direction()
        u1Perp = u1.perpTo()
        u2Perp = u2.perpTo()

        v10 = self.p0.vector()
        v11 = self.p1.vector()
        v20 = other.p0.vector()
        v21 = other.p1.vector()

        denom = (v11-v10).dot(u2Perp)
        if abs(denom) < tolerance:
            t1 = None
        else:
            t1 = (v20 - v10).dot(u2Perp) / denom

        denom = (v21-v20).dot(u1Perp)
        if abs(denom) < tolerance:
            t2 = None
        else:
            t2 = (v10 - v20).dot(u1Perp) / denom

        return (t1, t2)

    def point(self, t):
        # return point2D at parameter t on the line
        v = self.p0.vector() + t * (self.p1.vector() - self.p0.vector())
        return v.point()

    def __str__(self):
        return f"Line2D({self.p0}, {self.p1})"
