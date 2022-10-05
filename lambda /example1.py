## FIND THE SQUARE OF A NUMBER USING LEMBDA FUNCTION

square= lambda num: num**2
print(square(8))

## REVERSE A STRING USING LAMBDA FUNCTION 

str = 'hello guys'
# lambda returns a function object
rev_upper = lambda string: string.upper()[::-1]
print(rev_upper(str))

## MAP OUT THE EVEN NUMBER FROM THE LIST USING LEMBDA FUNCTION

mynums=[1,2,3,4,5]
print(list(map(lambda num: num%2==0,mynums)))

## FILTER OUT THE EVEN NUMBER FROM THE LIST USING LEMBDA FUNCTION
mynums=[1,2,3,4,5]
print(list(filter(lambda num: num%2==0,mynums)))

# FIND MAXIMUM NUMBER BETWEEN TWO NUMBERS USING LEMBDA FUNCTION
Max = lambda a, b : a if(a > b) else b
print(Max(8, 4))

