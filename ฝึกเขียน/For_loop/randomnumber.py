import random
import time
def randomnumber_target():
    deck = []
    for i in range(20,101):
        deck.append(i)
    pick =  random.sample(deck , 1)
    number = int(pick[0])
    return number

def randomnumber(namber):
    deck = []
    for i in range(namber):
        deck.append(random.randint(1,9))
        random.shuffle(deck)

    return deck
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('หมดเวลา !!')





targer = randomnumber_target()
deck = randomnumber(4)


print("เลขที่คำตอบที่สุ่มได้ : {}".format(targer))
print("-"*50)
print("เลขที่ใช้เพื่อหาคำตอบ :",end="")
for i in range(len(deck)):
    print(deck[i],end=" ")

print("\n")
print("-"*50)
print("เริ่มต้นจับเวลา : ")
countdown(10)


