from itertools import cycle
from time import sleep

lights = [
    ('Green', 10),
    ('Yellow', 3),
    ('Red', 5)

]

colors = cycle(lights)

while True:
    c,s = next(colors)
    print(c)
    sleep(s)