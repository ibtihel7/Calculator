from tkinter import *

 # create a GUI window
gui = Tk()
 
gui.configure(background="grey")

gui.title("Calculator")
 
gui.geometry("270x150")

equation = StringVar()
label_area = Label(gui, textvariable = equation)
label_area.grid(row=4,columnspan=2, ipadx=70)
label_area = ''


def press(num):
    global label_area
    label_area = str(label_area) + str(num)
    equation.set(label_area)

def equalpress():
    try:
        global label_area
        total = str(eval(label_area))
        equation.set(total)
        label_area = ""
    except:
 
        equation.set(" error ")
        label_area = ""

def clear():
    global label_area
    label_area = ""
    equation.set("")

button1 = Button(gui, text=' 1',command=lambda: press(1),  fg='black', bg='white', height=1, width=7)
button1.grid(row=0, column=0)

button2 = Button(gui, text=' 2',command=lambda: press(2), fg='black', bg='white', height=1, width=7)
button2.grid(row=0, column=1)

button3 = Button(gui, text=' 3',command=lambda: press(3), fg='black', bg='white', height=1, width=7)
button3.grid(row=0, column=2)

button4 = Button(gui, text=' 4',command=lambda: press(4), fg='black', bg='white', height=1, width=7)
button4.grid(row=1, column=0)

button5 = Button(gui, text=' 5',command=lambda: press(5), fg='black', bg='white', height=1, width=7)
button5.grid(row=1, column=1)

button6 = Button(gui, text='6',command=lambda: press(6),fg='black', bg='white', height=1, width=7)
button6.grid(row=1, column=2)

button7 = Button(gui, text='7',command=lambda: press(7), fg='black', bg='white', height=1, width=7)
button7.grid(row=2, column=0)

button8 = Button(gui, text='8',command=lambda: press(8), fg='black', bg='white', height=1, width=7)
button8.grid(row=2, column=1)

button9 = Button(gui, text='9',command=lambda: press(9), fg='black', bg='white', height=1, width=7)
button9.grid(row=2, column=2)

button0 = Button(gui, text='0',command=lambda: press(0), fg='black', bg='white', height=1, width=7)
button0.grid(row=3, column=0)

button_dec = Button(gui, text='.',command=lambda: press('.'), fg='black', bg='white', height=1, width=7)
button_dec.grid(row=3, column=1)

button_egal = Button(gui, text='=', fg='black',command=lambda:equalpress(), bg='white', height=1, width=7)
button_egal.grid(row=3, column=2)

button_div = Button(gui, text='/',command=lambda: press('/'), fg='black', bg='white', height=1, width=7)
button_div.grid(row=0, column=3)

button_multip = Button(gui, text='*',command=lambda: press('*'), fg='black', bg='white', height=1, width=7)
button_multip.grid(row=1, column=3)

button_minus = Button(gui, text='-', command=lambda: press('-'),fg='black', bg='white', height=1, width=7)
button_minus.grid(row=2, column=3)

button_plus = Button(gui, text='+', command=lambda: press("+"),fg='black', bg='white', height=1, width=7)
button_plus.grid(row=3, column=3)


button_clear = Button(gui, text='Clear', fg='black', bg='red', command=clear, height=1, width=7)
button_clear.grid(row=3, column='4')
 
gui.mainloop()
