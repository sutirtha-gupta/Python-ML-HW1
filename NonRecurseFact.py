def nonRecursefact(n):
    fact = 1

    while (n>0):
        fact = n*fact
        #print(fact)
        n = n-1
        
        
    return fact
        
       
     
    

x = 5
y = nonRecursefact(5)
print(y)