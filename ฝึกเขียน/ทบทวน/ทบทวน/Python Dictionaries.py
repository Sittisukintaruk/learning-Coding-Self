# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# print(thisdict['model'])
# x = thisdict.get("model")
# print(x)

# thisdict["year"] = 2018
# print(thisdict)

# for x in thisdict:
#   print(x)

# for x , d in enumerate(thisdict):
#   print(x , d)

# for x in thisdict:
#   print(x , thisdict[x])

# for x in thisdict.values():
#   print(x)
thisdict = dict(brand="Ford", model="Mustang", year=1964)

for key, value in thisdict.items():
  print(key, value)


if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

print(len(thisdict))


thisdict["color"] = "red"
for key, value in thisdict.items():
  print(key, value)

# thisdict.pop("model")
# print(thisdict)

thisdict.popitem() #method removes the last inserted item 
print(thisdict)

# del thisdict["model"]
# print(print(thisdict) #this will cause an error because "thisdict" no longer exists.
# del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.

# thisdict.clear()
# print(thisdict)

mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict)

# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
