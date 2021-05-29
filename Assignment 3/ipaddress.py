def ip(num):
    parts = num.split('.')
    x=(int(parts[0]) << 24) + (int(parts[1]) <<16)  + (int(parts[2]) << 8) + int(parts[3])
    return x



z=ip('4.5.6.7')
print(z)