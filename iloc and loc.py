#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np


# In[21]:


df = pd.DataFrame(np.arange(12).reshape(3,4))


# In[22]:


df


# In[23]:


df.loc[0,:]


# In[24]:


df.loc[[0,1,2],:]  


# In[25]:


#or


# In[26]:


df.loc[0:2,:]


# In[28]:


df.loc[0:1]


# In[32]:


df.loc[:, 0:3]


# iloc 

# In[35]:


df.iloc[:,0:3] #it wont include 3


# In[ ]:




