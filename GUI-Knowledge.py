from tkinter import *
from tkinter import ttk # theme of tk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('600x400')

L1 = Label(GUI, text = 'โปรแกรมบันทึกความรู้',font = ('Tahoma',30), fg = 'blue')
L1.place(x=30,y=20)
#B1 = ttk.Button(GUI, text = 'เงินมีอยู่กี่บาท')     # create button
#B1.pack(ipadx = 20, ipady = 20)             # show button in the middle

############################
def Button2():
    text = 'ตอนนี้มีเงิน 100 บาท'
    messagebox.showinfo('เงินในบัญชี', text)
    #messagebox.showerror('เงินในบัญชี', text)
   

#FB1 = Frame(GUI)
FB1 = LabelFrame(GUI, text = 'Money')
FB1.place(x=100,y=100)
B2 = ttk.Button(FB1, text = 'เงินมีอยู่กี่บาท', command = Button2)     # create button
# B2.pack(ipadx = 20, ipady = 20)  
B2.pack(ipadx=20,ipady=20, padx = 12.5, pady = 10)
############################

def Button3():
    text = 'Python 101, Math'
    #messagebox.showinfo('เงินในบัญชี', text)
    messagebox.showerror('วิชาเรียน', text)
    

FB2 = Frame(GUI)
FB2.place(x=100,y=210)
B3 = ttk.Button(FB2, text = 'สัปดาห์นี้เรียนวิชาอะไร', command = Button3)     # create button  
B3.pack(ipadx=20,ipady=20)
############################

GUI.mainloop()
