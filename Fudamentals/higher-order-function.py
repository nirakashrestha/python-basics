#higher order function means pass function inside function

def square(num):
    return num * num

def cube(num):
    return num * num * num



def operateOnList(lst, operation):
    for n in lst:
        result = operation(n)
        print(result)

mylist = [5,6,7]

print("performing square operation for each number in mylist...")
operateOnList(mylist,square)

print("performing cube operation for each number in mylist...")
operateOnList(mylist,cube)