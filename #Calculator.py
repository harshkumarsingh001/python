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
    print(sum(num_1,num_2))
elif(choice=='b'):
    print(subtract(num_1,num_2))
elif(choice=='c'):
    print(multiply(num_1,num_2))
if(choice=='d'):
    print(divide(num_1,num_2))
else:
    print("This is an invalid input")    



