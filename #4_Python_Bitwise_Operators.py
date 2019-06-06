#Python Bitwise Operators Example
a=50,b=13
#Operator	Description	Example
#&        Binary AND	Operator copies a bit to the result if it exists in both operands	(a & b) (means 0000 0000)
#|        Binary OR	It copies a bit if it exists in either operand.	(a | b) = 63 (means 0011 1111)
#^        Binary XOR	It copies the bit if it is set in one operand but not both.	(a ^ b) = 63 (means 0011 1111)
#~        Binary Ones Complement	It is unary and has the effect of 'flipping' bits.	(~a ) = -51 (means 0011 0011 in 2's complement form due to a signed binary number.
#<<       Binary Left Shift	The left operands value is moved left by the number of bits specified by the right operand.	a << 2 = 200 (means 1100 1000)
#>>       Binary Right Shift	The left operands value is moved right by the number of bits specified by the right operand.	a >> 2 = 12 (means 0000 1100)

a = 50            # 50 = 0011 0010
b = 13            # 13 = 0000 1101
output = 0

output = a & b;        # 0 = 0000 0000
print ("Operator & Output Value is ", output)

output = a | b;        # 63 = 0011 1111
print ("Operator | Output Value is ", output)

output = a ^ b;        # 63 = 0011 1111
print ("Operator ^ Output Value is ", output)

output = ~a;           # -51 = 0011 0011
print ("Operator ~ Output Value is ", output)

output = a << 2;       # 200 = 1100 1000
print ("Operator << Output Value is ", output)

output = a >> 2;       # 12 = 0000 1100
print ( "Operator >> Output Value is ", output)
