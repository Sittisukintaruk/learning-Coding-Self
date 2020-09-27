# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def temple():
    for cel in range(101):
        f = (cel * 9 / 5 ) + 32
        print("{}c = {:.2f}f".format(cel, f))
        
def mult_table(from_n , to_n):
    #nested loop
    for i in range(from_n,to_n + 1):
        for j in range(1, 13):
            print("{} x {} = {} ".format(i, j , i * j))
        print("-"*40)

temple()
                 
mult_table(3 , 5)


                 