from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def swap_rows(self, row1, row2):
        if row1 == row2:
            return
        elif row1 < 0 or row1 >= len(self) or row2 < 0 or row2 >= len(self):
            print "row dimension out of range for swap"
        else:
            temp = self.planes[row1]
            self.planes[row1] = self.planes[row2]
            self.planes[row2] = temp


    def multiply_coefficient_and_row(self, coefficient, row):
        newNormalVector = self[row].normal_vector * coefficient
        newConst = self[row].constant_term * coefficient
        self[row] = Plane(newNormalVector.coordinates, newConst)


    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        newNormalVector = self[row_to_be_added_to].normal_vector + (self[row_to_add].normal_vector * coefficient)
        newconstant_term = self[row_to_be_added_to].constant_term + coefficient * self[row_to_add].constant_term
        self[row_to_be_added_to] = Plane(newNormalVector.coordinates, newconstant_term)

    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector.coordinates)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices

    def compute_triangular_form(self):
        s = deepcopy(self)
        for i in range(s.dimension):
            if i >= len(s):
                break
            if s[i].normal_vector.coordinates[i] == 0:
                for j in range((i+1),len(s)):
                    if s[j].normal_vector.coordinates[i] != 0:
                        s.swap_rows(i,j)
                        break
        for i in range(len(s)):
            for j in range((i+1), len(s)):
                if j > s.dimension:
                    break
                if s[j].normal_vector.coordinates[i] != 0:
                    coef1 = s[i].normal_vector.coordinates[i]
                    coef2 = s[j].normal_vector.coordinates[i]
                    coefToAdd = Decimal(-1.)*coef2/coef1
                    s.add_multiple_times_row_to_row(coefToAdd,i,j)
                
        return s

    def compute_rref(self):
        tf = self.compute_triangular_form()
        for i in reversed(range(len(tf))):
            leadingCoefIndex = None
            try:
                leadingCoefIndex = Plane.first_nonzero_index(tf[i].normal_vector.coordinates)
            except:
                pass
            if leadingCoefIndex or leadingCoefIndex == 0:
                leadingCoef = tf[i].normal_vector.coordinates[leadingCoefIndex]
                tf.multiply_coefficient_and_row(Decimal(1.)/leadingCoef,i)
                for j in range(0,i):
                    rowJCoef = tf[j].normal_vector.coordinates[leadingCoefIndex]
                    tf.add_multiple_times_row_to_row(Decimal(-1.)*rowJCoef,i,j)
        return tf

    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps

print "********************test case 1 *******************************"
p1 = Plane(normal_vector=(['5.862','1.178','-10.366']), constant_term='-8.15')
p2 = Plane(normal_vector=(['2.931','-0.589','5.183']), constant_term='-4.075')
s = LinearSystem([p1,p2])
r = s.compute_rref()
print r

print "********************test case 2 *******************************"
p1 = Plane(normal_vector=(['8.631','5.112','-1.816']), constant_term='-5.113')
p2 = Plane(normal_vector=(['4.315','11.132','-5.27']), constant_term='-6.775')
p3 = Plane(normal_vector=(['-2.158','3.01','-1.727']), constant_term='-0.831')
s = LinearSystem([p1,p2,p3])
r = s.compute_rref()
print r

print "********************test case 3 *******************************"
p1 = Plane(normal_vector=(['5.262','2.739','-9.878']), constant_term='-3.441')
p2 = Plane(normal_vector=(['5.111','6.358','7.638']), constant_term='-2.152')
p3 = Plane(normal_vector=(['2.016','-9.924','-1.367']), constant_term='-9.278')
p4 = Plane(normal_vector=(['2.167','-13.543','-18.883']), constant_term='-10.567')
s = LinearSystem([p1,p2,p3,p4])
r = s.compute_rref()
print r
