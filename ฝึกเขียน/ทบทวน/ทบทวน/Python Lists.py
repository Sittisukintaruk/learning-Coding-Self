# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist)

# print(thislist[1])

# print(thislist[-1]) #หลังสุด 

# print(thislist[2:5])

# print(thislist[:4])

# print(thislist[2:])

# print(thislist[-4:-1])

# thislist[1] = "blackcurrant"
# print(thislist)

# for x in thislist:
#     print(x)

# if "apple" in thislist:
#       print("Yes, 'apple' is in the fruits list")
    
# print(len(thislist))

# thislist.append("orange")
# print(thislist)

# thislist.insert(1, "orange")
# print(thislist)

# thislist.remove("mango")
# print(thislist)

# thislist.pop()
# print(thislist)

# del thislist[0]
# print(thislist)

# # thislist.clear()
# # print(thislist)

# mylist = thislist.copy()
# print(mylist)

# mylist = list(thislist)
# print(mylist)

#Join Two Lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# for x in list2:
#       list1.append(x)

# print(list1)

list1.extend(list2)
print(list1)

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)