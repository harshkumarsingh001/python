#pattern printing 01

n=int(input("enter number"))
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        print(i,end=" ")
    print()       
    
    
    # output(when n is 3)
    #        1 1 1 
    #        2 2 2 
    #        3 3 3 