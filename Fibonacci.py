def FibonacciSeries(seriesLength):
    x =0
    y =1
    #z = 0
    for i in (range(0,seriesLength)):
        if(i==0):
            print(x)
        elif(i==1):
            print(y)
        else:
            z = x +y
            print(z)
            x = y
            y= z
        

FibonacciSeries(9)
    