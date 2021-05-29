def tribo(num):
    if num==0 or num==1 or num==2:
        return 0
    elif num==3:
        return 1
    else:
        return tribo(num-1)+tribo(num-2)+tribo(num-3)


