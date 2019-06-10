# The frozenset() is an inbuilt function is Python which takes an iterable object as input and makes them immutable.
# Simply it freezes the iterable objects and makes them unchangeable.

# Python program to understand frozenset() function

# set declaration
number = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print ("Object type of number is ",type(number))
# converting Sets to frozenset
fnumber = frozenset(number)
print ("object type of fnumber is ",type(fnumber))

# printing details
print("frozenset Object is : ", fnumber)

# Python program to understand use
# of frozenset function

# creating a dictionary
info = {"fname": "vijay", "age": 30, "sex": "Male",}

# making keys of dictionary as frozenset
key = frozenset(info)

# printing keys details
print('The frozen set is:', key)

# Python program to understand
# use of frozenset function

# below line will generate error
#TypeError: 'frozenset' object does not support item assignment
fnumber[1] = "11"
