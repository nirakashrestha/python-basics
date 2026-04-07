fruits = {1:'apple', 2:'banana', 3:'orange', 4:'mango',5:'watermelon',3:'kiwi'}
print(type(fruits))
print(fruits)
print(fruits[2])
#print(fruits[0]) #keyerror
print(fruits.get(0)) #None
print(fruits.get(0,'not a fruit')) #not a fruit
print(fruits.get(1))

#keys are set and values are set
print(fruits)

keys = {1,2,3}
values= ['a','b','c']
dict1 = dict(zip(keys,values))
print(dict1)

#dictionary operations
fruits.pop(1)
print(fruits)

del fruits[3]
print(fruits)

#dictionary inside dictionary
IDE =\
    {'js': 'vscode',
     'python': ['vscode', 'pycharm'],
     'java':{'corejava':'vscode', 'spring': 'Intellij'}
     }

print(IDE['js'])
print(IDE['python'][1])
print(IDE['java']['spring'])