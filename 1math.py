import math

def convert(deg):
    return math.radians(deg)

degree = int(input("Input degree: "))
print('Output radian:', convert(degree))

