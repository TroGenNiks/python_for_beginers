  # here we learn dictionary
# {} = dictionary

d1 = {"1":"nisarg", "2": "niks", "3":{"a":"deepa","b":"zaid", "c":"netri"}}
# datatype
print(type(d1))

print(d1["1"]) # printing values by using key
print(d1["3"]) # printing dictionary in dictionary by using key
d1["5"]="vinay" # adding another element in dictionary
print(d1)
del d1["2"] # deleting element with key
print(d1)
d2 = d1.copy() # making copy
print(d2)
del d2["3"]
print(d1)
print(d2)
d2.update({"leena":"toofy"}) # updating dictionary
print(d2)
print(d2.items()) # all items -> key : values
print(d2.values()) # values only
