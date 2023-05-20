#wap to calculate the grade of a student from the following scheme

marks=int(input("enter marks:"))
if(marks>100):
    print("invilid")
elif(marks>90 and marks<=100):
    print("a+")
elif(marks<=90 and marks>=80):
    print("a")
elif(marks<=80 and marks>=70):
    print("b")
elif(marks<=70 and marks>=60):
    print("c")
elif(marks<=60 and marks>=50):
    print("d")
elif(marks<=50 and marks>=40):
    print("e")  
else:
    print("carry over")