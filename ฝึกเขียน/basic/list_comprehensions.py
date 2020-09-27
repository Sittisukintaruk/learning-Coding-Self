def vl():
    for i in range(1, 11):
        print(i , i * 0.621371192)

def v2():
    [print(i , i * 0.621371192) for i in range(1, 11)]
    # m = [i * 0.621371192 for i in range(1, 11)]
    n = [kg_mal(i) for i in range(1, 11)]

    # print(m)
    print(f'{n}')

def v3(): #lamda
    m = list(map((lambda i: i * 0.621371192 ), range(1,11)))
    print(f'{m}')

def kg_mal(k): #lamda
    return k *  0.621371192

def sumof_bleach():
    # mp = [i  for i in range(1,11)]
    # print(mp)
    [print(i) for i in range(1,11)]


sumof_bleach()
# v2()
# v3()