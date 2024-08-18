import math
class Complex(object):
    __real__ = 0
    __imag__ = 0

    def __init__(self, x, y):
        self.__real__ = x
        self.__imag__ = y

    def __str__(self):
        if self.__imag__>0:
            return str(self.__real__) + "+" + str(self.__imag__) + "i"
        elif self.__imag__==0:
            return str(self.__real__)
        else: return str(self.__real__) + "-" + str(-self.__imag__) + "i"
    
    # Function
    def module(self):
        return math.sqrt(self.__real__**2+self.__imag__**2)
    
    def add(self, other):
        return Complex(self.__real__+other.__real__, self.__imag__+other.__imag__)
    
    def minus(self, other):
        return Complex(self.__real__-other.__real__, self.__imag__-other.__imag__)
    
    def multi(self, other):
        return Complex(self.__real__*other.__real__ - self.__imag__*other.__imag__, self.__real__*other.__imag__ + self.__imag__*other.__real__)
    
    def devide(self, other):
        return Complex((self.__real__*other.__real__ + self.__imag__*other.__imag__)/(other.__real__**2 + other.__imag__**2), (self.__imag__*other.__real__ - self.__real__*other.__imag__)/(other.__real__**2 + other.__imag__**2))

    def conj(self):
        return Complex(self.__real__, -self.__imag__)
    
    # Nạp chồng toán tử
    def __add__(self, other): # + cộng
        return Complex(self.__real__+other.__real__, self.__imag__+other.__imag__)
    
    def __sub__(self, other): # - trừ
        return Complex(self.__real__-other.__real__, self.__imag__-other.__imag__)
    
    def __mul__(self, other): # * nhân
        return Complex(self.__real__*other.__real__ - self.__imag__*other.__imag__, self.__real__*other.__imag__ + self.__imag__*other.__real__)

    def __truediv__(self, other): # / chia
        return Complex((self.__real__*other.__real__ + self.__imag__*other.__imag__)/(other.__real__**2 + other.__imag__**2), (self.__imag__*other.__real__ - self.__real__*other.__imag__)/(other.__real__**2 + other.__imag__**2))

    def __invert__(self): # ~ liên hợp
        return Complex(self.__real__, -self.__imag__)
com = Complex(2, 3)
com2 = Complex(3, 4)
add = Complex.add(com, com2)
minus = Complex.minus(com, com2)
mul = Complex.multi(com, com2)
devide = Complex.devide(com, com2)
print(Complex.module(com2))
print(add)
print(minus)
print(mul)
print(devide)
print(Complex.conj(com))
return_add = com + com2
return_sub = com - com2
return_mul = com*com2
return_truediv = com/com2
return_invert = ~com
print(Complex.module(com2))
print(return_add)
print(return_sub)
print(return_mul)
print(return_truediv)
print(return_invert)

print(Complex.module(com))
print(Complex.add(com, com2))
print(Complex.minus(com, com2))
print(Complex.multi(com, com2))
print(Complex.devide(com, com2))
print(Complex.conj(com))