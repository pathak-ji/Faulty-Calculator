# Exercise 2 Faulty Calculator
# 45*3=555, 56+9=77,56/6=4
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
print("Choose the number to perform the operation:")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
temp=int(input())
if temp==1:
    if num1==56:
        if num2==9:
            print(num1, "+", num2, " = 77")
        else:
            print(num1," + ",num2," = ",num1+num2)
    else:
        print(num1," + ",num2," = ",num1+num2)

elif temp==2:
    print(num1," - ",num2," = ",num1-num2)
elif temp==3:
    if num1==45:
        if num2==3:
            print(num1,"*",num2," = 555")
        else:
            print(num1,"*",num2," = ", num1*num2)
    else:
        print(num1,"*",num2," = ",num1*num2)
elif temp==4:
    if num1==56:
        if num2==6:
            print(num1,"/",num2," = 4")
        else:
            print(num1,"/",num2," = ",num1/num2)
    else:
        print(num1,"/",num2," = ",num1/num2)

