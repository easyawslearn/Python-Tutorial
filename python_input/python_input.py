user = input("enter a any key : >>>") #input from user

if (type(user)) == int:   # chack type 
    print("it is a number")
else:
    print("it is not a number")

# ///////output/////////
 # enter a any key : >>>q
 # it is not a number


user = input("enter a number:>>>>")   #input from user
try:
    val = int(user) # pass if number
except ValueError:
    print("that is not a number") # if not message print 

#  ///////output/////////
# enter a number:>>>>q
# that is not a input


user = input("enter a number:>>") #input from user
if user.isdigit():
    print("it is a digit")
else:
    print("it is not a digit:")

# ///////output/////////
# enter a number:>>1
# it is a digit

# enter a number:>>a
# it is not a digit:


def user():
    choice ="worng"
    while choice.isdigit() == False:
        choice = input("plese enter a number:")
    return int(choice)
user()

# output 1
#  plese enter a number:12

# output 2
# enter a number:>>q
# it is not a digit:


def user():
    choice = "worng"
    acceptable_rang = range(0,10)
    with_rang = False

    while choice.isdigit() == False or with_rang==False:
        choice = input("enter a number (0,10):")

        if choice.isdigit() == False:
            print("sorry this is not a digit")

        if choice.isdigit() == True:
            if int(choice) in acceptable_rang:
                with_rang = True
            else:
                with_rang = False
        
    return int(choice)