thistuple = ("apple", "banana", "cherry")
print(thistuple)

print(thistuple[1])

print(thistuple[-1])

print(thistuple[2:5])


print(thistuple[-4:-1])
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# thistuple[3] = "orange" # This will raise an error
# print(thistuple)
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)