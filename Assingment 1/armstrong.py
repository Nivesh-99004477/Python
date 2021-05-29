def armstr(num):
    count=0
    result=0
    rem=0
    temp=num
    temp1=num
    while temp!=0:
        count+=1
        temp//=10
    while temp1!=0:
        rem=temp1%10
        result+= rem ** count
        temp1//=10
    
    if num==result:
        return True
    else:
        return False
