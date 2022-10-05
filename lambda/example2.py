# Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

# square of number
squ = lambda num: num**2
print(squ(5))

# Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# reverse a string with the help of list, map, lamda
fun=["pthon","is","fun"]
ans=(list(map(lambda x:x[::-1],fun))) 
print(ans)

# first latter of word of list
name=["python","with","s3cloudehub"]
(print(list(map(lambda n:n[0],name))))

# print even number
mynum=[1,2,3,4,5,6]
print(list(filter(lambda num:num%2==0,mynum)))
