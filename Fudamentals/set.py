#set is collection of unordered unique elements
import typing

set1 = {34,57,89,57,98}
print(set1)
print(89 in set1) #True
print(67 in set1) #False

print(len(set1)) #4 - counts only unique values
print(type(set1))

set2={}
print(type(set2)) #<class 'dict'>

set3 = set()
print(type(set3)) #<class 'set'>

set4 = set('ailapolkamopty')
set5 = set('bavbopgh')
print(set4)
print(set5)

#set operations
print(set4 - set5) #includes only charcters in set4 only but not in set5
print(set4 | set5) #performs union of set4 and set5
print(set4 & set5) #includes only characters common in set4 and set5
print(set4 ^ set5) #includes only characters that are not common in set4 and set5



