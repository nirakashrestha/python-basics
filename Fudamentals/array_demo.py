from array import array

arr1 = array("i",[65,32,27,15,98,12,59])


print(arr1.tolist())

#array functions

#append
arr1.append(23)

for n in arr1:
    print(n,end=" ")

print()

#reverse
arr1.reverse()

#print array values 1 by 1
for n in arr1:
    print(n,end=" ")

#copy array into a different array
arr2 = arr1 #this actually doesn't copy. proof - in line#26 I changed a value in arr1 but changes in arr2 also
arr1[1] = 69
print("\nafter copying to arr2..")
print(arr1)
print(arr2)

#actually copying
arr3 = array("i",[75,32,27,15,98,12,59])
#arr4 = array("i", arr3.tolist()) #can be re-written following way - more memory efficient
arr4 = array(arr3.typecode, (n for n in arr3))
arr3[1] = 42

print("\nafter copying to arr4..")
print(arr3)
print(arr4)







