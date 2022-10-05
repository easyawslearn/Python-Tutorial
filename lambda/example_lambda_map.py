## RETURN THE 'EVEN' IF STRING IS EVEN OTHERWISE RETURN FIRST LETTER OF A STRING

# SLICER FUNCTION DEFINE
def slicer(mystring):
# FIND THE LENGTH OF MYSTRING VARIABLE    
    if len(mystring)%2 == 0:
# IF THE LENGTH OF MYSTRING IS EVEN IT RETURNS EVEN       
        return 'even'
    else:
# OTHERWISE RETURNS THE FIRST LETTER OF THE STRING        
        return mystring[0]        
names = ['adam','eve','sla','rock','rio']
# HERE WE PRINT WITH THE MAP AND IN LIST FORMAT
print(list(map(slicer,names)))

## HOW TO RUN 

# python: example_lambda_map.py
# ['even', 'e', 's', 'even', 'r']
