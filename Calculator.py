#Calculator

def sum(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)

print("Please select the operation.")
print("a.sum")
print("b.subtract")
print("c.multiply")
print("d.divide")

choice=input("enter choice (a/b/c/d):")
num_1=int(input("enter frist number:"))
num_2=int(input("enter second number:"))

if(choice=='a'):
    print(num_1,'+',num_2,"=",sum(num_1,num_2))
elif(choice=='b'):
    print(num_1,'-',num_2,"=",subtract(num_1,num_2))
elif(choice=='c'):
    print(num_1,'*',num_2,"=",multiply(num_1,num_2))
if(choice=='d'):
    print(num_1,'/',num_2,"=",divide(num_1,num_2))
else:
    print("This is an invalid input")    

