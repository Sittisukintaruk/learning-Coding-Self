from tkinter import *

def on_lick(e):
   
    Tv_strat.set(f'you selected {selectedOtp.get()}  {contries[selectedOtp.get()]}')

root = Tk()
root.option_add("*font" , "consolas 25")
# contries = ['Thailand' , 'japan' , 'Korea']
contries = {'Thailand': 'th' , 'japan':'jp' , 'Korea': 'kr'}

selectedOtp = StringVar()
Tv_strat = StringVar()
selectedOtp.set('Thailand')

om = OptionMenu(root , selectedOtp,*contries)
om.config(width = 15)
om.grid(row = 0 , column = 0)
btn = Button(root , text = 'select' ,bg = 'orange')
btn.grid(row = 0 , column = 1)
btn.bind('<Button-1>' , on_lick)
Label(root, textvariable = Tv_strat ).grid(row = 1 , columnspan  = 2 )
root.mainloop()