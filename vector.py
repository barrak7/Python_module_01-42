#!/bin/python

class Vector:
    def __init__(self, values):
        if any(isinstance(i, list) for i in values):
            if (len(values)) == 1:
                for i in values[0]:
                    if not isinstance(i, float):
                        raise TypeError("vector can only contain floating points")
            elif (len(values) > 1):
                for e in values:
                    if len(e) > 1:
                        raise ValueError("Column vectors can only contain 1 value per row")
                    for i in e:
                        if not isinstance(i, float):
                            raise TypeError("Vector can only contain floating points")
            else:
                raise ValueError("Vector can't be empty")
        else:
            raise ValueError("Vector can only contain lists of floats")
        self.values = values
        self.shape = (len(values[0]), len(values))

    def dot(self, v1):
        if not isinstance(v1, Vector) or self.shape != v1.shape:
            raise ValueError("Dot product can only be calculated between two vectors of the same shape")
        i = 0
        re = 0
        if (self.shape[0] == 1):
            for e in self.values[0]:
                re += e * v1.values[0][i]
                i += 1
        else:
            for e in self.values:
                re += e[0] * v1.values[i][0]
                i += 1
        return re

    def T(self):
        r = []

        if (self.shape[0] == 1):
            for e in self.values[0]:
                r.append([e])
            self.values = r
        else:
            for e in self.values:
                for i in e:
                    r.append(i)
            self.values = [r]
        self.shape = (self.shape[1], self.shape[0])
        return self

    def __add__(self, value):
        if not isinstance(value, Vector) or self.shape != value.shape:
            raise ValueError("Vector can only be added to a vector of the same shape")
        if (self.shape[0] == 1):
            l = [x + y for (x, y) in zip(self.values[0],value.values[0])]
            re = Vector([l])
        else:
            l = [[x[0] + y[0]] for x, y in zip(self.values,value.values)]
            re = Vector(l)
        return re

    def __sub__(self, value):
        if not isinstance(value, Vector) or self.shape != value.shape:
            raise ValueError("Vector can only be subtracted from a vector of the same shape")
        if (self.shape[0] == 1):
            l = [x - y for (x, y) in zip(self.values[0],value.values[0])]
            re = Vector([l])
        else:
            l = [[x[0] - y[0]] for x, y in zip(self.values,value.values)]
            re = Vector(l)
        return re

    def __truediv__(self, value):
        if (value == 0):
            raise ZeroDivisionError("Vector division or modulo by zero")
        if not isinstance(value, (int, float)):
            raise ValueError("Vector can only be divided by a scalar")
        if (self.shape[0] == 1):
            l = [x / value for x in self.values[0]]
            re = Vector([l])
        else:
            l = [x[0] / value for x in self.values]
            re = Vector(l)
        return re

    def __rtruediv__(self, value):
        raise NotImplementedError("Division of a scalar by a Vector is not defined")

    def __mul__(self, value):
        if not isinstance(vlaue, (int, float)):
            raise NotImplementedError("Vector can only be multiplied by a scalar")
        if self.shape[0] == 1:
            l = [x * value for x in self.values[0]]
            re = Vector([l])
        else:
            l = [x[0] * value for x in self.values]
            re = Vector(l)
        return re

    def __rmul__(self, value):
        if not isinstance(vlaue, (int, float)):
            raise NotImplementedError("Vector can only be multiplied by a scalar")
        if self.shape[0] == 1:
            l = [x * value for x in self.values[0]]
            re = Vector([l])
        else:
            l = [x[0] * value for x in self.values]
            re = Vector(l)
        return re

    def __str__(self):
       return  return f"This is a vector of the shape ({self.shape[0]},{self.shape[1]}) and of the values {self.values}"

    def __repr__(self):
        return f"Vector({self.values})"
