name = input("")
listt = list(name)
countlist = len(listt)

for i in range(countlist,0,-1):
    print(" "*i,listt[i-1])
    
    