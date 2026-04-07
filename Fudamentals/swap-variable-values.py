a=8
b=9

print("***Before Swapping***\n")
print("a: ",a)
print("b: ",b)

#conventional way
"""
temp = a
a=b
b=temp

"""
print("\n***After Swapping***\n")
#python way - behind the scene - Tuple Packing and Tuple Unpacking happens
a,b = b,a

print("a: ",a)
print("b: ",b)