#pattern print 4
n=int(input("enter no of row"))
for i in range(1,n+1):
    print(" "*(n-i),"*"*i)