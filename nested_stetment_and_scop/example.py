x=25 #globel 
def p():
     x=50    # local
     print(x)

print(x)

p()


x = 100 #global

def p():
    global x 
    x=50 # local
    return x
   

print(x)

p()

x=50
def fun():
    global x
    print(f"x is {x}")

    #Local Reassigment!
    x=200
    print(f"just localy change x to {x}")

fun()

x=50
def fun():
    print(f"x is {x}")

    #Local Reassigment!
    x=200
    print(f"just localy change x to {x}")

fun()

name = "this is "

def new():
    #ENclossing
    name="summy"
    print(name)

    def new1():
        name="gimmy"
        print(name)



