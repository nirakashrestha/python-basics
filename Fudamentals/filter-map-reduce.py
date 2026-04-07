from functools import reduce

nums = [9,7,4,13,18,3,6,1,2]

"""
Problem Statement: In above list, find even numbers and put all even numbers in a list. Then, Double each number in
                    the list. Then, find the sum of all the doubled numbers.
"""

#Solution


evens = list(filter(lambda n : n % 2 == 0, nums))
doubles = list(map(lambda n : n * 2, evens))
sum = reduce(lambda x,y : x + y, doubles)


print(evens)
print(doubles)
print(sum)