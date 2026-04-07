#tuple is immutable
tup0 = 16,25 #declare tuple - method1
print(type(tup0))

tup1= (34,78)
print(type(tup1)) # declare tuple - method2

print(len(tup1))
print(sum(tup1))
print(max(tup1))

tupA = (5, 'nirakash', 19.1)

#unpacking tuple
num1, name, num2 = tupA
print(num1)
print(name)
print(num2)

#list insde tuple - we can change the value in list though tuple is immutable
tupB = [6,[89,78,31]]
tupB[1][2] = 91
print(tupB)

family_tuple = ("nirakash", "anisha", "nolan", "aaron")
print('nirakash' in family_tuple)
print('Nirakash' in family_tuple)


tupC = (45)
print(type(tupC)) #<class 'int'>

tupD = (45,)
print(type(tupD)) #<class 'tuple'>