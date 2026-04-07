data = [42, 'Nirakash', 5.10, 'SBA', 'NorthPotomac']

for value in data:
    print(value)

for value in range(10):
    print(value)


#Break and Continue
print("continue")
for value in range(25):
    if value % 10 == 0:
        continue
    print(value)

print("Break")
for value in range(5):
    if value == 3:
        break
    print(value)