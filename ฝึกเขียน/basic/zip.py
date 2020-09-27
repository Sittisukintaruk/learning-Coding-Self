def demo():
    weight = [70 , 60 ,48]
    height = [170 , 175 , 161]
    bmi = []
    for i in range(len(weight)):
        bmi.append(weight[i]/(height[i] / 100) ** 2)
    return bmi


def demo1():
    weight = [70 , 60 ,48]
    height = [170 , 175 , 161]
    bmi = []
    for w,h in zip(weight,height):
        bmi.append(w/(h / 100) ** 2)
    return bmi

def demo2():
    weight = [70 , 60 ,48]
    height = [170 , 175 , 161]
    return[ w/(h / 100) ** 2   for w,h in zip(weight,height)]        

def demo3():
    weight = [70 , 60 ,48]
    height = [170 , 175 , 161]
    name = ['beer', 'mai' ,'fah']
    return[ {n:w/(h / 100) ** 2}   for w,h,n in zip(weight,height,name)]   


def demo4():
    weight = [70 , 60 ,48]
    height = [170 , 175 , 161]
    name = ['beer', 'mai' ,'fah']
    gender = ['F','M' ,'M']
    return [ {n:w/(h / 100) ** 2}   for w,h,n,g in zip(weight,height,name,gender) if g == 'M']   

# print(f'{demo()}')
# print(f'{demo1()}')
# print(f'{demo2()}')
# print(f'{demo3()}')
# print(f'{demo4()}')

def demo5():
    weight = [70 , 60 ,48]
    height = [170 , 175 , 161]
    name = ['beer', 'mai' ,'fah']
    gender = ['F','M' ,'M']
    text = "*"
    return [print(f'Myname is {n}\nmy weight :{w}\nmyheight {h} and gender is a {g} \n{text*40}')    for w,h,n,g in zip(weight , height , name , gender) if g == "M" ]


demo5()