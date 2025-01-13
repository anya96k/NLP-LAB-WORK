#!/usr/bin/env python
# coding: utf-8

# In[10]:



import numpy as np

import pandas as pd


# In[9]:


list = [1, 2, 15]
print(a[0]) 
list.append(11) 
list.remove(2) 
print(list)


# In[13]:


tup = ('om', 'For')
print(tup)


# In[14]:


set1 = {10, 2,30, 4}
print(set1)


# In[15]:


import re


# In[16]:


(/1//txt="the, rain, in, ichalkarnji")
x=re.findall("al",txt)
print (x)


# In[17]:


txt = "The rain in ichalkarnji"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


# In[18]:


txt = "The rain in ichalkarnji"
x = re.search("miraj", txt)
print(x) 


# In[19]:


txt = "The rain in Ichalkarnji"
x = re.search("ichalkaranji", txt)
print(x) 


# In[20]:


txt = "The rain in ichalkaranji"
x = re.split("\s", txt)
print(x) 


# In[21]:


txt = "The rain in ichalkaranji"
x = re.sub("\s", "12", txt)
print(x) 


# In[26]:


txt = "The rain in ichalkaranji"
x = re.search(r"\bi\w+", txt)
print(x.span())


# In[29]:


txt = "The rain in ichalkaranji"
x = re.search(r"\br\w+", txt)
print(x.group())


# In[28]:


txt = "The rain in ichalkaranji"
x = re.search("^The.*ichalkaranji$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")


# In[30]:


(/2//txt="This, is, an, example, sentence, with, stopwords.")
x=re.findall("en",txt)
print (x)


# In[31]:


txt = "This is an example sentence with stopwords"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


# In[33]:


txt = "This is an example sentence with stopwords"
x = re.search("with", txt)
print(x) 


# In[34]:


txt = "This is an example sentence with stopwords"
x = re.search("sent", txt)
print(x) 


# In[35]:


txt = "This is an example sentence with stopwords"
x = re.split("\s", txt)
print(x) 


# In[36]:


txt = "This is an example sentence with stopwords"
x = re.sub("\s", ".", txt)
print(x) 


# In[ ]:




