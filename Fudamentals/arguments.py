
def sum(num1, *num2): #variable length arguments
    sum = num1
    for n in num2:
        sum+=n

    return sum

total = sum(1,2,3,4,5)
print(total)

def person(name, age=18):
    print("name: ", name)
    print("age:, ", age)

person("Nirakash", 42)
print("passing arguments in wrong position..still works...but wrong..")
person(30, "John")


#so we can solve this using Keyword argument
person(age=30, name="John")

#Keyword Variable Length Argument -note ** in argument - it returns dictionary
def person1(name, **kwargs):
    print("name: ", name)
    for k, v in kwargs.items():
        print(k, " : ", v)

person1(name="Anisha", age=36, work="shadygrove", profession="nurse")