#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


dataframe = pd.read_csv("Zomato-data-.csv")
print(dataframe.head())


# In[4]:


def handleRate(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)

dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())


# In[7]:


print(dataframe.isnull().sum())


# 1) Listed_in (type) identify column popular restaurant categories.

# In[8]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")


# 2) votes by Restaurant type

# In[10]:


grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c='green', marker='o')
plt.xlabel('Type of restaurant')
plt.ylabel('Votes')


# In[11]:


max_votes = dataframe['votes'].max()
restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']

print('Restaurant(s) with the maximum votes:')
print(restaurant_with_max_votes)


# In[12]:


sns.countplot(x=dataframe['online_order'])


# Analyze Ratings 

# In[13]:


plt.hist(dataframe['rate'],bins=5)
plt.title('Ratings Distribution')
plt.show()


# Approx_cost(for two people) 

# In[14]:


couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)


# In[15]:


plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate', data = dataframe)


# Relationship between order mode (online_order) and restaurant type (listed_in(type))

# In[16]:


pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Heatmap')
plt.xlabel('Online Order')
plt.ylabel('Listed In (Type)')
plt.show()


# In[ ]:




