from tkinter import *

root = Tk()
root.title('Крестики-нолики')
root.minsize(200,200)

def click():
    print('click')

btn_w = 10
btn_h = 5

button_1 = Button(width=btn_w, height=btn_h, command=click)
button_2 = Button(width=btn_w, height=btn_h, command=click)
button_3 = Button(width=btn_w, height=btn_h, command=click)
button_4 = Button(width=btn_w, height=btn_h, command=click)
button_5 = Button(width=btn_w, height=btn_h, command=click)
button_6 = Button(width=btn_w, height=btn_h, command=click)
button_7 = Button(width=btn_w, height=btn_h, command=click)
button_8 = Button(width=btn_w, height=btn_h, command=click)
button_9 = Button(width=btn_w, height=btn_h, command=click)

button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=0, column=2)
button_4.grid(row=1, column=0)
button_5.grid(row=1, column=1)
button_6.grid(row=1, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

root.mainloop()