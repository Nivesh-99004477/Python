def leap(num):
    if num%100==0 and num%400:
        return True
    elif num%4==0:
        return True
    else:
        return False

print(leap(2002))