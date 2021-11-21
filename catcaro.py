from tkinter import *
from tkinter import messagebox
# tạo cửa sổ
window = Tk()
window.title("CAT CARO")
window.geometry("500x550")

ctn = 0
# import 25 box
boxcat1 = "1"
boxcat2 = "2"
boxcat3 = "3"
boxcat4 = "4"
boxcat5 = "5"
boxcat6 = "6"
boxcat7 = "7"
boxcat8 = "8"
boxcat9 = "9"
boxcat10 = "10"
boxcat11 = "11"
boxcat12 = "12"
boxcat13 = "13"
boxcat14 = "14"
boxcat15 = "15"
boxcat16 = "16"
boxcat17 = "17"
boxcat18 = "18"
boxcat19 = "19"
boxcat20 = "20"
boxcat21 = "21"
boxcat22 = "22"
boxcat23 = "23"
boxcat24 = "24"
boxcat25 = "25"


pa = StringVar()
pb = StringVar()
p1 = StringVar()
p2 = StringVar()
label = Label(window, text="CAT 1: ", font='Times 15 bold', bg='white', fg='black')
label.grid(row=12, column=0)

label = Label(window, text="CAT2: ", font='Times 15 bold', bg='white', fg='black')
label.grid(row=12, column=3)
cat1_name = Entry(window, textvariable=p1, bd=5)
cat1_name.grid(row=15, column=0, columnspan=2)
cat2_name = Entry(window, textvariable=p2, bd=5)
cat2_name.grid(row=15, column=3, columnspan=6)
# tạo 25 button
button1 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(1))
button1.grid(row='0', column="0", ipadx="40", ipady="30")
button2 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(2))
button2.grid(row='0', column="1", ipadx="40", ipady="30")
button3 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(3))
button3.grid(row='0', column="2", ipadx="40", ipady="30")
button4 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(4))
button4.grid(row='0', column="3", ipadx="40", ipady="30")
button5 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(5))
button5.grid(row='0', column="4", ipadx="40", ipady="30")
button6 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(6))
button6.grid(row='1', column="0", ipadx="40", ipady="30")
button7 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(7))
button7.grid(row='1', column="1", ipadx="40", ipady="30")
button8 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(8))
button8.grid(row='1', column="2", ipadx="40", ipady="30")
button9 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(9))
button9.grid(row='1', column="3", ipadx="40", ipady="30")
button10 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(10))
button10.grid(row='1', column="4", ipadx="40", ipady="30")
button11 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(11))
button11.grid(row='2', column="0", ipadx="40", ipady="30")
button12 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(12))
button12.grid(row='2', column="1", ipadx="40", ipady="30")
button13 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(13))
button13.grid(row='2', column="2", ipadx="40", ipady="30")
button14 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(14))
button14.grid(row='2', column="3", ipadx="40", ipady="30")
button15 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(15))
button15.grid(row='2', column="4", ipadx="40", ipady="30")
button16 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(16))
button16.grid(row='3', column="0", ipadx="40", ipady="30")
button17 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(17))
button17.grid(row='3', column="1", ipadx="40", ipady="30")
button18 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(18))
button18.grid(row='3', column="2", ipadx="40", ipady="30")
button19 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(19))
button19.grid(row='3', column="3", ipadx="40", ipady="30")
button20 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(20))
button20.grid(row='3', column="4", ipadx="40", ipady="30")
button21 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(21))
button21.grid(row='4', column="0", ipadx="40", ipady="30")
button22 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(22))
button22.grid(row='4', column="1", ipadx="40", ipady="30")
button23 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(23))
button23.grid(row='4', column="2", ipadx="40", ipady="30")
button24 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(24))
button24.grid(row='4', column="3", ipadx="40", ipady="30")
button25 = Button(window, text="  ", font='Times 9 bold', bg='blue', fg='white', command=lambda: activate(25))
button25.grid(row='4', column="4", ipadx="40", ipady="30")
player = 1

# khai báo toàn bộ biến
def activate(box):
    global player
    global ctn
    global pa
    global pb
    global cat1_name
    global cat2_name
    global boxcat1
    global boxcat2
    global boxcat3
    global boxcat4
    global boxcat5
    global boxcat6
    global boxcat7
    global boxcat8
    global boxcat9
    global boxcat10
    global boxcat11
    global boxcat12
    global boxcat13
    global boxcat14
    global boxcat15
    global boxcat16
    global boxcat17
    global boxcat18
    global boxcat19
    global boxcat20
    global boxcat21
    global boxcat22
    global boxcat23
    global boxcat24
    global boxcat25

    ctn = ctn + 1

# chèn X O vào button
    if box == 1 and player == 1:
        button1.config(text="O")
        player = 2
        boxcat1 = "O"
    elif box == 1 and player == 2:
        button1.config(text="X")
        player = 1
        boxcat1 = "X"
    elif box == 2 and player == 1:
        button2.config(text="O")
        player = 2
        boxcat2 = "O"
    elif box == 2 and player == 2:
        button2.config(text="X")
        player = 1
        boxcat2 = "X"
    elif box == 3 and player == 1:
        button3.config(text="O")
        player = 2
        boxcat3 = "O"
    elif box == 3 and player == 2:
        button3.config(text="X")
        player = 1
        boxcat3 = "X"
    elif box == 4 and player == 1:
        button4.config(text="O")
        player = 2
        boxcat4 = "O"
    elif box == 4 and player == 2:
        button4.config(text="X")
        player = 1
        boxcat4 = "X"
    elif box == 5 and player == 1:
        button5.config(text="O")
        player = 2
        boxcat5 = "O"
    elif box == 5 and player == 2:
        button5.config(text="X")
        player = 1
        boxcat5 = "X"
    elif box == 6 and player == 1:
        button6.config(text="O")
        player = 2
        boxcat6 = "O"
    elif box == 6 and player == 2:
        button6.config(text="X")
        player = 1
        boxcat6 = "X"
    elif box == 7 and player == 1:
        button7.config(text="O")
        player = 2
        boxcat7 = "O"
    elif box == 7 and player == 2:
        button7.config(text="X")
        player = 1
        boxcat7 = "X"
    elif box == 8 and player == 1:
        button8.config(text="O")
        player = 2
        boxcat8 = "O"
    elif box == 8 and player == 2:
        button8.config(text="X")
        player = 1
        boxcat8 = "X"
    elif box == 9 and player == 1:
        button9.config(text="O")
        player = 2
        boxcat9 = "O"
    elif box == 9 and player == 2:
        button9.config(text="X")
        player = 1
        boxcat9 = "X"
    elif box == 10 and player == 1:
        button10.config(text="O")
        player = 2
        boxcat10 = "O"
    elif box == 10 and player == 2:
        button10.config(text="X")
        player = 1
        boxcat10 = "X"
    elif box == 11 and player == 1:
        button11.config(text="O")
        player = 2
        boxcat11 = "O"
    elif box == 11 and player == 2:
        button11.config(text="X")
        player = 1
        boxcat11 = "X"
    elif box == 12 and player == 1:
        button12.config(text="O")
        player = 2
        boxcat12 = "O"
    elif box == 12 and player == 2:
        button12.config(text="X")
        player = 1
        boxcat12 = "X"
    elif box == 13 and player == 1:
        button13.config(text="O")
        player = 2
        boxcat13 = "O"
    elif box == 13 and player == 2:
        button13.config(text="X")
        player = 1
        boxcat13 = "X"
    elif box == 14 and player == 1:
        button14.config(text="O")
        player = 2
        boxcat14 = "O"
    elif box == 14 and player == 2:
        button14.config(text="X")
        player = 1
        boxcat14 = "X"
    elif box == 15 and player == 1:
        button15.config(text="O")
        player = 2
        boxcat15 = "O"
    elif box == 15 and player == 2:
        button15.config(text="X")
        player = 1
        boxcat15 = "X"
    elif box == 16 and player == 1:
        button16.config(text="O")
        player = 2
        boxcat16 = "O"
    elif box == 16 and player == 2:
        button16.config(text="X")
        player = 1
        boxcat16 = "X"
    elif box == 17 and player == 1:
        button17.config(text="O")
        player = 2
        boxcat17 = "O"
    elif box == 17 and player == 2:
        button17.config(text="X")
        player = 1
        boxcat17 = "X"
    elif box == 18 and player == 1:
        button18.config(text="O")
        player = 2
        boxcat18 = "O"
    elif box == 18 and player == 2:
        button18.config(text="X")
        player = 1
        boxcat18 = "X"
    elif box == 19 and player == 1:
        button19.config(text="O")
        player = 2
        boxcat19 = "O"
    elif box == 19 and player == 2:
        button19.config(text="X")
        player = 1
        boxcat19 = "X"
    elif box == 20 and player == 1:
        button20.config(text="O")
        player = 2
        boxcat20 = "O"
    elif box == 20 and player == 2:
        button20.config(text="X")
        player = 1
        boxcat20 = "X"
    elif box == 21 and player == 1:
        button21.config(text="O")
        player = 2
        boxcat21 = "O"
    elif box == 21 and player == 2:
        button21.config(text="X")
        player = 1
        boxcat21 = "X"
    elif box == 22 and player == 1:
        button22.config(text="O")
        player = 2
        boxcat22 = "O"
    elif box == 22 and player == 2:
        button22.config(text="X")
        player = 1
        boxcat22 = "X"
    elif box == 23 and player == 1:
        button23.config(text="O")
        player = 2
        boxcat23 = "O"
    elif box == 23 and player == 2:
        button23.config(text="X")
        player = 1
        boxcat23 = "X"
    elif box == 24 and player == 1:
        button24.config(text="O")
        player = 2
        boxcat24 = "O"
    elif box == 24 and player == 2:
        button24.config(text="X")
        player = 1
        boxcat24 = "X"
    elif box == 25 and player == 1:
        button25.config(text="O")
        player = 2
        boxcat25 = "O"
    elif box == 25 and player == 2:
        button25.config(text="X")
        player = 1
        boxcat25 = "X"
# điều kiên chiến thắng
    if boxcat1 == boxcat2 == boxcat3 == boxcat4 == boxcat5 == "O" or boxcat6 == boxcat7 == boxcat8 == boxcat9 == boxcat10 == "O" or boxcat11 == boxcat12 == boxcat13 == boxcat14 == boxcat15 == "O" or boxcat16 == boxcat17 == boxcat18 == boxcat19boxcatbx20 == "O" or boxcat21 == boxcat22 == boxcat23 == boxcat24 == boxcat25 == "O":
        pa = p1.get()
        messagebox._show("Game end", "player: " + pa + " " + "wins")
        exit(0)
    elif boxcat1 == boxcat2 == boxcat3 == boxcat4 == boxcat5 == "X" or boxcat6 == boxcat7 == boxcat8 == boxcat9 == boxcat10 == "X" or boxcat11 == boxcat12 == boxcat13 == boxcat14 == boxcat15 == "X" or boxcat16 == boxcat17 == boxcat18 == boxcat19boxcatbx20 == "X" or boxcat21 == boxcat22 == boxcat23 == boxcat24 == boxcat25 == "X":
        pb = p2.get()
        messagebox._show("Game end", "player: " + pb + " " + " wins")
        exit(0)
    elif boxcat1 == boxcat6 == boxcat11 == boxcat16 == boxcat21 == "O" or boxcat6 == boxcat7 == boxcat12 == boxcat17 == boxcat22 == "O" or boxcat3 == boxcat8 == boxcat13 == boxcat18 == boxcat23 == "O" or boxcat4 == boxcat9 == boxcat14 == boxcat19 == boxcat24 == "O" or boxcat5 == boxcat10 == boxcat15 == boxcat20 == boxcat25 == "O":
        pa = p1.get()
        messagebox._show("Game end", "player: " + pa + " " + " wins")
        exit(0)
    elif boxcat1 == boxcat6 == boxcat11 == boxcat16 == boxcat21 == "X" or boxcat6 == boxcat7 == boxcat12 == boxcat17 == boxcat22 == "X" or boxcat3 == boxcat8 == boxcat13 == boxcat18 == boxcat23 == "X" or boxcat4 == boxcat9 == boxcat14 == boxcat19 == boxcat24 == "X" or boxcat5 == boxcat10 == boxcat15 == boxcat20 == boxcat25 == "X":
        pb = p2.get()
        messagebox._show("Game end", "player: " + pb + " " + " wins")
        exit(0)
    elif boxcat1 == boxcat7 == boxcat13 == boxcat19 == boxcat25 == "O" or boxcat5 == boxcat9 == boxcat13 == boxcat17 == boxcat21 == "O":
        pa = p1.get()
        messagebox._show("Game end", "player: " + pa + " " + " wins")
        exit(0)
    elif boxcat1 == boxcat7 == boxcat13 == boxcat19 == boxcat25 == "X" or boxcat5 == boxcat9 == boxcat13 == boxcat17 == boxcat21 == "X":
        pb = p2.get()
        messagebox._show("Game end", "player: " + pb + " " + " wins")
        exit(0)
    elif ctn == 25:
        messagebox._show("STOPPPPPPPPP", "AHHHHHHHHHH TIE")


def close_window():
    window.destroy()


Label(window, text="Click for fun:", bg="black", fg="white", font="none 10 bold").grid(row=17, column=2, sticky=W)
Button(window, text="just for fun", width=10, command=close_window).grid(row=18, column=2, sticky=W)

window.mainloop()