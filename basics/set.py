# note :- we cant add duplicate values

s= set ([1,4,5])
print(type(s))
s1 = set()
s1.add(5)
s1.add(8)
print(s,s1)
print(s1.union(s))
print(s1.intersection(s))
print(s1.isdisjoint(s))
print(s.difference(s1))
print(s1.difference(s))
print(s.__and__(s1))


