#ตัวอย่างการใช้งาน finally 
try:
    items = ['Mac', 'iPhone', 'iPad']

    print('Avilable items: ', items)
    need = input('What do you want to buy?: ')
    if need not in items:
        raise Exception('Sorry, \'' + need + '\'' + ' out of stock')

    print('You have purchased ' + '\'' + need + '\'')

except Exception as e:
    print(e)

finally: #ทำเสมอแม้ จะผิดพลาด
    print("Thank you for shopping with us")