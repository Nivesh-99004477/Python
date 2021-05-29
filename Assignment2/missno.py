def missno(oldlist,newlist):
    n=[]
    n.extend(set(oldlist).difference(newlist))
    return n

