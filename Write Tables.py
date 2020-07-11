def tables():
    for x in range(1,11):
        print ("table of %d starts" % x)
        
        for y in range (1,11):
            print("%d x %d = %d" % (x,y, (x*y)))
        print()
        print ("table of %d completed" % x)
        print ('-'*20)
        

tables()