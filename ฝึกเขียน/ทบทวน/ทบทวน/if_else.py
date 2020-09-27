
a = 200
b = 33
c = 500

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


if a > b: print("a is greater than b")

print("A") if a > b else print("B")


print("A") if a > b else print("=") if a == b else print("B")

if a > b and c > a:
  print("Both conditions are True")


x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


a = 33
b = 200
if b > a:
  pass