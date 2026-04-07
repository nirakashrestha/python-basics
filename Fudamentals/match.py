#like switch statement in Java
from random import randint

num = randint(1,6)

match num:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case 5:
        print("five")
    case _:
        print("Value is Greater than 5")
