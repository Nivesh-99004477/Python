def triangle(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")



from math import fact


def pascaltriangle(n):
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            print(fact(i)//(fact(j)*fact(i-j)), end=" ")
        print()

pascaltriangle(5)
triangle(4)