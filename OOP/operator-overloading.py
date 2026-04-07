a = '5'
b = '6'
#c = a + b
c = str.__add__(a, b)
d = a.__add__(b)
print(c)
print(d)

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self): #over-riding the str function in object class
        return f'{self.name} : {self.balance}'

    def __add__(self, other):
        return Account("combined balance", self.balance + other.balance)

    def __gt__(self, other):
        return self.balance > other.balance

user1 = Account('Nirakash', 3000)
user2 = Account('Anisha', 2000)

combined = user1 + user2

print(user1)
print(user2)
print(combined)

if user1 > user2:
    print("nirakash pays the bill")
else:
    print("anisha pays the bill")

