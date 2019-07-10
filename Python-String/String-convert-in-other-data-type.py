#Python String Demostration

#How to club with other character
example = "test"
print ('w' + example[1:])

#Converting String to list
list_example=list(example)
print ("String Data Type value is :",example)
print ("List data type:",list_example)

#Converting String to set
set_example=set(example)
print ("String Data Type value is :",example)
print ("Set data type:",set_example)

#Converting String to boolean
boolean_example=bool(example)
print ("String Data Type value is:",example)
print ("Boolean data type:",boolean_example)

example =''
#Converting String to boolean with blank value
boolean_example=bool(example)
print ("String Data Type value is:",example)
print ("Boolean data type:",boolean_example)
