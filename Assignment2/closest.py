def closest(lst, K):  
      
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]
      
lst = [1, 2, 3, 4, 5]

n= len(lst)
get_sum = sum(lst)
mean = get_sum / n
K = 2.8
print(closest(lst, K))
