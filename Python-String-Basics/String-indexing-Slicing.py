#Demostration of Pythong String Indexing

example= "Python Scripting"

"""
P   Y   T   H   O   N       S   C   R   I   P   T   I   N   G
0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15 (Sequecebe )
-16-15 -14 -13 -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1 ()
 """

print("Initial String: ")
print(example)

# Printing First character
print("\nFirst character of String is: ")
print(example[0])
#output would be P

print ("\n7th Character of String is:\n",example[7])
#this will print only S

# Printing Last character
print("\nLast character of String is: ")
print(example[-1])
#output would be G

# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(example[3:12])
#output would be "hon Script"

# Printing characters between
# 3rd and 2nd last character
print("\nSlicing characters between " + "3rd and 2nd last character: ")
print(example[3:-2])
#hon Script

#printing character from 1 to end
print ("\nCharacter from 1 to :")
print (example[1:])

#printing character from 1 to 6
print ("\nCharacter from 1 to 6")
print (example[1:6])

#printing character from 1 to 12
print ("\nCharacter from 1 to 12")
print (example[1:12])

#printing character from 1 to 12 with increment by 2
print ("\nCharacter from 1 to 12 with increment by 2")
print (example[1:12:2])


#printing character from 1 to 12 with increment by 2
print ("\nCharacter from -3 to -1 with increment by 2")
print (example[-9:-1:-1])

#printing character from -3 -15 in reverse order
print ("\nCharacter from -3 -15 in reverse order")
print (example[-3::-1])
