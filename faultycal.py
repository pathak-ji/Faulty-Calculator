# You have to create a faulty calculator which provides wrong result only in these particular cases. Case1- 56+9=77, Case2- 45*3=555, Case3- 56/6=4.
def calculator():
    operation = input('''
    Please type in the math operation you would like to complete:
     + for addition, - for subtraction, * for multiplication, / for division, ** for power, % for modulo
    Enter your operation symbol: ''')

    num1 = int(input("Enter the first Number: "))
    num2 = int(input("Enter the second Number: "))

    if operation == '+':
        if num1 == 56 and num2 == 9:
            print(num1, "+", num2, " = 77")
        elif num1 == 9 and num2 == 56:
            print(num1, "+", num2, " = 77")
        else:
            print(num1, " + ", num2, " = ", num1+num2)
    elif operation == '-':
        print(num1, " - ", num2, " = ", num1-num2)
    elif operation == '*':
        if num1 == 45 and num2 == 3:
            print(num1, "*", num2, " = 555")
        elif num1 == 3 and num2 == 45:
            print(num1, "*",  num2, " = 555")
        else:
            print(num1, " * ", num2, " = ", num1*num2)
    elif operation == '/':
        if num1 == 56 and num2 == 6:
            print(num1, "/", num2, " = 4")
        else:
            print(num1, " / ", num2, " = ", num1/num2)
    elif operation == '**':
        print(num1, " ** ", num2, " = ", num1**num2)
    elif operation == '%':
        print(num1, " % ", num2, " = ", num1%num2)
    else:
        print("Error! Enter a valid operation symbol.")
    again()


def again():
    cal_again = input('''
    Do you want to calculate again?
    Please type y for YES or n for NO.
    ''')

    if cal_again == 'y':
        calculator()
    elif cal_again == 'n':
        print("See You Later.")
    else:
        again()


calculator()
