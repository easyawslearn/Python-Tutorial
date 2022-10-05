## RETURN THE NUMBER IF IT IS EVEN

# CHECK_EVEN FUNCTION DEFINE
def check_even(num):

# RETURN THE NUMBER IF THE CONDITION IS TRUE
    return num%2==0

# GIVING INPUTS TO THE NUMS 
nums = [1,2,3,4,5,6]

# HERE WE PRINT WITH THE FILTER AND IN LIST FORMAT
print(list(filter(check_even,nums)))   

# PRINT USING FOR LOOP
for i in filter(check_even,nums):
    print(i)

## SIMPLE OUTPUT
# HOW TO RUN
# PYTHON: example_lambda_filter.py
# [2, 4, 6]
  
## OUTPUT AFTER USING THE FOR LOOP  
# PYTHON: example_lambda_filter.py
# 2
# 4
# 6