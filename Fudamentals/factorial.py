def fact(num):
    res = 1
    for i in range(1, num+1):
        res *= i
    return res

result = fact(9)
print(result)


#factorial recursion

def fact_recursive(num):
    if num == 1:
        return 1
    return num * fact_recursive(num-1)

result = fact_recursive(9)
print(result)