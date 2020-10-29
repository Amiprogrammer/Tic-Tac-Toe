from tkinter import *
from tkinter import messagebox

master = Tk()
master.iconbitmap("juliao-martins.ico")
master.title("Tic Tac Toe")


b1 = Button(master, text="X", fg="white", bg="black", font=("Apercu Mono",40), width=4, height=2)

b1.grid(row=0, column=0)

master.mainloop()
