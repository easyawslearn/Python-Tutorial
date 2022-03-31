a, b = 0, 1
count = 0
input_count=10

print("Fibonacci sequence:")
while count < input_count:
  print(a)
  new = a + b
  a = b
  b = new
  count += 1
