#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv(r'C:\Users\Dell\Downloads\Udemy Courses.csv')


# In[3]:


data


# In[10]:


data.duplicated().sum()


# In[9]:


data.drop_duplicates(inplace=True)


# In[11]:


data.duplicated().sum()


# In[12]:


data.isnull().sum()


# In[13]:


#Q. 1) What are all different subjects for which Udemy is offering courses ?


# In[14]:


data.head()


# In[15]:


data['subject'].unique()   #answer


# In[16]:


#Q. 2) Which subject has the maximum number of courses.


# In[17]:


data['subject'].value_counts()  #answer


# In[18]:


#Q. 3) Show all the courses which are Free of Cost.


# In[19]:


data[data['is_paid']==False]  #answer


# In[20]:


#Q. 4) Show all the courses which are Paid.


# In[21]:


data[data['is_paid']==True]   #answer


# In[22]:


#Q. 5) Which are Top Selling Courses ?


# In[27]:


data.sort_values('num_subscribers',ascending=False)  #answer


# In[28]:


#Q. 6) Which are Least Selling Courses ?


# In[29]:


data.sort_values('num_subscribers')  #answer


# In[33]:


#Q. 7) Show all courses of Graphic Design where the price is equal 100 ?


# In[40]:


data[(data['subject']=='Graphic Design') & (data['price']=='100')]  #answer


# In[41]:


#Q. 8) List out all the courses that are related to 'Python'.


# In[42]:


data[data['course_title'].str.contains('Python')]  #answer


# In[43]:


len(data[data['course_title'].str.contains('Python')])


# In[44]:


#Q. 9) What are courses that were published in the year 2015 ?


# In[49]:


data.dtypes


# In[48]:


data['published_timestamp']=pd.to_datetime(data['published_timestamp'])


# In[50]:


data['Year']=data['published_timestamp'].dt.year


# In[53]:


data[data['Year']==2015]    #answer


# In[54]:


#Q. 10) What is the Max. Number of Subscribers for Each Level of courses ?


# In[55]:


data.head()


# In[57]:


data.groupby('level')['num_subscribers'].max()  #answer


# In[ ]:




