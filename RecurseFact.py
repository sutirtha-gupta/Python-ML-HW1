def recurseFact(n):
    fact = 1
    while (n>0):
        fact = n* recurseFact(n-1)
        break
    return fact

x = 5
print(recurseFact(x))
        
        