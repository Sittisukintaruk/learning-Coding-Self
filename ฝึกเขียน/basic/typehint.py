def demo(a , b):
    c = a + b
    print(f'{c}')

def beta(a:str , b:int , c):
    
    print(a , b , c)
    

def funcname(parameter_list:str) ->str:
    return parameter_list


if __name__ == "__main__":
    # demo(5,3)
    # demo('rain','bow')
    name = funcname(5)
    # beta(3,'bow',77)
    print(f'{type(name)}')
    print(f'{name}')
