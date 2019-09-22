###########    String find Example    ################

example="A#B#C#D$1$2$3"
find_example=example.find('1')

print ("value 1 location in string is",find_example)
#Output would be
#('value 1 location in string is', 8)

print ("value from string at 8 index is",example[8])
#Output would be
#('value from string at 8 index is', '1')

find_example=example.find('4')

print ("value 4 in string",find_example)
#Output would be
#('value 4 in string', -1)
