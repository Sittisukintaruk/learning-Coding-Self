import random

def play_card():
    suit =("\u2660" ,"\u2665" ,"\u2666", "\u2663")
    rank = list("A23456789") + ["10"] + list("JKQ")
    print(rank)
    deck = []
    for s in suit:
        for r in rank:
            deck.append(r + s)
    return deck

d = play_card()
print(d)
random.shuffle(d)
print(d)

p = random.sample(d, 3)
print("pick :" , p)