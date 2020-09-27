number = int(input(""))
getint = 0
for i in range(number):
    span = number
    span = span - i
    dolor = i + (i + 1)
    print(" "* (span - 1) ,"*" * dolor )
    getint = dolor
     
for b in range(1 , number):
    spanb = b
    dolorb = getint - 2
    print(" "*spanb ,"*" * dolorb)
    getint -=  2