def diffbetlow(l):
    min1=min(l)
    l.remove(min(l))
    min2=min(l)
    if min2>min1:
        return min2-min1
    else:
        return min1-min2
