#Python | random.sample() function

import random

print ("The random value from random.seed(10) is : ", end="")
print (random.seed(10))
#If we wanted a random integer, we can use the randint function
#Randint accepts two parameters: a lowest and a highest number.
#Generate integers between 1,5. The first value should be less than the second.
print ("The random integer value from 10 to 100 is : ", end="")
print (random.randint(10,100))

#If you want a larger number, you can multiply it.
#For example, a random number between 0 and 100:
print ("The random value of random function is : ", end="")
print (random.random()*20)

# Python code to demonstrate the working of
# randrange()
print ("The random range of 1000 is : ", end="")
print (random.randrange(1000))

print ("The random range of 10 to 100 by skipping 2 is : ", end="")
print (random.randrange(10,100,2))

a=[1,2,9,'c','e',1.1]
print ("list a value is ",a)
print ("The list a value after random.shuffle function is : ", end="")
random.shuffle(a)
print (a)
