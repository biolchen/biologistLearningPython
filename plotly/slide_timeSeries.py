#!/usr/bin/env python
# coding: utf-8


# ## Dataset
# 
# You are to analyze campaign contributions to the 2016 U.S. presidential primary races made in California. 
# Use the csv file located here: https://drive.google.com/file/d/1Lgg-PwXQ6TQLDowd6XyBxZw5g1NGWPjB/view?usp=sharing. 
# This file originally came from the U.S. Federal Election Commission (https://www.fec.gov/).
# Documentation for this data can be found here: https://drive.google.com/file/d/11o_SByceenv0NgNMstM-dxC1jL7I9fHL/view?usp=sharing

import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import seaborn as sns
from plotly.offline import iplot
import plotly.graph_objs as go


os.chdir(os.path.dirname(__file__))
# These commands below set some options for pandas and to have matplotlib show the charts in the notebook
pd.set_option('display.max_rows', 10)
pd.options.display.float_format = '{:,.2f}'.format

# Define a date parser to pass to read_csv
d = lambda x: pd.datetime.strptime(x, '%d-%b-%y')

# Load the data
contrib = pd.read_csv('../large_files/P00000001-CA.csv', 
                      index_col=False, 
                      parse_dates=['contb_receipt_dt'], 
                      date_parser=d,
                     dtype={'contbr_zip':'object', 'receipt_desc':'object', 'memo_cd':'object'})
print(contrib.shape)


# Subset data to primary period 
contrib = contrib.copy()[contrib['contb_receipt_dt'] <= datetime.datetime(2016, 5, 31)]
print(contrib.shape)


# ## 1. Exploring Data
print(contrib.shape)
print(contrib.columns)
contrib.groupby('election_tp').agg({'election_tp':'count'}).rename({'election_tp':'count'}, axis=1)


contrib.election_tp.unique()
contrib.contb_receipt_amt.hist(bins = 10)
contrib.isna().sum().sort_values(ascending=False)
contrib[contrib['contbr_city'].str.len() < 2]

a=contrib.contbr_city.value_counts()
df=a[a>1000]
f, ax = plt.subplots(figsize=(12, 5))
ax.set_title('Counts of Contribiutions by City')
ax.set_xlabel('Counts')
ax.set_ylabel('Frequency')
sns.distplot(df, bins=500)



df_2a=contrib[['cand_nm','contb_receipt_amt']].groupby('cand_nm', as_index=False).agg({'contb_receipt_amt':'count'}).sort_values('contb_receipt_amt', ascending=False)
df_2a.rename({'contb_receipt_amt':'contb_receipt_count'}, axis='columns', inplace=True)
print(df_2a)



df_2b=contrib[['cand_nm','contb_receipt_amt']].groupby('cand_nm', as_index=False).agg({'contb_receipt_amt':'sum'}).sort_values('contb_receipt_amt', ascending=False)
df_2b.rename({'contb_receipt_amt':'contb_receipt_total'}, axis='columns', inplace=True)

print(df_2b)


df_2ab=pd.merge(df_2a,df_2b, left_on='cand_nm',right_on='cand_nm')
print(df_2ab)



df_2ab['average_receipt']=df_2ab['contb_receipt_total']/df_2ab['contb_receipt_count']
print(df_2ab)


# **2e. Plotting a Bar Chart**
# 
# Make a bar chart that shows two different bars per candidate with one bar as the total value of the donations and the other as average $ per donation. 
# - Show the Candidates Name on the x-axis
# - Show the amount on the y-axis
# - Include a title
# - Include axis labels
# - Hint: You can make the y-axis a log-scale if you'd prefer

# 2e YOUR CODE HERE

f, [axA,axB] = plt.subplots(figsize=(23, 9),nrows=1, ncols=2)
axA.set_title('Total $', fontsize = 25)
axB.set_title('Average $ per Donation', fontsize = 25)
axA.set_ylabel('amount', fontsize = 20)
axB.set_ylabel('amount', fontsize = 20)
axA.tick_params(axis='x', rotation=90, direction='out', labelsize=20)
axB.tick_params(axis='x', rotation=90, direction='out',labelsize=20)
axA.tick_params(axis='y', labelsize=20)
axB.tick_params(axis='y', labelsize=20)
sns.barplot(x = 'cand_nm', y = 'contb_receipt_total', 
            data=df_2ab.sort_values(['contb_receipt_total'],ascending=False), 
            ax=axA)
sns.barplot(x = 'cand_nm', y = 'average_receipt', 
            data=df_2ab.sort_values(['average_receipt'],ascending=False), 
            ax=axB)


# **2f. Comment on the results of your data analysis in a short paragraph.**
# 
# - There are several interesting conclusions you can draw from the table you have created.
# - What have you learned about campaign contributions in California?

# `2f YOUR RESPONSE HERE`
# 1. Hillary received that largest total amount of donation, whereas the average donation to James S III is the highest. Tis is because Hillary has a much larger counts of donations, including a large quatity of small donations.
# 
# 2. In general, democrates received more donation than republicans in CA.
# 

# ## 3. Exploring Donor Occupations
# 
# Above in part 2, we saw that some simple data analysis can give us insights into the campaigns of our candidates. Now let's quickly look to see what *kind* of person is donating to each campaign using the `contbr_occupation` variable.

# **3a. Show the top 5 occupations of individuals that contributed to Hillary Clinton.** 
# 
# - Subset your data to create a dataframe with only donations for Hillary Clinton.
# - Then use the `value_counts` and `head` methods to present the top 5 occupations (`contbr_occupation`) for her donors.
# - Note: we are just interested in the count of donations, not the value of those donations.

df_Hillary=contrib[(contrib['cand_nm'] == 'Clinton, Hillary Rodham') &                    (contrib['contbr_occupation'] != '[BLANK]')]

top_occupation=df_Hillary.groupby(['contbr_occupation']).agg({'contbr_occupation':'count'}).rename(columns={'contbr_occupation': 'count'}).sort_values('count', ascending = False).apply(lambda x: x.nlargest(5)).reset_index()

top_occupation


# **3b. Write a function called `get_donors`.**
# 
# Imagine that you want to do the previous operation on several candidates.  To keep your work neat, you want to take the work you did on the Clinton-subset and wrap it in a function that you can apply to other subsets of the data.
# 
# - The function should take a DataFrame as a parameter, and return a Series containing the counts for the top 5 occupations contained in that DataFrame.



## Asumption: For sanity, I elimnated the row when occupations are either [BLANK] or 'INFORMATION REQUESTED' 
def get_donors(df: str):
    """This function takes a dataframe that contains a variable named contbr_occupation.
    It outputs a Series containing the counts for the 5 most common values of that
    variable."""
    
    df_input=contrib[(contrib['cand_nm'] == df) &                    (contrib['contbr_occupation'] != '[BLANK]') &                     (contrib['contbr_occupation'] != 'INFORMATION REQUESTED') &
                    (contrib['contbr_occupation'] !='INFORMATION REQUESTED PER BEST EFFORTS') &
                    (contrib['contbr_occupation'] != 'RETIRED')]
    
    top_occupation=df_input.    groupby(['contbr_occupation']).    agg({'contbr_occupation':'count'}).    rename(columns={'contbr_occupation': 'count'}).    sort_values('count', ascending = False).    apply(lambda x: x.nlargest(5)).reset_index()
    
    
    print("top 5 occupations of {}'s donors: \n{}\n".format(df, top_occupation))


# **3c. Now run the `get_donors` function on subsets of the dataframe corresponding to three candidates.**
# 
# - Hillary Clinton
# - Bernie Sanders
# - Donald Trump

# In[19]:


## I assume you want to use these names as input of the function. 

# 3c YOUR CODE HERE
get_donors('Clinton, Hillary Rodham')
get_donors('Sanders, Bernard')
get_donors('Trump, Donald J.')


# **3d. Finally, use `groupby` to separate the entire dataset by candidate.**
# 
# - Call .apply(get_donors) on your groupby object, which will apply the function you wrote to each subset of your data.
# - Look at your output and marvel at what pandas can do in just one line!

def get_donors(df):
    """This function takes a dataframe that contains a variable named contbr_occupation.
    It outputs a Series containing the counts for the 5 most common values of that
    variable."""
    
    top_occupation = df.    groupby(['contbr_occupation']).    agg({'contbr_occupation':'count'}).    rename(columns = {'contbr_occupation': 'count'}).    sort_values('count', ascending = False).    apply(lambda x: x.nlargest(5)).reset_index()
    
    return top_occupation
pd.set_option('display.max_rows', 100)

df_input=contrib[(contrib['contbr_occupation'] != '[BLANK]') &
                 (contrib['contbr_occupation'] != 'INFORMATION REQUESTED') &
                 (contrib['contbr_occupation'] !='INFORMATION REQUESTED PER BEST EFFORTS') &
                 (contrib['contbr_occupation'] != 'RETIRED') &
                 (contrib['contbr_occupation'] != 'NONE')]

df_input.groupby('cand_nm').apply(get_donors)


# **3e. Comment on your findings in a short paragraph.**

# `3e YOUR RESPONSE HERE`
# One of the most striking finding is that top contributors for Bernard Sanders are unemployed Americans. The data also show that he has received a swell of financial support from Americans giving in small amounts, as nearly three-quarters of Senator Sanders' donations have been under $200. Candidates are most like to receive financial support from the people with similar professional background. For example, Jill Stein receive large donations from researchers, so does Ben Carson from physicians. In addition and perhaps very predictable, billionaire businessman Donald Trump are more popular among CEO and bussiness leaders. 

# **3f. Think about your findings in section 3 vs. your findings in section 2 of this assignment.**
# 
# Do you have any new insights into the results you got in section 2, now that you see the top occupations for each candidate

# `3f YOUR RESPONSE HERE`
# Yes. There is more detailed information about the backgroud of contributors for each candidate.

# 
# ## 4. Plotting Data
# 
# There is an important element that we have not yet explored in this dataset - time.

# **4a. Present a single line chart with the following elements.**
# 
# - Show the date on the x-axis
# - Show the contribution amount on the y-axis
# - Include a title
# - Include axis labels

df = contrib.groupby(['contb_receipt_dt']).sum()


df.loc[df['contb_receipt_amt']<0] = 0
# I assume that contb_receipt_amt should be a value > 0. If not I changed it to 0
df.plot(y = 'contb_receipt_amt', 
        use_index = True,
        figsize = (20,6),
        title = "contribution $ over time")


# **4b. Make a better time-series line chart**
# 
# This chart is messy and it is hard to gain insights from it.  Improve the chart from 4a so that your new chart shows a specific insight. In the spot provided, write the insight(s) that can be gained from this new time-series line chart.

o

df=contrib.groupby(['cand_nm','contb_receipt_dt']).agg({'contb_receipt_amt':'sum'})
df=df[df > 0]

df=df.reset_index().pivot(index='contb_receipt_dt', 
                          columns='cand_nm', 
                          values='contb_receipt_amt')
df=df.fillna(0)
df.sort_index(axis = 0)
df=df.reset_index()
df=df[(df['contb_receipt_dt']>'2015-05-01') & (df['contb_receipt_dt']<'2016-6-1')]
df

#import pickle

#with open('../large_files/contrib_ca_2016.pkl', 'wb') as handle:
#   pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)

df=contrib.groupby(['cand_nm','contb_receipt_dt']).agg({'contb_receipt_amt':'sum'})
df=df[df > 0]

df=df.reset_index().pivot(index='contb_receipt_dt', 
                          columns='cand_nm', 
                          values='contb_receipt_amt')
df=df.fillna(0)
df.sort_index(axis = 0)
df=df.reset_index()
df=df[(df['contb_receipt_dt']>'2015-05-01') & (df['contb_receipt_dt']<'2016-10-19')]


#df.to_csv('slide_timeSeries.csv', index = False)

trace_high = go.Scatter(
                x=df.contb_receipt_dt,
                y=df['Clinton, Hillary Rodham'],
                name = "Clinton",
                line = dict(color = '#0015bc'),
                opacity = 0.8)

trace_low = go.Scatter(
                x=df.contb_receipt_dt,
                y=df['Trump, Donald J.'],
                name = "Trump",
                line = dict(color = '#ff0000'),
                opacity = 0.8)

data = [trace_high, trace_low]

layout = dict(
    title = "Comparison of Donation to Clinton and Trump in 2016 (USD)",
    xaxis = dict(
        range = ['2015-05-01','2016-10-18'],
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=12,
                     label='12m',
                     step='month',
                     stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
    
    )
)

fig = dict(data=data, layout=layout)
iplot(fig)
