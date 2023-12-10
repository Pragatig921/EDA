#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df=pd.read_csv(r'C:\Users\Pc\Downloads\Python_Diwali_Sales_Analysis-main\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv', encoding='unicode_escape')


# In[3]:


df.shape


# In[4]:


df.head(5)


# In[5]:


df.info()


# In[6]:


df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[7]:


df.info()


# In[8]:


pd.isnull(df)


# In[9]:


pd.isnull(df).sum()


# In[10]:


df.shape


# In[11]:


df.dropna(inplace=True)


# In[12]:


df.shape


# In[13]:


df['Amount']=df['Amount'].astype('int')


# In[14]:


df['Amount'].dtypes


# In[15]:


df.columns


# In[16]:


df.rename(columns={'Marital_Status':'Shaadi'})


# In[17]:


df.describe()


# In[18]:


df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis

# In[19]:


df.columns


# In[20]:


sns.countplot(x='Gender', data=df);


# In[21]:


ax=sns.countplot(x='Gender', data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[22]:


df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[23]:


sales_gen=df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Gender', y='Amount',data=sales_gen)


# From above graph, we can see that most of the buyers are females and even the purchasing power of females are greater than men

# # AGE

# In[24]:


df.columns


# In[25]:


sns.countplot(data=df, x='Age Group')


# In[26]:


sns.countplot(data=df, x ='Age Group', hue='Gender')


# In[27]:


ax=sns.countplot(data=df, x='Age Group', hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[28]:


sales_age=df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Age Group', y='Amount', data=sales_age)


# From above graph, we can see that most of the buyers are of age group between 26-35 yrs female.

# # State

# In[29]:


df.columns


# In[30]:


sales_state=df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state, x='State', y='Orders')


# In[31]:


sales_state=df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state, x='State', y='Amount');


# From above graphs, we can see that most of the orders & total_sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively.

# # Marital Status

# In[32]:


ax=sns.countplot(data=df, x='Marital_Status')
sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[34]:


sales_state=df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data=sales_state, x='Marital_Status', y='Amount', hue='Gender');


# From above graphs, we can see that most of the buyers are married(women) and they have high purchasing power

# In[36]:


sns.set(rc={'figure.figsize':(20,5)})
ax=sns.countplot(data=df, x='Occupation')
for bars in ax.containers:
    ax.bar_label(bars)


# In[37]:


sales_state=df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x='Occupation', y='Amount')


# From above graphs, we can see that most of the buyers are working in IT, Healthcare and Aviation sector

# # Product Category

# In[38]:


sns.set(rc={'figure.figsize':(20,5)})
ax=sns.countplot(data=df, x='Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)


# In[41]:


sales_state=df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x='Product_Category', y='Amount');


# From above graphs, we can see that most of the sold products are from Food, clothing and Electronics Category.

# In[44]:


sales_state=df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x='Product_ID', y='Orders');


# In[46]:


fig1,ax1=plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar');


# Conclusion:
# Married women age group 26-35 yrs from UP, Maharashtra and Karnataka working in IT, Healthcare and Aviationare more likely
# buy products from Food, Clothing and Electronics Category.

# In[ ]:




