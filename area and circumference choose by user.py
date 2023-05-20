'''area and circumference choose by user'''

a=float(input("enter the radius"))
print("press 1 for area")
print("press 2 for circumference")
x=int(input())
if(x==1):
    print("area",3.14*a**2)
elif(x==2):
    print("circumference",2*3.14*a)
else:
    print("invalid choose")

