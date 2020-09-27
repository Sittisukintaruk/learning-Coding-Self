class Manmal(object):
    def __init__(self,ManmalName):
        print(ManmalName)
        
class dog(Manmal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('dog')



def Square(n):
    return n*n

def MapFuntion():
    numbers = (1,2,3,4)
    result = map(Square,numbers)    
    print(result)
    print(set(result))

def ZipFuntion():
    numbers = [1,2,3]
    strings = ['one','two','three']

    result = zip()
    resultList = list(result)
    print(resultList)

    result = zip(numbers,strings)
    resultset = set(result)
    print(resultset)
    #>>>>{(1, 'one'), (3, 'three'), (2, 'two')}<<<<

def SuperFuntion():
    d = dog()
    print(d)

def HashFuntion():
    print('hash value for an integer; ',hash(190))
    print('hash value for an decimal; ',hash(171.23))
    print('hash value for an string; ',hash('python'))
    voweles = ('a','b','c','d')
    print('hash for voweles: ', hash(voweles))

def FormatFuntion():
    print('Format for integer: ', format(123,"d"))
    print('Format for float: ', format(123.456789,"f"))
    print('Format for binary: ', format(12,"b"))
    """
    Format for integer:  123
    Format for float:  123.456789
    Format for binary:  1100
    """
def EnumerateFuntion():
    glod = ['one','two','three']
    enumerates = enumerate(glod)
    print(type(enumerates))
    print(list(enumerates))
    
    enumerates = enumerate(glod,10) 
    print(list(enumerates))
    """
[(0, 'one'), (1, 'two'), (2, 'three')]
[(10, 'one'), (11, 'two'), (12, 'three')]
    """

def MemoryFuntion():
    Bytearray = bytearray('ABC','utf-8')
    mv = memoryview(Bytearray)
    print(mv[0])
    print(bytes(mv[0:2]))
    print(list(mv[0:3]))
    """
    Output:
    65
    b'AB'
    [65, 66, 67]
    """
def PowFuntion():# ยกกำลัง
    print(pow(2,2))
    print(pow(-2,2))
    print(pow(2,-2))
    print(pow(-2,-2))
    """
        4
        4
        0.25
        0.25
    """ 
def reprFuntion(): #แสดงผลทั้งหมด 'foo'
    var = 'foo'
    print(repr(var))

def stripFuntion():#ตัดช่องว่าง
    a = '   Apple  '
    print(a.strip())

def roundFuntion(): #ปัดเศษส่วน .5 ขึ้นไป ปัดขึ้น .5 ลงมา ปัดลง
    print(round(10))
    print(round(10.7))
    print(round(5.2))
    print(round(2.665, 2))
    """  
    10
    11
    5
    2.67
    """
def absFuntion(): #ทำให้ไม่เป็นจำนวน ติด - 
    interger = -20
    print(abs(interger))

    floating = -30.33
    print(abs(floating))

def Clearfuntion(): # Remove ทุกอย่างใน eleament
    print("88")

def dirfuntion(): # แสดง Module ของ eleament
    print("88")