from pprint import pprint

def station():
    yield 'MUA'
    yield 'SAM'
    yield 'STL'
    yield 'LIM'


def sum_all_digit(n):
    return sum([int(c) for c in str(n)])

def lucky(target = 9 , start_number = 1 , stop = 100):
    d = []
    for i in range(start_number , stop+1):
        if sum_all_digit(i) == target:
            d.append(i)
    return d


def lucky_gen(taget = 9 , start_number = 1):
    i = start_number
    while True:
        if sum_all_digit(i) == taget:
            yield i
        i +=  1
        
def zip_demo():
    protext = [1,2,3,4,5]
    posttext = [6,7,5,10,9]
    i = zip(protext,posttext)
    print(next(i))
    print('*'*40)
    for z,l in i:
        print(z,l)
    # print(next(i))

# zip_demo()

# print(lucky())
# g = lucky_gen(8 , 1000 )
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))



count = 0
a = []
def day_tree(n):
    global count 
    for i in range(1,n+1):
        if i % 2 == 0 :
            count += 1
            # yield i
            a.append(i)
            
        
        else :
            pass
# def sets():
#     global count 
#     count = 5

# def s():
#     global a
#     a = ['beer' , 'mai' , 'fah']
# s()
n = 30
day_tree(n)
lists = []
for i in range(1,count+1):
    lists.append(i)


# print(day)

# print(count)
# pprint(a)
# pprint(lists)
# zipdir = zip(a,lists)
# dira = dict(zipdir)
# pprint(dira)
# print(dira)


tuples = [(5,6),(7,8),(9,6)]
ds = dict(tuples)
print(ds)


list_test = [1,2,3,4,5,6,7,8,9,10]
dis = dict.fromkeys(ds,0)



# for i in range(1,16):
#     print(next(day))

# s = station()
# print(f'{s}')
# print(f'{next(s)}')
# print(f'{next(s)}')
# print(f'{next(s)}')
# print(f'{next(s)}')
