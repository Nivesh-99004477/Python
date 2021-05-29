import cmath

def quad(a,b,c):
    n=[]
    D=b**2 - 4*a*c
    if D>0:
        res1= -b + cmath.sqrt(D)
        root1=res1/2*a
        res2= -b - cmath.sqrt(D)
        root2=res2/2*a
        n.extend([root1,root2])
        return n
    elif D==0:
        root1=root2= -b / 2*a
        n.extend([root1,root2])
        return n
    else:
        res1= -b/2*a + cmath.sqrt(-D)
        root1=res1/2*a
        res2= -b/2*a - cmath.sqrt(-D)
        root2=res2/2*a
        n.extend([root1,root2])
        return n

