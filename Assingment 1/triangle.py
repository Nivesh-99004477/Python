import math

def typeoftriangle(x,y,z):
    if x==y and y==z:
        print("Equilateral Triangle")
    elif x==y or y==z or z==x:
        print("Isosceles Triangle")
    elif x== math.sqrt(y**2 + z**2) or y== math.sqrt(x**2 + z**2) or z== math.sqrt(x**2 + y**2):
        print("Right angle triangle")
    else:
        print("Scalene Triangle")


typeoftriangle(3,4,5)
