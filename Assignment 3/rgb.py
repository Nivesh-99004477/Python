def decToHexa(n):
 
    hexaDeciNum = ['0'] * 100
    i = 0
     
    while (n != 0):

        temp = 0

        temp = n % 16
 
        if (temp < 10):
            hexaDeciNum[i] = chr(temp + 48)
            i = i + 1
 
        else:
            hexaDeciNum[i] = chr(temp + 55)
            i = i + 1
 
        n = int(n / 16)
 
    hexCode = ""
    if (i == 2):
        hexCode = hexCode + hexaDeciNum[0]
        hexCode = hexCode + hexaDeciNum[1]
 
    elif (i == 1):
        hexCode = "0"
        hexCode = hexCode + hexaDeciNum[0]
 
    elif (i == 0):
        hexCode = "00"
    return hexCode
def convertRGBtoHex(R, G, B):
 
    if ((R >= 0 and R <= 255) and
        (G >= 0 and G <= 255) and
        (B >= 0 and B <= 255)):
 
        hexCode = "#";
        hexCode = hexCode + decToHexa(R)
        hexCode = hexCode + decToHexa(G)
        hexCode = hexCode + decToHexa(B)
        return hexCode
 
    else:
        return "-1"

R = 0
G = 0
B = 0
print (convertRGBtoHex(R, G, B))
 
R = 255
G = 255
B = 255
print (convertRGBtoHex(R, G, B))
 
R = 20
G = 45
B = 246
print (convertRGBtoHex(R, G, B))
 
R = 2
G = 3
B = 4
print (convertRGBtoHex(R, G, B))
 
R = 258
G = 265
B = 245
print (convertRGBtoHex(R, G, B))