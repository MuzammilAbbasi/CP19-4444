#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox as mb
from tkinter import Frame

m = tk.Tk()
def su():
    o = 1+1
    print(o)
    mb.showinfo("Titlllllle","PAKISTAN ZINDABAD")
m.title('Program')
p = Frame(m)
p.grid()

m.geometry("700x500")
l1 = tk.Button(m,text='We Are Pakistani Pakistan Zindabad',command = su)
l1.grid(row=3,column=3,padx=20,pady=30)
l2 = tk.Button(m,text='PAKISTAN ZINDABAD',command = su)
l2.grid(row=2,column=2,padx=15,pady=20)
l3 = tk.Label(m,text='Azeemullah')
l3.grid(row=1,column=1,padx=10,pady=15)
e1=tk.Entry(p)
e1.grid(row=4,column=4)
m.mainloop()


# In[ ]:


import tkinter as tk
from tkinter import messagebox as mb
from tkinter import Frame

m = tk.Tk()
def su():
    o = 1+1
    print(o)
    mb.showinfo("Titlllllle","PAKISTAN ZINDABAD")
    
m.geometry("400x200")
m.title('Program')
l1 = tk.Button(m,text='We Are Pakistani Pakistan Zindabad',command = su,fg="Red",height=10,width=30)
l2 = tk.Button(m,text='Pakistan Zindabad',command = su)
l3 = tk.Label(m,text='Azeemullah')
l3.pack()
l1.pack()
l2.pack()
m.mainloop()


# In[ ]:





# In[ ]:




