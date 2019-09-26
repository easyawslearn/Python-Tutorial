# Python code to demonstrate printing
# escape characters from repr()

# initializing target string
example = "I\nLove\tworld"

print ("The string without repr() is : ")
print (example)

print ("\r")

print ("The string after using repr() is : ")
print (repr(example))


# Python code to demonstrate printing
# escape characters from "r" or "R"

# initializing target string
ch = "I\nLove\tWorld"

print ("The string without r / R is : ")
print (ch)

#print ("\r")

# using "r" to prevent resolution
ch1 = r"I\nLove\tWorld"

print ("The string after using r is : ")
print (ch1)

#print ("\r")

# using "R" to prevent resolution
ch2 = R"I\nLove\tWorld"

print ("The string after using R is : ")
print (ch2)
