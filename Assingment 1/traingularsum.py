def trisum(number):
    sum=0
    for i in range(1,number+1):
        for j in range(0,i+1):
            sum+=j
    return sum

