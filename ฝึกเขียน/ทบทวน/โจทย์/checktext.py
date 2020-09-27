text = input()

listtext = list(text.strip())
Strint = ''
print(listtext)
count = 0
for i in listtext:
    if i.islower() == True:
        listtext[count] = i.upper()
        count = count + 1 
    elif i.isupper() == True:
        listtext[count] = i.lower()
        count = count + 1 
    elif i.isspace() == True:
        count = count + 1 

print(Strint.join(listtext))