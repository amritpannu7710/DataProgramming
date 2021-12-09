#!/usr/bin/env python
# coding: utf-8

# In[3]:


#importing the dataset
import pandas as pd
data = pd.read_csv(r"C:\Users\Manmeet\Downloads\Netflix Dataset.csv")


# In[4]:


data


# In[5]:


data.head()


# In[6]:


data.tail()


# In[7]:


#
data.shape


# In[8]:


data.size


# In[9]:


data.columns


# In[10]:


data.dtypes


# In[11]:


data.info()


# In[12]:


#duplicate
data.head()


# In[13]:


data.shape


# In[14]:


# To check row wise and detect the duplicate rows
data.duplicated()


# In[15]:


data[data.duplicated()]


# In[16]:


# To remove the duplicate rows permanently
data.drop_duplicates()


# In[17]:


# To remove the duplicate rows permanently
data.drop_duplicates(inplace = True)


# In[18]:


# No result  check all duplicate removed
data[data.duplicated()]


# In[19]:


data.shape


# In[20]:


data.head()


# In[21]:


# to show where the null value is present # true means null value is present
data.isnull()


# In[22]:


# to show the count of null values in each column
data.isnull().sum()


# In[29]:


get_ipython().system('pip install seaborn')


# In[30]:


# To import seaborn library
import seaborn as sns


# In[31]:


# using heat map to show null values count
sns.heatmap(data.isnull())


# # Q1  for "house of card" what is the show id and who is the director of this show
# 

# In[32]:


data.head()


# In[34]:


data[data['Title'].isin(['House of Cards'])]


# In[35]:


data[data['Title'].str.contains('House of Cards')]


# # Q2 In which year highest number of TV shows & movies were released ? show with bar graph

# In[36]:


data.dtypes


# In[37]:


data['Date_N'] = pd.to_datetime(data['Release_Date'])


# In[38]:


# new column Date_N is created
data.head()


# In[39]:


data.dtypes


# In[40]:


# It counts the occurence of all individual years in date column
data['Date_N'].dt.year.value_counts()


# In[41]:


# Bar graph 
data['Date_N'].dt.year.value_counts().plot(kind='bar')


# # Q3 How many movies and tv shows are in the data set ? show with bar graph

# In[43]:


data.head(2)


# In[46]:


# To group all unique items of a column and show their count
data.groupby('Category').Category.count()


# In[47]:


# To show the count of all unique values of any column in the form of bar graph
sns.countplot(data['Category'])


# # Q4 show all the movies that were released in year 2000  

# In[48]:


data.head(2)


# In[49]:


# To create new  Year column ; it will consider only year
data['Year'] = data['Date_N'].dt.year


# In[50]:


data.head(2)


# In[51]:


data[(data['Category'] =='Movie') & (data['Year']==2000)]


# In[52]:


data[(data['Category'] =='Movie') & (data['Year']==2020)]


# # Q5 Show only  the titles of all tv shows that were released in india only 

# In[53]:


data.head(2)


# In[57]:


data[ (data['Category'] =='TV Show') & (data['Country']=='India')] ['Title']


# # Q6 Show top 10 directors who gave the highest number of TV shows and movies to netflix

# In[60]:


data['Director'].value_counts().head(10)


# # Q7 show all the records where "categoory is movie  and type is comedeies" or "country is united kingdom"

# In[63]:


data[(data['Category']== 'Movie') & (data['Type']=='Comedies')]


# In[65]:


data[(data['Category']== 'Movie') & (data['Type']=='Comedies') | (data['Country']=='United Kingdom')]


# # Q8 In how many movies/shows, Tom cruise was cast?

# In[66]:


data.head(2)


# In[67]:


#filtering
data[data['Cast']=='Tom Cruise']


# In[68]:


data_new = data.dropna()


# In[69]:


data_new.head(2)


# In[70]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# # Q9 what are the different ratings defined by netflix ?

# In[71]:


data['Rating'].nunique()


# In[72]:


data['Rating'].unique()


# # Q.9.1 How many movies got the 'TV-14' rating,in Canada ?

# In[74]:


data[(data['Category']== 'Movie') & (data['Rating']=='TV-14')].shape


# In[75]:


data[(data['Category']== 'Movie') & (data['Rating']=='TV-14') & (data['Country']=='Canada')]


# In[76]:


data[(data['Category']== 'Movie') & (data['Rating']=='TV-14') & (data['Country']=='Canada')].shape


# # Q.9.2 How many TV show got the 'R' rating, after the year 2018 ?

# In[79]:


data[(data['Category']== 'TV Show') & (data['Rating']=='R')]


# In[80]:


data[(data['Category']== 'TV Show') & (data['Rating']=='R') & (data['Year'] > 2018)]


# # Q10 what is the maximum duration of amovie/show on Netflix ?

# In[81]:


data.head(2)


# In[82]:


data.Duration.unique()


# In[83]:


data.Duration.dtypes


# In[86]:


data.head(2)


# In[87]:


data[['Minutes', 'Unit']] = data['Duration'].str.split(' ',expand = True)


# In[88]:


data.head(2)


# In[89]:


data['Minutes'].max()


# In[90]:


data['Minutes'].min()


# In[91]:


data['Minutes'].mean()


# In[92]:


data.dtypes


# # Q11 which individual country has the highest number of  TV shows ?

# In[93]:


data.head(2)


# In[94]:


data_tvshow = data[data['Category']== 'TV Show']


# In[96]:


data_tvshow.head(2)


# In[97]:


data_tvshow.Country.value_counts()


# In[98]:


data_tvshow.Country.value_counts().head(1)


# # Q12 How can we sort the dataset by Year ?

# In[100]:


data.sort_values(by ='Year')


# In[102]:


data.sort_values(by ='Year',ascending=False).head(10)


# # Q13 Find all the instances where :
# 
# 
#   Category is 'Movie' and Type is 'Dramas'
#     
#     or
#     
#   Category is 'TV show' and Type is 'kids TV'

# In[103]:


data.head(2)


# In[106]:


data[(data['Category']== 'Movie') & (data['Type']=='Dramas')].head(2)


# In[109]:


data[(data['Category']== 'TV Show') & (data['Type']=="Kids' TV")]


# In[110]:


data[(data['Category']== 'Movie') & (data['Type']=='Dramas')  | (data['Category']== 'TV Show') & (data['Type']=="Kids' TV")]


# In[ ]:




