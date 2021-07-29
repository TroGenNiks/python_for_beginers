# make a guessing numbers game
# store random number in variable and guess with limited chance



import random

a = (random.randint(1,100))
b = random.randint(1,5)
c = random.randint(1,5)
# print(a,b,c) # here u  got random numbers

print("your number is between",a-b," to ",a+c)
chance = 5
for i in range(0 ,chance):
    b = int(input("enter the number : "))

    chance = chance-1
    if b ==a:
        print("You won !")
        break
    if b >a:
        print("try for lessor ")

    if b <a:
        print("try for gretor ")

    if (chance==0):
        print("the number is ",a)
        break

print("game over ")