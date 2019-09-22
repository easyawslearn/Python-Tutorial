###########    Spliting Example    ################
example='abcd#efg#hijk#lamno$1$2$3$4'

split_example=example.split()
print(split_example)
#Output would be
#String Spliting Example
#['abcd#efg#hijk#lamno$1$2$3$4']

split_example=example.split('#')
print ("String Spliting Example")
print(split_example)
#Output would be
#String Spliting Example
#['abcd', 'efg', 'hijk', 'lamno$1$2$3$4']


###########    Joining Example    ################

example=['ABC','DEF','GHI','JKL']
join_example=''.join(example)
print ("String Join Example")
print(join_example)
#Output would be
#String Join Example
#ABCDEFGHIJKL

join_example=' * * '.join(example)
print ("String Join Example")
print(join_example)
#output would be
#String Join Example
#ABC * * DEF * * GHI * * JKL
