#mod 

def leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False


def double_even(n):
    return True if n % 2 == 0 else False
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

def odd_number(n):
    return not(double_even(n))
    # if n % 2 == 1:
    #     return True
    # else:
    #     return False

def promotion(come , pay , per_head , pax):
    # come 4 ,pay 2
    # come 5 , pay = ?
    # per_head = 100
    # 200 + 100 
    return  (pax // come) * (pay * per_head) + (pax % come ) * per_head  #หารปัดเศษทิ้ง




# print(double_even(5))
# print(odd_number(5))
print(promotion(4,2,100,4))