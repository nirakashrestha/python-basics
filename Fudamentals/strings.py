#use \ to cancel meaning of special chars
print('Nirakash\'s \'Business\'')
print('c:\\users\\nirakash')

#concat
print('nirakash' ' shrestha')
fname = 'nirakash'
#print (fname ' shrestha') -> error
print(fname + ' shrestha')

#substring
text = 'Everest'
print(text[5]) #s
print(text[-1]) #t
print(text[-7]) #E
#print(text[-8]) #out of range
print(text[1:4]) #ver (4th pos is excluded)
print(text[2:]) #erest (starting index 2 and all the way to the end)
print(text[2:-2]) #ere(starting index 2 and exclude char at -2)
print(text[::-1]) #tserevE (reverses the sting)
