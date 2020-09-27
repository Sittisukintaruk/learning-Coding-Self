
# name = "beer" #pf snipet
# print(f'name : {name}')
# label = 'hero.txt'
# with open(label, mode = 'r' ,encoding= 'utf8') as f:   #rf read file
#     s=f.read()

# print(s)p
if __name__ == "__main__":
    label = "hero.txt"
    with open(label, mode = 'r' ,encoding= 'utf8') as f:
        s=f.read()
    print(s)