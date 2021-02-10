#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
import numpy as np


# In[42]:


df =pd.DataFrame(np.arange(12).reshape(3, 4), columns=['P', 'Q', 'R', 'S'])


# In[43]:


df


# In[44]:


df.drop(['Q','R'],axis=1)


# In[45]:


df.drop(columns=['P', 'S'])


# In[46]:


df.drop([0, 1])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




