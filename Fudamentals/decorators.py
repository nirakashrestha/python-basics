

def log_deco(func):
    def wrap(*args, **kwargs):
        print("values", args)
        result = func(*args)
        print("Result ", result)
        return result
    return wrap

def greater_first(func):
    def wrap(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return wrap

@log_deco
@greater_first
def divide(a,b):
    print("Dividing..")
    return a/b

@log_deco
@greater_first
def subtract(a,b):
    print("Subtracting..")
    return a-b

@log_deco
def add(*nums):
    print("Adding..")
    sum = 0
    for n in nums:
        sum += n
    return sum

# subtract = greater_first(subtract)
# divide = greater_first(divide)

divide(2,4)
subtract(5,8)
add(7,9, 11, 3)