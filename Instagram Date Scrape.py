
# coding: utf-8

# In[1]:


from lxml import html
import requests
import datetime
import pandas as pd
from datascience import *
import matplotlib.pyplot as plt
from pandas import Series, DataFrame, Panel
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#the dataset of instagram posts that you're workingwith
post_urls = [ 'https://www.instagram.com/p/BkL-15NhJO4/?taken-by=eratosthena' ]


# In[3]:


lst = []
def get_a_date(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    hey = tree.text_content()
    the_index = hey.index('"taken_at_timestamp"')
    start_point = the_index + 21
    end_point = the_index + 31
    timestamp = hey[start_point:end_point]
    lst.append(timestamp)
    


# In[4]:


#loops through all of the urls at the top and applies them to get_a_date
for item in post_urls:
    try:
        get_a_date(item)
    except ValueError: #sometimes the computer doesn't read the page correctly and gives an error. these errors 
                       #generally break the code unless you make an exception for them, which is what I have done here
        pass 


# In[5]:


all_post_dates = []
for item in lst: #gives us the exact dates and times of each post
    all_post_dates.append(
    datetime.datetime.fromtimestamp(
        int(item)
    ).strftime('%Y-%m-%d'))
    


# In[6]:


dict = {} #counts the number of posts on each day
for item in all_post_dates:
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1


# In[7]:


may_df = pd.DataFrame(list(dict.items()),
                      columns=['Date','# of Posts'])
datasci_table = Table.from_df(may_df)


# In[8]:


scatter_table2 = datasci_table.select('Date',"# of Posts") 


# In[9]:


scatter_table2.to_csv('Instagram_Analytics.csv')

