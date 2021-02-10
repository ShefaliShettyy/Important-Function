#!/usr/bin/env python
# coding: utf-8

# #changing the index 

# In[2]:


import pandas as pd


# In[3]:


df =pd.DataFrame(  columns=['big','small'] , data=[[10,10],
                                                   [20,20],
                                                   [30,30],
                                                   [40,40],
                                                   [50,50],[60,60],[70,70],[80,80],[90,90]])


# In[4]:


df


# In[14]:


df.set_index([pd.Index([2, 3, 4, 5 ,1 ,6, 7 , 8 , 9]), 'big'])


# In[15]:


df.set_index(['big'])


# In[16]:


df.set_index(['big','small'])


# #apply map

# In[29]:


def myfunction(a,b):
    return a + b

x = map(myfunction,(1,5,6),(5,6,4))


# In[30]:


print(list(x))


# In[27]:


def myfunc(a,b):
    return a + b

x = map(myfunc,('cat','banna','apple'),('liion','cat','c'))
print(list(x))


# In[39]:


list1 = ['math','sci','bio']
list2 = ['phy','chem','math']


# In[59]:


result=map(lambda x,y:x==y , list1 , list2)


# In[60]:


print(list(result)) 


# In[61]:


numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 
  
result = map(lambda x, y: x + y, numbers1, numbers2) 
print(list(result)) 


# In[70]:


numbers = ['cat', 'sat', 'bat']
result1 =list(map(list,numbers))
result1


# In[ ]:




