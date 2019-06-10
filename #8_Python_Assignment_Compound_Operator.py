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
print (" Value of c is (c=a+b) ", c)

c += a
print (" Value of c is (c +=a)", c)

c *= a
print (" Value of c is (c *=a)", c)

c /= a
print (" Value of c is (c /=a)", c)

c  = 2
c %= a
print (" Value of c is (c %=a)", c)

c **= a
print (" Value of c is (c **= a)    ", c)

c //= a
print (" Value of c is (c //=a)", c)
