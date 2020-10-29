from tkinter import *
from tkinter import messagebox

master = Tk()
master.iconbitmap("juliao-martins.ico")
master.title("Tic Tac Toe")

def disable_box():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,counts,winner

    counts = 0

    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    # ask user to reset or quit the game
    if messagebox.askyesno("Tic Tac Toe","Do you want to play again!"):
        messagebox.showinfo("Tic Tac Toe","New Game!")
        all_here()
    else:
        messagebox.showwarning("Tic Tac Toe","Program will be close!")
        master.destroy()

winner = False

def someonewon():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,winner,counts

    # if player X or O isn't win!
    if counts == 9:
        # ask user to reset or quit the game
        if messagebox.askyesno("Tic Tac Toe","Do you want to play again!"):
            messagebox.showinfo("Tic Tac Toe","New Game!")
            all_here()
        else:
            messagebox.showwarning("Tic Tac Toe","Program will be close!")
            master.destroy()

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(fg="red", bg="white")
        b2.config(fg="red", bg="white")
        b3.config(fg="red", bg="white")
        messagebox.showinfo("Tic Tac Toe","X is won!")
        disable_box()
        winner = True
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(fg="red", bg="white")
        b5.config(fg="red", bg="white")
        b6.config(fg="red", bg="white")
        messagebox.showinfo("Tic Tac Toe","X is won!")
        disable_box()
        winner = True
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(fg="red", bg="white")
        b8.config(fg="red", bg="white")
        b9.config(fg="red", bg="white")
        messagebox.showinfo("Tic Tac Toe","X is won!")
        disable_box()
        winner = True
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(fg="red", bg="white")
        b4.config(fg="red", bg="white")
        b7.config(fg="red", bg="white")
        messagebox.showinfo("Tic Tac Toe","X is won!")
        disable_box()
        winner = True
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(fg="red", bg="white")
        b5.config(fg="red", bg="white")
        b8.config(fg="red", bg="white")
        messagebox.showinfo("Tic Tac Toe","X is won!")
        disable_box()
        winner = True
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(fg="red", bg="white")
        b6.config(fg="red", bg="white")
        b9.config(fg="red", bg="white")
        messagebox.showinfo("Tic Tac Toe","X is won!")
        disable_box()
        winner = True
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(fg="red", bg="white")
        b5.config(fg="red", bg="white")
        b9.config(fg="red", bg="white")
        messagebox.showinfo("Tic Tac Toe","X is won!")
        disable_box()
        winner = True
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(fg="red", bg="white")
        b5.config(fg="red", bg="white")
        b7.config(fg="red", bg="white")
        messagebox.showinfo("Tic Tac Toe","X is won!")
        disable_box()
        winner = True

    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(fg="red", bg="white")
        b2.config(fg="red", bg="white")
        b3.config(fg="red", bg="white")
        messagebox.showinfo("Tic Tac Toe","O is won!")
        disable_box()
        winner = True
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(fg="red", bg="white")
        b5.config(fg="red", bg="white")
        b6.config(fg="red", bg="white")
        messagebox.showinfo("Tic Tac Toe","O is won!")
        disable_box()
        winner = True
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(fg="red", bg="white")
        b8.config(fg="red", bg="white")
        b9.config(fg="red", bg="white")
        messagebox.showinfo("Tic Tac Toe","O is won!")
        disable_box()
        winner = True
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(fg="red", bg="white")
        b4.config(fg="red", bg="white")
        b7.config(fg="red", bg="white")
        messagebox.showinfo("Tic Tac Toe","O is won!")
        disable_box()
        winner = True
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(fg="red", bg="white")
        b5.config(fg="red", bg="white")
        b8.config(fg="red", bg="white")
        messagebox.showinfo("Tic Tac Toe","O is won!")
        disable_box()
        winner = True
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(fg="red", bg="white")
        b6.config(fg="red", bg="white")
        b9.config(fg="red", bg="white")
        messagebox.showinfo("Tic Tac Toe","O is won!")
        disable_box()
        winner = True
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(fg="red", bg="white")
        b5.config(fg="red", bg="white")
        b9.config(fg="red", bg="white")
        messagebox.showinfo("Tic Tac Toe","O is won!")
        disable_box()
        winner = True
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(fg="red", bg="white")
        b5.config(fg="red", bg="white")
        b7.config(fg="red", bg="white")
        messagebox.showinfo("Tic Tac Toe","X is won!")
        disable_box()
        winner = True


clicked = True
counts = 0

def on_click(b):
    global clicked,counts

    if b["text"] == " " and clicked == True:
        b.config(text="X")
        counts += 1
        clicked = False
        someonewon()
    elif b["text"] == " " and clicked == False:
        b.config(text="O")
        counts += 1
        clicked = True
        someonewon()
    else:
        messagebox.showerror("Tic Tac Toe","The box already been selected!\npick another box.")

def all_here():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,clicked,counts,winner

    b1 = Button(master, text=" ", fg="white", bg="black", font=("Apercu Mono",40), width=4, height=2, command=lambda: on_click(b1))
    b2 = Button(master, text=" ", fg="white", bg="black", font=("Apercu Mono",40), width=4, height=2, command=lambda: on_click(b2))
    b3 = Button(master, text=" ", fg="white", bg="black", font=("Apercu Mono",40), width=4, height=2, command=lambda: on_click(b3))

    b4 = Button(master, text=" ", fg="white", bg="black", font=("Apercu Mono",40), width=4, height=2, command=lambda: on_click(b4))
    b5 = Button(master, text=" ", fg="white", bg="black", font=("Apercu Mono",40), width=4, height=2, command=lambda: on_click(b5))
    b6 = Button(master, text=" ", fg="white", bg="black", font=("Apercu Mono",40), width=4, height=2, command=lambda: on_click(b6))

    b7 = Button(master, text=" ", fg="white", bg="black", font=("Apercu Mono",40), width=4, height=2, command=lambda: on_click(b7))
    b8 = Button(master, text=" ", fg="white", bg="black", font=("Apercu Mono",40), width=4, height=2, command=lambda: on_click(b8))
    b9 = Button(master, text=" ", fg="white", bg="black", font=("Apercu Mono",40), width=4, height=2, command=lambda: on_click(b9))



    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


all_here()

master.mainloop()
