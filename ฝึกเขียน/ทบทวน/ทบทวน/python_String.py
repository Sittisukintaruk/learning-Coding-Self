# txt = " hello World "
# x = txt.strip()
# print(x)

# txt = " hello World "
# x = txt.upper()
# print(x)

# b = "Hello, World!"
# print(b[-5:-2])

# a = "Hello, World!"
# print(len(a.strip()))

# a = "Hello, World!"
# print(a.replace("H", "J"))

# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']
# b = a.split(",")
# print(type(b))

# txt = "The rain in Spain stays mainly in the plain"
# x = "ain" in txt
# print(x)

# txt = "The rain in Spain stays mainly in the plain"
# x = "ain" not in txt
# print(x) 

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price)) 

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price)) 
# print("I want to pay {2} dollars for {0} pieces of item {1}.".format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."


myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)
