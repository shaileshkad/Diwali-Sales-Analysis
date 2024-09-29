#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as np
import pandas as pd 
import matplotlib .pyplot as plt 
get_ipython().run_line_magic('', 'matplotlib inline')
import seaborn as sns 


# In[14]:


df=pd.read_csv('Diwali Sales Data.csv',encoding= 'unicode_escape')
df


# In[15]:


df.shape


# In[16]:


df.head()


# In[17]:


df.info()


# In[18]:


# drop unrelated/blank columns
df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[21]:


# Check For Null values 
pd.isnull(df).sum()


# In[22]:


#Drop Null values 
df.dropna(inplace=True)


# In[23]:


# change data Type 
df["Amount"]=df["Amount"].astype('int')


# In[24]:


df['Amount'].dtypes


# In[25]:


df.columns


# In[27]:


# Rename Column 
df.rename(columns={'Marital_Status': 'Shaadi'})


# In[28]:


# describe() method returns description of the data in the dataframe (i.e. Count,mean,STD,etc)
df.describe()


# In[29]:


# use describe()for specific Columns 
df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis
# 
# 
# Gender
# 

# In[37]:


# ploting a bar Chart For Gender and it's Count

ax=sns.countplot(x='Gender',data =df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[36]:


import seaborn as sns


# In[39]:


# plotting a bar chart for gender vs total amount 

sales_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Gender',y='Amount',data=sales_gen)


# In[41]:


# From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men


# Age
# 

# In[40]:


ax = sns.countplot(data =df,x= 'Age Group',hue= 'Gender')
for bars in ax.containers:   # use of the Value Showing 
    ax.bar_label(bars)


# In[43]:


# total Amount Vs Age group

sales_age =df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x = 'Age Group',y='Amount',data =sales_age)


# In[45]:


# From above graphs we can see that most of the buyers are of age group between 26-35 yrs female


# STATE

# In[49]:


# total Number of orders from top 10 states 

sales_state = df.groupby (['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state,x='State',y='Orders')


# In[50]:


# total Amount/sales from top 10 states

sales_state= df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state,x='State',y='Amount')


# In[51]:


# From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively


# Marital Status

# In[54]:


ax = sns.countplot(data = df, x = 'Marital_Status')
sns.set(rc={'figure.figsize':(3,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[55]:


sales_state =df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state,x='Marital_Status',y='Amount',hue='Gender')


# In[56]:


# From above graphs we can see that most of the buyers are married (women) and they have high purchasing power


# Occupation

# In[57]:


sns.set(rc={'figure.figsize':(20,5)})
ax =sns.countplot(data = df, x='Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[58]:


sales_state =df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending =False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state,x='Occupation',y='Amount')


# From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector

# Product Category

# In[61]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
   ax.bar_label(bars)


# In[62]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category 

# In[63]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[64]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# Conclusion:
# Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

# In[ ]:




