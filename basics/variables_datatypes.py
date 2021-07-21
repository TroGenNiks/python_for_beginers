# variables , datatype and type casting
var1 = "hello nisarg"
var2 = 40
var3 = 12.5
var4 =  'welcome in class ,'
# printing datatype of above variables using type function
print (type(var1))
print (type(var2))
print (type(var3))
print (type(var4))
# adding variables
print(var4+var1)  # we can add int flot, string string
print(var3+var2)

# typecasting
print(str(var3)+str(var2))
a = "20"
b= "30"
print(a+b) # concatenate 20 and 30
print(int(a) + int(b)) # adding 30 + 20

print(10 * a) # multiple tme printings
# user input
print("enter your number")
a = input()
print(a)


# calculator for simple addition
print("enter first number")
a = int(input())
print("enter second number")
b = int(input())
print(a+b)