a=10 #global variable

print("Before Update: ", a)

def update():
    a = 15 #local variable
    globals()['a'] = 20 #update global variable
    print("Inside: ", a)

update()

print("Outside: ",a)