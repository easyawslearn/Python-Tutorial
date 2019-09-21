##############################################
####### Python exampleing Start with and End with
###############################################
# Python exampleing method startswith()
# checks whether exampleing starts with example,
# optionally reexampleicting the matching
# with the given indices start and end.


# Syntex example.startswith(example, beg=0,end=len(exampleing));

example = "python";
print ("example start with p")
print example.startswith( 'p' )
# output is
# example start with p
# True

print ("example start with P")
print example.startswith( 'P' )
# output is
# example start with P
# False

print ("example start with Y")
print example.startswith( 'y' )
# output is
# example start with Y
# False

print ("example start with y at index 1")
print example.startswith( 'y', 1 )
# output is
# example start with y at index 1
# True

print ("example start with y at index 1 till 4 length of string")
print example.startswith( 'y', 1, 4 )
# output is
# example start with y at index 1 till 4 length of string
# True
