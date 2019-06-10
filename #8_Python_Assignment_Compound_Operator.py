# Assignment operators in Python
# Operator	Example	Equivatent to
# =	x = 5	x = 5
# +=	x += 5	x = x + 5
# -=	x -= 5	x = x - 5
# *=	x *= 5	x = x * 5
# /=	x /= 5	x = x / 5
# %=	x %= 5	x = x % 5
# //=	x //= 5	x = x // 5
# **=	x **= 5	x = x ** 5
# &=	x &= 5	x = x & 5
# |=	x |= 5	x = x | 5
# ^=	x ^= 5	x = x ^ 5
# >>=	x >>= 5	x = x >> 5
# <<=	x <<= 5	x = x << 5

a = 10
b = 20
c = 0

print ("a value is ",a)
print ("b value is ",b)
print ("c value is ",c)

c = a + b
print ("Line 1 - Value of c is (c=a+b) ", c)

c += a
print ("Line 2 - Value of c is (c +=a)", c)

c *= a
print ("Line 3 - Value of c is (c *=a)", c)

c /= a
print ("Line 4 - Value of c is (c /=a)", c)

c  = 2
c %= a
print ("Line 5 - Value of c is (c %=a)", c)

c **= a
print ("Line 6 - Value of c is (c **= a)    ", c)

c //= a
print ("Line 7 - Value of c is (c //=a)", c)
