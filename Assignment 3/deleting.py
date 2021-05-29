def maxnumber(num, k):

    for i in range(0, k):
        
        a = 0
        i = 1
       
        while num // i > 0:
        
            temp = (num//(i * 10))*i + (num % i)
            i *= 10
        
            if temp > a:
                a = temp
        num = a     
   
    
    return a
   
  
