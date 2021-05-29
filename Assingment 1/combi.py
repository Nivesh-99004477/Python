def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)


def combination(n,r):
    res1=res2=0
    res1=fact(n)
    res2=fact(r)*fact(n-r)
    return res1//res2

