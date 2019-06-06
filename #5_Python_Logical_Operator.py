# Operator	Description	Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10
# or	Returns True if one of the statements is true	x < 5 or x < 4
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

a=0
print ("If variable value is equal to 0 then True else False:::::::::",not(a),)
#Output Would be
#True

a=1
print ("If variable value is equal to 0 then True else False:::::::::",not(a),)
#Output Would be
#False

a=0;b=1
print ("One of Both Condition are satisfied then True else False:::::::::",(a>b) or (b>a),)
#Output Would be
#True

a=0;b=1
print ("Both Condition are satisfied then True else False:::::::::", (a>b) and (b>a),)
#Output Would be
#False


a=0;b=1
print ("Value are equal ?:::::::::", (a == b),)
#Output Would be
#False

a=0;b=0
print ("a is b are equal ?:::::::::", (a is b),)
#Output Would be
#True

a=0;b=0
print ("a is not equal to b  ?:::::::::", (a is not b),)
#Output Would be
#False

a=0;b=1
print ("a is not equal to b  ?:::::::::", (a is not b),)
#Output Would be
#True
