#!/usr/bin/env python
# coding: utf-8

# In[6]:


import webbrowser
import pyttsx3
from fuzzywuzzy import fuzz
import tkinter as tk
from tkinter import *
p = tk.Tk()
s = pyttsx3.init()
rate = s.getProperty('rate')
s.setProperty('rate', 125)
data1 = open(r'ques.txt', 'r+')
data2 = open(r'ans.txt', 'r+')
predic = []
answers = []
p.configure(bg="grey")
p.title('ChatBot')
for u in data1: 
    predic.append(u)
for n in data2:
    answers.append(n)
def chat():
    inputer = l2.get()
    l4.insert(END,'you : ' + inputer+ '\n')
    l2.delete(0,END)
    l2.insert(0,'')
    els = ''
    for i in predic:
        a = fuzz.partial_ratio(inputer,i)
        if a > 95:
            index = predic.index(i)
            o = answers[index]
            els = o
            s.say(o)
            l4.insert(END,'Bot : ' + (answers [index]))
            s.runAndWait()
            break
        elif 'search' in inputer:
            s.say('searching')
            inputer = inputer.replace('search', '')
            web = 'https://www.google.com.pk/search?source=hp&ei=ez3gXMTDM-WRlwSC_o7IBg&q=' + inputer
            webbrowser.open_new_tab(web)
            s.runAndWait()
            break
    search(inputer,els)
def search(inpu,le):
    if(le==''):
        s.say('searching')
        web = 'https://www.google.com.pk/search?source=hp&ei=ez3gXMTDM-WRlwSC_o7IBg&q=' + inpu
        webbrowser.open_new_tab(web)
        s.runAndWait()
p.geometry("700x600")
l1 = tk.Label(p,text = "Let's Chat Type Below")
l2 = tk.Entry(p)
l3 = tk.Button(p,text = 'CHAT',command = chat)
l4 = tk.Text(p,height=20, width=50)
l5 = tk.Label(p,text = "For searching anything type 'search'+'anything you desire'")
l4.pack()
l1.pack()
l2.pack()
l3.pack()
l5.pack()
p.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




