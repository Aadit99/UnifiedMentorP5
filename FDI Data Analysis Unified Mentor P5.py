#!/usr/bin/env python
# coding: utf-8

# ### Importing Necessary libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Reading and storing dataframe for manipulation and analysis

# In[2]:


fdi_data = pd.read_csv("FDI data.csv")
fdi_data.head()


# ### Checking for null values

# In[3]:


fdi_data.isnull().sum()


# ### Some Central Tendencies and Quartiles of the dataframe

# In[4]:


fdi_data.describe()


# In[5]:


fdi_data.info()


# ### FDI Trend for each Industry

# In[6]:


for index, row in fdi_data.drop("Sector",axis=1).iterrows():
    plt.plot(row, label=fdi_data["Sector"][index])
    plt.grid()
    plt.ylabel("FDI")
    plt.legend(loc="upper left")
    plt.xticks(rotation=90)
    plt.show()


# In[7]:


yearwise_total_FDI = []
for i in fdi_data.drop("Sector",axis=1).columns:
    yearwise_total_FDI.append(fdi_data[i].sum())
yearwise_total_FDI = np.array(yearwise_total_FDI)


# ### Total Yearwise FDI trend

# In[8]:


x = np.arange(17)
plt.plot(yearwise_total_FDI)
plt.xticks(x,labels=[i for i in fdi_data.drop("Sector",axis=1)],rotation=90)
plt.title("Total FDI Yearwise")
plt.xlabel("Year")
plt.grid()
plt.ylabel("FDI")
plt.show()

