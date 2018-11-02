#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as  pd
import numpy as np

path = "D:\RAVI\Data Science\Datasets\Davis\Davis.csv"
df = pd.read_csv(path)


# In[34]:


df.head(2)


# Now we are going to build a function to count the missing values in each column of the data frame

# In[33]:


missing_data = df.isnull()


# In[4]:


missing_data.columns.values.tolist()


# In[5]:


for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")


# Now we are going to drop all the rows with missing values. Note that this is not a good practice, but for the sake of simplicity in this tutorial, we are going to handle the missing values in this data set by removing the entire row. We expect to teach you more advanced methods to handle missing data in the upcoming tutorials.

# In[6]:


df.dropna(subset = ['repwt'], axis = 0, inplace = True)
df.dropna(subset = ['repht'], axis = 0, inplace = True)
#df.reset_index(drop = True, inplace = True)
df.head(10)


# Now let us run our missing values function again

# In[7]:


df.shape


# In[8]:


path = "D:\RAVI\Data Science\Datasets\davis_cleaned.csv"
df.to_csv(path)


# Now that we have cleaned our data, we can jump into the analytics part

# First lets get a sneak peak of our data

# In[9]:


df.describe()


# Male and Female Percentage

# In[10]:


import matplotlib.pyplot as plt
df["sex"].value_counts().plot.pie()
plt.gca().set_aspect("equal")


# Majority of the persons who participated in the survey are females

# In[11]:


df.hist(column = 'height', rwidth = 0.85, bins = 12)


# Now we will subset males from the dataset to some descriptive analysis 

# First we have to create 2 dataframes subsetting males and females

# In[26]:


mdf = df[df.sex == 'M']
fdf = df[df.sex == 'F']


# In[13]:


from matplotlib import pyplot

bins = np.linspace(145, 200, 40)

pyplot.hist(mdf['height'], bins, alpha=0.5, label='males', edgecolor = 'black')
pyplot.hist(fdf['height'], bins, alpha=0.5, label='females', edgecolor = 'black')
pyplot.legend(loc='upper right')
pyplot.show()


# Distribution of Weights in Males and females

# In[14]:


bins = np.linspace(25, 175, 70)

pyplot.hist(mdf['weight'], bins, alpha=0.5, label='males', edgecolor = 'black')
pyplot.hist(fdf['weight'], bins, alpha=0.5, label='females', edgecolor = 'black')
pyplot.legend(loc='upper right')
pyplot.show()


# It turns out that Males and Females have approximately similar weights. But if you look deeper, it can be concluded that men are heavier. There are some extreme data as well.

# Now we are going to calculate BMI for each and every individual  and append that column to our initial data frame

# In[15]:


df['bmi']=df['weight']/((0.01*df['height'])*(0.01*df['height']))
df.head(1)


# In[18]:


bins = np.linspace(15, 38, 10)

pyplot.hist(mdf['bmi'], bins, alpha=0.5,  label='males', edgecolor = 'black')
pyplot.hist(fdf['bmi'], bins, alpha=0.5,  label='females', edgecolor = 'black')
pyplot.legend(loc='upper right')
pyplot.show()


# A BMI value between 20-24 is normal. From the above histogram, it is visible that majority of women have a normal  BMI and there are considerable no. of men who are over weight.

# 

# Now  let us calculate the BMI based on the reported height and weight values

# In[23]:


df['newbmi'] = df['repwt']/((0.01*df['repht'])*(0.01*df['repht'])) 


# In[24]:


df['bmi_def'] = df['bmi'] - df['newbmi']


# In[25]:


df.head(2)


# In[32]:


bins = np.linspace(-7, 5, 50)

pyplot.hist(mdf['bmi_def'],bins,  alpha=0.5,  label='males', edgecolor = 'black')
pyplot.hist(fdf['bmi_def'],bins,  alpha=0.5,  label='females', edgecolor = 'black')
pyplot.legend(loc='upper right')
pyplot.show()

