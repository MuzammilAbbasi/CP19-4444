import tkinter as tk
from tkinter import messagebox as mb
from tkinter import Frame
from tkinter import StringVar
import pyttsx3
i = pyttsx3.init()
p = tk.Tk()
var = tk.StringVar()
p.title('Speaker')
def say():
    a = l2.get()
    l = 3
    while(l<=5):
        if(a=='exit'):
            break
        else:
            i.say(a)
            i.runAndWait()
            break
p.geometry("200x100")
l1 = tk.Label(p,text = 'Enter the Sentence')
l2 = tk.Entry(p)
l3 = tk.Button(p,text = 'SAY',command = say)
l1.pack()
l2.pack()
l3.pack()
p.mainloop()



