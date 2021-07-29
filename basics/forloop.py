# list = [1,2,3,4,5,6]
# for i in range(0 , len(list)):
#     print(list[i])
#
# list1 =["niks","nisarg","srushti","SHeetal"]
# for i in list1:
#     print(i)
#
# list2 =[["niks",1],["nisarg",2],["srushti",3],["SHeetal",4]]
# dicr = dict(list2)
# print(dicr)
# for i,j in dicr.items():  # whe  we have to retrive key and item both
#     print(i,j)
# for i in dicr:   # ONLY FOR key
#     print(i)
#
# # makl a list , check for number and print only >6
#
# list4 = [1,88,9,"trogan",6,"srushti",5,4]
# for i in list4:
#     if str(i).isnumeric() and i>6 :
#         print(i)
#
# while loop
# i = 1
# while i < 6:
#   print(i)
#   i += 1
#
# while (True):
#       inp = int(input("Enter a Number\n"))
#       if inp > 100:
#           print("Congrats you have entered a number greater than 100\n")
#           break
#       else:
#           print("Try again!\n")
#           continue
#
#
#
#   # breaking conditions in for  loop
#
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break


# print number greter than 5 less than 15

i = 0
while(True):
    if (i+1 <5):
        i = i +1
        continue
    print(i+1, end=" ")
    if(i==15):
       break
    i = i + 1