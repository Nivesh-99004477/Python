def smallmean(l):
    sum1=sum(l)
    return sum1/len(l)

def mean(l1):
    smallmean1=smallmean(l1)
    count=0
    for i in range(0,len(l1)):
        if l1[i]<smallmean1:
            count+=1
    return count 