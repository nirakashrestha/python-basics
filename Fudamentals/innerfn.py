def outer():
    print('in outer function')

    def inner(num):
        print('in inner function ', num)

    return inner



a = outer()
a(23)