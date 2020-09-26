from tkinter import  *


def on_clik():
    # print("*"*20)
    # for i,chk in enumerate(chks):
    #     if chk.get():
    #         print(interest[i])
    lst = [interest[i] for i,chk in enumerate(chks) if chk.get()]
    # print(lst)    
    print(",".join(lst))

interest = ['Music' ,'Movie' ,'book' ,'Photography' , 'Game']
root = Tk()
root.option_add("*font" , "impact 30")

chks = [BooleanVar() for i in interest]
Label(root , text = "You Interest" ,bg = "gold").pack()
for i,s in enumerate(interest):
    Checkbutton(root, text = s, variable = chks[i]).pack(anchor = W)

    


Button(root , text = "submit" , command = on_clik).pack()


root.mainloop()