from tkinter import *

window = Tk()
window.title("Калькулятор")
window.geometry("500x500")
num1 = 0
num2 = 0
calcu = ""
selp = False
selm = False
SelectMul = False
seldIV = False
def mafop(model):
    global calcu ,num1, selp, selm, SelectMul, seldIV
    num1 = float(calcu)
    calcu = ""
    label.config(text=calcu)
    if model == "+":
        selp = True
    elif model == "-":
         selm = True
    elif model == "*":
        SelectMul = True
    elif model == "/":
        seldIV = True
def cler ():
    global calcu, num1, num2 
    calcu = ""
    num1 = 0
    num2 = 0
    label.config(text=calcu)
    
def icl():
    global calcu ,num2,num1, selp, selm, SelectMul
    num2 = float(calcu)
    if selp:
        calcu = num1 + num2
        selp = False
    
    elif selm:
        calcu = num1 - num2
        selm = False
    elif SelectMul:
        calcu = num1 * num2
        SelectMul = False
    
    elif seldIV:
        calcu = num1 / num2
        SelectMul = False
    label.config(text=calcu)
    


window.resizable(width=False, height=False)
frame = Frame(window, bg='blue')
frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
label = Label(frame, text="а", bg='blue', fg='blue')
label.place(x=1, y=1, width=488)
label = Label(frame, text="0", font=100)
def button (num):
    global calcu
    num = str(num)
    calcu += num
    label.config(text=calcu)
label. place(x=1,y=1, width=488)
buttons = []
xb = 50
yb = 300
for i in range(10):
    buttons.append(Button(frame, text=i, font=50, command=lambda i=i:button(i)))
    if i == 0:
        buttons[0].place(x=175, y=425, width=100, height=50)
    else:
        buttons[i].place(x=xb, y=yb, width=100, height=50)
        xb += 125
        if xb > 300:
            xb = 50
            yb -= 125   
bPlus = Button (frame, text="+", font=50, command=lambda i=i:mafop("+"))
bPlus. place(x = 425, y = 380, width=50, height=100)

bMinus = Button (frame, text="-", font=50, command=lambda i=i:mafop("-"))
bMinus. place(x = 425, y = 270, width=50,height=100)

bdevite = Button (frame, text="/", font=50,command=lambda i=i:mafop("/"))
bdevite. place(x = 425, y = 160, width=50,height=100) 

bmultt = Button (frame, text="*", font=50, command=lambda i=i:mafop("*"))
bmultt. place(x = 425, y = 50, width=50,height=100)

bicw = Button (frame, text="=", font=50, command=icl )
bicw. place(x = 300, y = 425, width=100,height=50)

bcler = Button (frame, text="c", font=50, command=cler)
bcler. place(x = 50, y = 425, width=100,height=50)



window.mainloop()

