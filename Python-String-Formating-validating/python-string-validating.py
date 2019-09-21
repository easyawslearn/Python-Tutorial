#######################################
####### Pyhton String validating Example
#######################################

example="python"


print("String validating for lowercase")
print(example.islower())
# String validating for lowercase
# True

example="python"
print("String validating for Upper case")
print(example.isupper())
# String validating for Upper case
# False

example="Python Example"
print("String validating for Title case")
print(example.istitle())
# String validating for Title case
# True

example=" "
print("String validating for is having only space")
print(example.isspace())
# String validating for is having only space
# True

example="123asd"
print("String validating for is having alphanumeric")
print(example.isalnum())
# String validating for is having alphanumeric
# True

example="123asd"
print("String validating for is having alphabets")
print(example.isalpha())
# String validating for is having alphabets
# False

example="123"
print("String validating for is having onlyu digits")
print(example.isdigit())
# String validating for is having onlyu digits
# True
