import random as r
cmp_win = 0
user_win = 0
choice = "y"
for i in range(0, 5):
    _list = ["Snake", "Water", "Gun"]
    pc = r.choice(_list)

    user = int(input("Enter 1.Snake 2.Water 3.Gun :\n"))

    if (user == 1 and pc == "Water") or (user == 2 and pc == "Gun") or (user == 3 and pc == "Snake"):
        print("You Win!!")
        user_win += 1
    elif (user == 1 and pc == "Snake") or (user == 2 and pc == "Water") or (user == 3 and pc == "Gun"):
        print("Result is Draw ")
        cmp_win += 1
    else:
        print("Ops! You Loose ")

print(f"User wins {user_win} times and computer wins {cmp_win} times out of 5 times")

if user_win == cmp_win :
    print("Res is Draw")
elif user_win > cmp_win :
    print("User Wins")
else :
    print("Computer Wins")