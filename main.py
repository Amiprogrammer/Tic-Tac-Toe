from tkinter import *
from tkinter import messagebox

master = Tk()
master.iconbitmap("juliao-martins.ico")
master.title("Tic Tac Toe")

clicked = True
counts = 0

def on_click(b):
    pass

b1 = Button(master, text="", fg="white", bg="black", font=("Apercu Mono",40), width=4, height=2, command=lambda: on_click(b1))
b2 = Button(master, text="", fg="white", bg="black", font=("Apercu Mono",40), width=4, height=2, command=lambda: on_click(b2))
b3 = Button(master, text="", fg="white", bg="black", font=("Apercu Mono",40), width=4, height=2, command=lambda: on_click(b3))

b4 = Button(master, text="", fg="white", bg="black", font=("Apercu Mono",40), width=4, height=2, command=lambda: on_click(b4))
b5 = Button(master, text="", fg="white", bg="black", font=("Apercu Mono",40), width=4, height=2, command=lambda: on_click(b5))
b6 = Button(master, text="", fg="white", bg="black", font=("Apercu Mono",40), width=4, height=2, command=lambda: on_click(b6))

b7 = Button(master, text="", fg="white", bg="black", font=("Apercu Mono",40), width=4, height=2, command=lambda: on_click(b7))
b8 = Button(master, text="", fg="white", bg="black", font=("Apercu Mono",40), width=4, height=2, command=lambda: on_click(b8))
b9 = Button(master, text="", fg="white", bg="black", font=("Apercu Mono",40), width=4, height=2, command=lambda: on_click(b9))



b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)


master.mainloop()
