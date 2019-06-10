# A set is an unordered collection of Unique elements.
seta=set('abcd')
print (seta)

l = ['apple','banana','orange','graps']
print ("object type is", type(l),)
b=set(l) # converted List into set objects
print ("Object Type is ", type(b),)

s = {'apple','banana','orange','graps'}
print ("object type is", type(s),)
c=set(s) # converted List into set objects
print ("Object Type is ", type(c),)


example=set('abcdefg')
print ("define variable",example)

example.add('z')
print ("define variable",example)

d=example.copy()
print("copy set example",d)

example.remove('a')
print("removed a element from example set",example)

list1 = [1, 2, 3]
list2 = [5, 6, 7]
set1 = set(list2)
set2 = set(list1)

# Update method
set1.update(set2)

# Print the updated set
print("set update example",set1)

example.discard ('c')
print ("discard c example",example)

example.clear()
print ("clear example",example)
