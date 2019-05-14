import tkinter as tk
from tkinter import *
p = tk.Tk()
p.title('ChatBot')
def chat():
    a = l2.get()
    l = 3
    while(l<=5):
        if(a=='exit'):
            break
        else:
            l4.insert(END, a +'\n')
            l2.delete(0,END)
            l2.insert(0,'')
            break
            
p.geometry("400x200")
l1 = tk.Label(p,text = "Let's Chat Type Below")
l2 = tk.Entry(p)
l3 = tk.Button(p,text = 'CHAT',command = chat)
l4 = tk.Text(p,height=4, width=20)
l4.pack()
l1.pack()
l2.pack()
l3.pack()
p.mainloop()
