def sumfact(number):
    sum=0
    for i in range(1,number+1):
        if number%i==0:
            sum+=i
    return sum

