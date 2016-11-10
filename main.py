from vector import *
from line import *
from math import pi

print "magnitude:"

v1 = Vector([-.221, 7.437])
print v1.mag()
v2 = Vector([8.813, -1.331, -6.247])
print v2.mag()

print ""
print "norm:"

v3 = Vector([5.581,-2.136])
print v3.norm()
v4 = Vector([1.996, 3.108, -4.554])
print v4.norm()

print ""
print "dot product:"

v1 = Vector([7.887, 4.138])
v2 = Vector([-8.802, 6.776])
print v1.dot(v2)

v1 = Vector([-5.955, -4.904, -1.874])
v2 = Vector([-4.496,-8.755,7.103])
print v1.dot(v2)

print ""
print "angle between:"

v1 = Vector([3.183,-7.627])
v2 = Vector([-2.668,5.319])
print v1.angleBetween(v2)

v1 = Vector([7.35, .221, 5.188])
v2 = Vector([2.751, 8.259, 3.985])
print (v1.angleBetween(v2) * 180/pi)

print ""
print "test parallel, test orthogonal:"

v1 = Vector([-7.579, -7.88])
v2 = Vector([22.737, 23.64])
print v1.testParallel(v2)
print v1.testOrthogonal(v2)

v1 = Vector([-2.029, 9.97, 4.172])
v2 = Vector([-9.231, -6.639, -7.245])
print v1.testParallel(v2)
print v1.testOrthogonal(v2)

v1 = Vector([-2.328, -7.284, -1.214])
v2 = Vector([-1.821, 1.072, -2.94])
print v1.testParallel(v2)
print v1.testOrthogonal(v2)

print ""
print "projection:"

v1 = Vector([3.039, 1.879])
v2 = Vector([0.825, 2.036])
print v1.proj(v2)

print ""
print "orthogonal:"

v1 = Vector([-9.88, -3.264, -8.159])
v2 = Vector([-2.155, -9.353, -9.473])
print v1.orth(v2)

print ""
print "proj and orth components:"

v1 = Vector([3.009, -6.172, 3.692, -2.51])
v2 = Vector([6.404, -9.144, 2.759, 8.718])
print v1.proj(v2)
print v1.orth(v2)

print ""
print "cross product:"

v1 = Vector([8.462, 7.893, -8.187])
v2 = Vector([6.984, -5.975, 4.778])
print v1.cross(v2)

v1 = Vector([1.5, 2.2])
v2 = Vector([3.3, 4.4])
print v1.cross(v2)

v1 = Vector([1., 0.])
v2 = Vector([0., 1.])
print v1.cross(v2)

print ""
print "parallelogram area:"

v1 = Vector([-8.987, -9.838, 5.031])
v2 = Vector([-4.268, -1.861, -8.866])
print v1.cross(v2).mag()

print ""
print "triangle area:"

v1 = Vector([1.5, 9.547, 3.691])
v2 = Vector([-6.007, .124, 5.772])
print v1.cross(v2).mag() * Decimal('0.5')


print ""
print "line intersections:"
l1 = Line([4.046,2.836],1.21)
l2 = Line([10.115,7.09],3.025)
print l1.getIntersect(l2)

l1 = Line([7.204,3.182],8.68)
l2 = Line([8.172,4.114],9.883)
print l1.getIntersect(l2)

l1 = Line([1.182,5.562],6.744)
l2 = Line([1.773,8.343],9.525)
print l1.getIntersect(l2)