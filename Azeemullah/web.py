#!/usr/bin/env python
# coding: utf-8

# In[4]:


import webbrowser
i = input('Enter Search : ')

i = i.split()

web = 'https://www.google.com.pk/search?ei=DAngXLeOKsu2aYO2q5AO&q='

for l in i:

    web = web+l

webbrowser.open_new_tab(web)


# In[ ]:




