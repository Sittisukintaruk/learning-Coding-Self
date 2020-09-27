def price_with_vat(amount):
    vat = amount * 7 / 107 # 
    price = amount -  vat
    # t = price , vat # tuple
    # return t
    return price , vat

# # print(price_with_vat(107))
# a = price_with_vat(200)
# print(type(a))
# print(a)
# print(f"price = {a[0]}")
# print(f"vat = {a[1]}")
# p , v = price_with_vat(200)
# print(f"p = {p}")
# print(f"v = {v}")


def thai_area(sqwa):
    rai = sqwa // 400
    ngan = (sqwa - (rai *400)) // 100
    wa = sqwa % 100
    return rai , ngan , wa

a = 956
print(thai_area(a))
r , n , w = thai_area(a)

print(f'{r} {n} {w}')



# print(f"price = {a[0]:.0f}")