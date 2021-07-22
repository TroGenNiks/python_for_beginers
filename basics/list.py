# here we learn list list functions , tuple ,tuple functions , converting
# [] =  list = mutable = can change
# () = tuple = nonmutable = can not change

list = ["niks" , "netri" , "zaid" , "deepa", "danny danzoga" , "mufasa" , 12, 45, 14.5 ]
list1 = [5,21,29,7,8,3,11]
print(list)
print(list1)
print(list[5:])
print(list[:6])
print(list[::3])
list.pop() # pop last element
print(list)
list.insert(2,"nisarg") # inserting element at index 2
print(list)
list.append(1913) # appending element at last
print(list)
print((list1)) # finding max in integer list , similarly  min
list1.sort()
print(list1)
list1.reverse()
print(list1)

# tuple
a = ( 4 ,8 , 3 , 3 )
print(a)
print(len(a))
print(a.count(3))


# swapping
c= 4
b= 5
print(c,b)
c,b = b,c
print(c,b)