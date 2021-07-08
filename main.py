from Functions import say_hi
from TF import C

say_hi()

Con = input("Do you want to use confirmations: ")

if Con == "Yes":
    Con = True

elif Con == "No":
    Con = False

user = input("Whats your name: ")


def ask_say_hi_again():
    print("Hi " + user + "")


if user != "":
    Cn = True

elif user == "I don't want to answer":
    Cn = False

if Cn:
    ask_say_hi_again()

Q1 = input("Do you want to start calculator? : ")

if Q1 == "Yes":
    C = True

elif Q1 == "No":
    C = False

while C:

    num1 = float(input("Enter first number: "))

    if Con:

        Con1 = input("WARNING! Are you sure you want to use this number: ")

        if Con1 == "Yes":
            print("Go on next.")

        elif Con1 == "No":
            num1 = float(input("Enter first number: "))

    op1 = input("Enter operator: ")
    if Con:

        Con2 = input("WARNING! Are you sure you want to use this operator: ")

        if Con2 == "Yes":
            print("Go on next.")

        elif Con2 == "No":
            op1 = input("Enter operator: ")

    num2 = float(input("Enter second number: "))
    if Con:

        Con3 = input("WARNING! Are you sure you want to use this number: ")

        if Con3 == "Yes":
            print("Go on next.")

        elif Con3 == "No":
            num2 = float(input("Enter second number: "))

    op2 = input("Enter second operator: ")
    if Con:
        Con4 = input("WARNING! Are you sure you want to use this operator: ")

        if Con4 == "Yes":
            print("Go on next.")

        elif Con4 == "No":
            op2 = input("Enter second operator: ")

    num3 = float(input("Enter third number: "))
    if Con:
        Con5 = input("WARNING! Are you sure you want to use this number: ")

        if Con5 == "Yes":
            print("Go on next")

        elif Con5 == "No":
            num3 = float(input("Enter third number: "))

    op3 = input("Enter third operator: ")
    if Con:
        Con6 = input("WARNING! Are you sure you want to use this operator: ")

        if Con6 == "Yes":
            print("Go on next")

        elif Con6 == "No":
            op3 = input("Enter third operator: ")

    num4 = float(input("Enter fourth number: "))
    if Con:
        Con7 = input("WARNING! Are you sure you want to use this number: ")

        if Con7 == "Yes":
            print("Go on next")

        elif Con7 == "No":
            num4 = float(input("Enter fourth number: "))

    op4 = input("Enter fourth operator: ")
    if Con:
        Con8 = input("WARNING! Are you sure you want to use this operator: ")

        if Con8 == "Yes":
            print("Go on next")

        elif Con8 == "No":
            op4 = float(input("Enter fourth operator: "))

    num5 = float(input("Enter fifth number: "))
    if Con:
        Con9 = input("WARNING! Are you sure you want to use this number: ")

        if Con9 == "Yes":
            print("Go on next")

        elif Con9 == "No":
            num5 = float(input("Enter fifth number: "))

    if op1 == "+":
        result1 = (num1 + num2)

    elif op1 == "-":
        result1 = (num1 - num2)

    elif op1 == "*":
        result1 = (num1 * num2)

    elif op1 == "/":
        result1 = (num1 / num2)

    elif op1 == "E":
        q1 = input("Do you really exit? :  ")

    q1 = input("Do you want to exit? : ")

    if q1 == "Yes":
        C = False

    elif q1 == "No":
        C = True

    else:
        print("Invalid operator")

    if op2 == "+":
        result2 = (result1 + num3)

    elif op2 == "-":
        result2 = (result1 - num3)

    elif op2 == "*":
        result2 = (result1 * num3)

    elif op2 == "/":
        result2 = (result1 / num3)

    elif op1 == "E":
        q1 = input("Do you really exit? :  ")

    if q1 == "Yes":
        C = False

    elif q1 == "No":
        C = True

    else:
        "Invalid operator"

    if op3 == "+":
        result3 = (result2 + num4)

    elif op3 == "-":
        result3 = (result2 - num4)

    elif op3 == "*":
        result3 = (result2 * num4)

    elif op3 == "/":
        result3 = (result2 / num4)

    elif op3 == "E":
        q1 = input("Do you really exit? :  ")

    if q1 == "Yes":
        C = False

    elif q1 == "No":
        C = True

    else:
        "Invalid operator"

    if op4 == "+":
        f_result = result3 + num5

    elif op4 == "-":
        f_result = result3 - num5

    elif op4 == "*":
        f_result = result3 * num5

    elif op4 == "/":
        f_result = result3 / num5

    elif op4 == "E":
        q1 = input("Do you really exit? :  ")

    if q1 == "Yes":
        C = False

    elif q1 == "No":
        C = True

    else:
        "Invalid operator"


    class Result:
        pass


    def result():
        print(f_result)

    ask = input("Do you want to see the result: ")

    if ask == "Yes":
        result()

    elif ask == "No":
        print("")

