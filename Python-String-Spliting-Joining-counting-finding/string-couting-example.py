###########    String Coutning Example    ################

example="A#B#C#D"
count_example=example.count('#')

print ("Number of # in example string is",count_example)
#Output would be
#('Number of # in example string is', 3)


count_example=example.count('#',0,4)

print ("Number of # in example string is",count_example)
#Output would be
#('Number of # in example string is', 2)
