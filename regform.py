import tkinter as tk
from tkinter import *
from tkinter import ttk
window=tk.Tk()
window.configure(bg="violet")
tk.Label(window,text="STUDENT REGISTRATION FORM",justify="center").place(x=20,y=0)
#l1.pack()
tk.Label(window,text="FIRST NAME").grid(row = 1)
tk.Label(window,text="LAST NAME").grid(row =2)
tk.Label(window,text="DATE OF BIRTH").grid(row =3)
tk.Label(window,text="EMAIL ID").grid(row =4)
tk.Label(window,text="MOBILE NUMBER").grid(row =5)
tk.Label(window,text="GENDER").grid(row =6)
tk.Label(window,text="ADDRESS").grid(row =7)
tk.Label(window,text="CITY").grid(row =8)
tk.Label(window,text="PIN CODE").grid(row =9)
tk.Label(window,text="STATE").grid(row =10)
tk.Label(window,text="COUNTRY").grid(row =11)
tk.Label(window,text="Hobbies").grid(row =12)
tk.Label(window,text="QUALIFICATION").grid(row =13)
tk.Label(window,text="COURSES APPLIED FOR").grid(row =14)
e1=tk.Entry(window)
e2=tk.Entry(window)
e3=tk.Entry(window)
e4=tk.Entry(window)
n = StringVar()
day= ttk.Combobox(textvariable=n)
day['values'] = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
month = ttk.Combobox(textvariable=n)
month['values'] = ('January','February','March','April','May','June','July','August','September','October','November','December','January')
x = IntVar()
year = ttk.Combobox(intvariable = x)
year['values'] = (1999,2000,2001,2002,2004,2005,2006)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
day.grid(row = 2,column = 1)
month.grid(row = 2,column = 2)
year.grid(row = 2,column = 3)
e3.grid(row=3,column=1)
e4.grid(row=4,column=1)
r = Radiobutton()






window.mainloop()

