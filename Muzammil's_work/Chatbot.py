#!/usr/bin/env python
# coding: utf-8

# In[48]:


import webbrowser
import pyttsx3
from fuzzywuzzy import fuzz
import tkinter as tk
from tkinter import *
p = tk.Tk()
s = pyttsx3.init()
rate = s.getProperty('rate')
volume = s.getProperty('volume')
s.setProperty('rate', 125)
data1 = open(r'ques.txt', 'r+')
data2 = open(r'ans.txt', 'r+')
predic = []
answers = []
p.title('ChatBot')
for u in data1: 
    predic.append(u)
for n in data2:
    answers.append(n)
def chat():
    inputer = l2.get()
    l4.insert(END,'you : ' + inputer+ '\n')
    for i in predic:
        a = fuzz.partial_ratio(inputer,i)
        if a > 95:
            index = predic.index(i)
            o = answers[index]
            s.say(o)
            l4.insert(END,'Bot : ' + (answers [index]))
            l2.delete(0,END)
            l2.insert(0,'')
            s.runAndWait()
            break
        elif 'search' in inputer:
            s.say('searching')
            inputer = inputer.replace('search', '')
            web = 'https://www.google.com.pk/search?source=hp&ei=ez3gXMTDM-WRlwSC_o7IBg&q=' + inputer
            webbrowser.open_new_tab(web)
            l2.delete(0,END)
            l2.insert(0,'')
            s.runAndWait()
            break
                
p.geometry("500x250")
l1 = tk.Label(p,text = "Let's Chat Type Below")
l2 = tk.Entry(p)
l3 = tk.Button(p,text = 'CHAT',command = chat)
l4 = tk.Text(p,height=5, width=40)
l4.pack()
l1.pack()
l2.pack()
l3.pack()
p.mainloop()


# In[ ]:





# In[ ]:




