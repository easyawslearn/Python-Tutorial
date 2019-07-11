#Python String Replacing Demostration

# Python3 program to demonstrate the
# use of replace() method

example = "Hello World"
# Prints the string by replacing geeks by Geeks
print(example.replace("World", "India"))

example = "Hello World World World"
# Prints the string by replacing only 3 occurence of Geeks
print(example.replace("World", "India", 2))

#concatenation with spliting and string
example = "Spammy"
example= example [:2]+'ic'+example[5:]
print(example)

example = "Hello"
example= example.replace('e','P')
print(example)

#How to get the supported function of string
print(dir(example))
