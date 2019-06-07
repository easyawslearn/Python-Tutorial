# Python code to demonstrate Type conversion
# int(a,base) : This function converts any data type to integer. ‘Base’ specifies the base in which string is if data type is string.
# float() : This function is used to convert any data type to a floating point number
# complex(): This function is used to convert any data type to complex data type
# bool(): This function is used to identify the value is 0 or not it return True or False

a=1
b="101010"

print ("Convert Value in integer data type",int(b,2),)

print ("Convert value in float data type",float(a),)

print ("convert value in complex data type",complex(a),)

print ("validiate value as boolen datatype",bool(a),)

# using ord(), hex(), oct()
# initializing integer
example = '4'

# printing character converting to integer
output = ord(example)
print ("After converting character to integer : ",end="")
print (output)

# printing integer converting to hexadecimal string
output = hex(50)
print ("After converting 56 to hexadecimal string : ",end="")
print (output)

# printing integer converting to octal string
output = oct(60)
print ("After converting 56 to octal string : ",end="")
print (output)

example=0
output = (bool(example))
print ("validating example value is 0 or not using bool function: ", end="")
print (output)

example=1
output = (bool(example))
print ("validating example value is 0 or not using bool function: ", end="")
print (output)

example=-1
output = (bool(example))
print ("validating example value is 0 or not using bool function: ", end="")
print (output)
