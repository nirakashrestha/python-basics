

try:
    a = 5
    b = int ('t')
    #b = 0
    c = a/b
    print(c)
except ZeroDivisionError as e1:
    print("Error: ", e1)
except ValueError as e2:
    print("Error: ", e2)
except Exception as e:
    print("Error: ", e)
finally:
    print("finally execution")

print("End of execution")