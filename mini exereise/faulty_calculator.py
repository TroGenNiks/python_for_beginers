# exercise of code with harry
# here we have to make a calculator which shows wrong answer of some operations
# operations are 3+4=11 .... 5*7=2    6-3 = 40 ..... 8/2=100


operation = int(input("type \n1:addition\n2:subtraction\n3:multiplication\n4: division\n: "))
first = int(input("first number : "))
second = int(input("second number : "))

if operation == 1:
    if first ==3 and second==4:
        print("11")
    else:
        print(first+second)
elif operation == 2:
    if first ==6 and second==3:
        print("40")
    else:
        print(first-second)
elif operation == 3:
    if first ==5 and second==7:
        print("2")
    else:
        print(first*second)
elif operation == 4:
    if first ==8 and second==2:
        print("100")
    else:
        print(first/second)
