class Fraction:
    @staticmethod
    def gcd(numerator, denominator):
        while numerator % denominator != 0:
            numerator, denominator = denominator, numerator % denominator
        return denominator

    @staticmethod
    def sgn(numerator):
        if numerator > 0:
            return 1
        elif numerator < 0:
            return -1
        else:
            return 0

    def __init__(self, numerator, denominator):
        if numerator == 0:
            self.numerator = 0
            self.denominator = 1
        else:
            sign = self.sgn(numerator) * self.sgn(denominator)
            num = abs(numerator)
            den = abs(denominator)
            self.numerator = sign * num
            self.denominator = den

    def __str__(self):
        return f'The fraction: <numerator={self.numerator}, denominator={self.denominator}'

    def __repr__(self):
        return f'The fraction: <numerator={self.numerator}, denominator={self.denominator}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            num = self.numerator * other.denominator + self.denominator * other.numerator
            denom = self.denominator * other.denominator
        elif isinstance(other, int):
            num = self.numerator + self.denominator * other
            denom = self.denominator
        else:
            return NotImplemented
        gcd_val = self.gcd(num, denom)
        return self.__class__(num // gcd_val, denom // gcd_val)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            num = self.numerator * other.denominator - self.denominator * other.numerator
            denom = self.denominator * other.denominator
        elif isinstance(other, int):
            num = self.numerator - self.denominator * other
            denom = self.denominator
        else:
            return NotImplemented
        gcd_val = self.gcd(num, denom)
        return self.__class__(num // gcd_val, denom // gcd_val)

    def __rsub__(self, other):
        res = self.__sub__(other)
        if other > self.numerator / self.denominator:
            return self.__class__(res.numerator * (-1), res.denominator)
        else:
            return res

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.numerator * other.numerator, self.denominator * other.denominator)
        elif isinstance(other, int):
            return self.__class__(self.numerator * other, self.denominator)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.numerator * other.denominator, self.denominator * other.numerator)
        elif isinstance(other, int) or isinstance(other, float):
            if other != 0:
                return self.__class__(self.numerator, self.denominator * other)
            else:
                raise ZeroDivisionError
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        if other > self.numerator / self.denominator:
            res = self.__rmul__(self.__class__(1, other))
            res.numerator, res.denominator = res.denominator, res.numerator
            return res
        return self.__truediv__(other)

    def __pow__(self, power, modulo=None):
        if power == 0:
            return 1
        elif power == 1:
            return self
        else:
            return self.__class__(self.numerator ** power, self.denominator ** power)

    def __float__(self):
        return self.numerator / self.denominator

    def __int__(self):
        return self.numerator // self.denominator

    def __bool__(self):
        return self.numerator != 0

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return self.numerator / self.denominator < other.numerator / other.denominator

    def reduct(self, numerator, denominator):
        numerator = numerator // abs(self.gcd(numerator, denominator))
        denominator = denominator // abs(self.gcd(numerator, denominator))
        return self.__class__(numerator, denominator)