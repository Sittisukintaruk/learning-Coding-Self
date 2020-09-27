def demo():
    i = 1 
    while i <= 10:
        print(i)
        i += 1
    print("bye")
def summit():
    number = int(input("enter number : "))
    total = 0
    while number != 0:
        total += number
        number = int(input("enter number : "))
    print("bye total : ", total)


# ทำซ้ำ repeat
def sum_repeat():
    total = 0
    while True:
        number = int(input("enter number : "))
        if number!= 0:
            total += number
        else:
            break
    print("bye total : ", total)


sum_repeat()