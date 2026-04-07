#list1
nums = [45,89,34,78,98,95]

print(nums[-1])
print(nums[2:4])

#list2
names = ['ram','hari','shiva','bishnu', 'krishna']

#mixing 2 lists
god_nums = [nums, names]

print(god_nums) #[[45, 89, 34, 78, 98], ['ram', 'hari', 'shiva', 'bishnu', 'krishna']]
print(god_nums[0]) #[45, 89, 34, 78, 98]
print(god_nums[1]) #['ram', 'hari', 'shiva', 'bishnu', 'krishna']
print(god_nums[0][1]) #89
print(god_nums[1][1]) #hari

#combine values in 2 arrays
num_gods = nums + names

print(num_gods) #[45, 89, 34, 78, 98, 'ram', 'hari', 'shiva', 'bishnu', 'krishna']

#list operations
nums.append(80)
print(nums)
nums.insert(1,95)
print(nums)
print(nums.count(95))
nums.remove(89)
print(nums)
nums.pop(2)
print(nums)
nums.pop()
print(nums)

del nums[2:4]
print(nums)

nums.extend([96,97,98,99])
print(nums)

#replace value in the list
nums[2:4] = [85,86]
print(nums)
nums.reverse()
print(nums)
nums.sort()
print(nums)

#use python inbuilt functions against list
print(min(nums))
print(max(nums))
print(sum(nums))
