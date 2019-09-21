#######################################
####### Pyhton String Formating Example
#######################################

example="hello"

print ("center 5 function example")
string=example.center(5)
print(string)
#output is
#center 5 function example
#hello

print ("center 7 function example")
print(example.center(7))
#output is
# center 7 function example
#  hello


print ("center 9 function example")
print(example.center(9))
#output is
# center 9 function example
#   hello


print ("center 9 with * function example")
print(example.center(9,'*'))
#output is
# center 9 with * function example
# **hello**

print ("left justification example output is")
print(example.ljust(7))
# ljustification example output is
# hello

print ("left justification with * example output is")
print(example.ljust(7,'*'))
# ljustification with * example output is
# hello**

print ("right justification example output is")
print(example.rjust(7))
# right justification example output is
#   hello

print ("right justification with * example output is")
print(example.rjust(7,'*'))
# right justification with * example output is
# **hello


print ("Zfilling 5 example output is")
print(example.zfill(5))
# Zfilling 5 example output is
# hello

print ("Zfilling 7 example output is")
print(example.zfill(7))
# Zfilling 7 example output is
# 00hello

print ("Zfilling 9 example output is")
print(example.zfill(9))
# Zfilling 9 example output is
# 0000hello
