#!/usr/bin/env python
# coding: utf-8

# # 44688-Data Analytics Capstone Project

# ## FDIP (Fire Department Incident Prediction)

# ##### 03/13/23 - 04/28/23

# ##### Debra D. "DeeDee" Walker

# ##### Northwest Missouri State University, Maryville MO 64468, USA

# In[1]:


#Import the pandas framework to import and work with the dataset
import pandas as pd

#Set pandas to show all rows and not truncate
pd.set_option("display.max_rows", None)

#Import datetime so we can work with dates and times
import datetime as dt

#Import numpy
import numpy as np

#Data is accessed through the csv file download due to the limitations of the API on the site for this large dataset. The API endpoint limits hits and requires data to be requested by page
# Data was pulled from https://data.cityofnewyork.us/Public-Safety/Incidents-Responded-to-by-Fire-Companies/tm6d-hbzd on March 16, 2023
#Use the function read_csv from pandas and create a dataframe assigned to variable df
df = pd.read_csv("Incidents_Responded_to_by_Fire_Companies.csv", sep=",", dtype={"IM_INCIDENT_KEY": str, "FIRE_BOX": str, "INCIDENT_TYPE_DESC": str, "INCIDENT_DATE_TIME": object, 
                                                                                 "ARRIVAL_DATE_TIME": object, "UNITS_ONSCENE": float, "LAST_UNIT_CLEARED_DATE_TIME": object, "HIGHEST_LEVEL_DESC": str,
                                                                                "TOTAL_INCIDENT_DURATION": float, "ACTION_TAKEN1_DESC": str, "ACTION_TAKEN2_DESC": str, "ACTION_TAKEN3_DESC": str,
                                                                                "PROPERTY_USE_DESC": str, "STREET_HIGHWAY": str, "ZIP_CODE": str, "BOROUGH_DESC": str, "FLOOR": str, 
                                                                                 "CO_DETECTOR_PRESENT_DESC": str, "FIRE_ORIGIN_BELOW_GRADE_FLAG": str, "STORY_FIRE_ORIGIN_COUNT": str,
                                                                                "FIRE_SPREAD_DESC": str, "DETECTOR_PRESENCE_DESC": str, "AES_PRESENCE_DESC": str, "STANDPIPE_SYS_PRESENT_FLAG": str})


# In[2]:


#Remove columns/features that we aren't using to reduce the size of the file or project concentration
df.drop(['FIRE_BOX', 'ARRIVAL_DATE_TIME', 'LAST_UNIT_CLEARED_DATE_TIME', 'STREET_HIGHWAY', 'FLOOR', 'CO_DETECTOR_PRESENT_DESC', 'FIRE_ORIGIN_BELOW_GRADE_FLAG',
                'STORY_FIRE_ORIGIN_COUNT', 'FIRE_SPREAD_DESC', 'DETECTOR_PRESENCE_DESC', 'AES_PRESENCE_DESC', 'STANDPIPE_SYS_PRESENT_FLAG', 'ACTION_TAKEN2_DESC',
                'ACTION_TAKEN3_DESC'], axis=1, inplace=True)


# In[3]:


#convert INCIDENT_DATE_TIME from object to datetime format then print min & max
df["INCIDENT_DATE_TIME"] = pd.to_datetime(df["INCIDENT_DATE_TIME"], infer_datetime_format = True)
print (df["INCIDENT_DATE_TIME"].min())
print (df["INCIDENT_DATE_TIME"].max())


# In[4]:


#filter by year only selecting 2017 - 2022 then print min & max to verify
df = df[(df["INCIDENT_DATE_TIME"]).dt.year.isin([2017,2018,2019,2020,2021])]
print (df["INCIDENT_DATE_TIME"].min())
print (df["INCIDENT_DATE_TIME"].max())


# In[5]:


df.info()


# In[6]:


#the file is large enough that info() doesn't report the null values so we have to force it.
#This is for record 1 through 1,599,999
df.iloc[:1600000].info(verbose=True)


# In[7]:


#the file is large enough that info() doesn't report the null values so we have to force it.
#This is for record 1,600,000 through 2,348,968
df.iloc[1600000:2348969].info(verbose=True)


# In[8]:


df.describe()


# In[9]:


df["INCIDENT_TYPE_DESC"].value_counts()


# In[10]:


#Based on the code assign a new category
df.loc[df['INCIDENT_TYPE_DESC'].str.startswith('1'), 'INCIDENT_CATEGORY'] = 'FIRE'
df.loc[df['INCIDENT_TYPE_DESC'].str.startswith('2'), 'INCIDENT_CATEGORY'] = 'OVERPRESSURE RUPTURE, EXPLOSION, OVERHEAT-NO FIRE'
df.loc[df['INCIDENT_TYPE_DESC'].str.startswith('3'), 'INCIDENT_CATEGORY'] = 'RESCUE & EMS'
df.loc[df['INCIDENT_TYPE_DESC'].str.startswith('4'), 'INCIDENT_CATEGORY'] = 'HAZARDOUS CONDITION-NO FIRE'
df.loc[df['INCIDENT_TYPE_DESC'].str.startswith('5'), 'INCIDENT_CATEGORY'] = 'SERVICE CALL'
df.loc[df['INCIDENT_TYPE_DESC'].str.startswith('6'), 'INCIDENT_CATEGORY'] = 'CANCELED, GOOD INTENT'
df.loc[df['INCIDENT_TYPE_DESC'].str.startswith('7'), 'INCIDENT_CATEGORY'] = 'FALSE ALARM FALSE CALL'
df.loc[df['INCIDENT_TYPE_DESC'].str.startswith('8'), 'INCIDENT_CATEGORY'] = 'SEVERE WEATHER & NATURAL DISASTER'


# In[11]:


#review value counts of new feature
df.iloc[:1600000].info(verbose=True)
df.iloc[1600000:2348969].info(verbose=True)
df["INCIDENT_CATEGORY"].value_counts()


# In[12]:


df["HIGHEST_LEVEL_DESC"].value_counts()


# In[13]:


#Remove row with no data in highest level and duration
df.dropna(subset=["HIGHEST_LEVEL_DESC","TOTAL_INCIDENT_DURATION"], inplace = True)


# In[14]:


#Based on the code assign a new category
df.loc[df['HIGHEST_LEVEL_DESC'].str.startswith('0'), 'LEVEL_CATEGORY'] = '1'
df.loc[df['HIGHEST_LEVEL_DESC'].str.startswith('1'), 'LEVEL_CATEGORY'] = '1'
df.loc[df['HIGHEST_LEVEL_DESC'].str.startswith('2'), 'LEVEL_CATEGORY'] = '2'
df.loc[df['HIGHEST_LEVEL_DESC'].str.startswith('3'), 'LEVEL_CATEGORY'] = '3'
df.loc[df['HIGHEST_LEVEL_DESC'].str.startswith('4'), 'LEVEL_CATEGORY'] = '4'
df.loc[df['HIGHEST_LEVEL_DESC'].str.startswith('5'), 'LEVEL_CATEGORY'] = '5'
df.loc[df['HIGHEST_LEVEL_DESC'].str.startswith('6'), 'LEVEL_CATEGORY'] = '6'
df.loc[df['HIGHEST_LEVEL_DESC'].str.startswith('7'), 'LEVEL_CATEGORY'] = '7'
df.loc[df['HIGHEST_LEVEL_DESC'].str.startswith('8'), 'LEVEL_CATEGORY'] = '7'
df.loc[df['HIGHEST_LEVEL_DESC'].str.startswith('11'), 'LEVEL_CATEGORY'] = '7'


# In[15]:


#review value counts of new feature
df.iloc[:1600000].info(verbose=True)
df.iloc[1600000:2348969].info(verbose=True)
df["LEVEL_CATEGORY"].value_counts()


# In[16]:


#Drop converted features 
df.drop(['HIGHEST_LEVEL_DESC'], axis=1, inplace=True)
df.drop(['INCIDENT_TYPE_DESC'], axis=1, inplace=True)


# In[17]:


df["ACTION_TAKEN1_DESC"].value_counts()


# In[18]:


#Drop feature since the most information is coming from incident type and highest level description
df.drop(["ACTION_TAKEN1_DESC"], axis=1, inplace=True)


# In[19]:


df["PROPERTY_USE_DESC"].value_counts()


# In[20]:


#Drop feature due to number of undetermined values
df.drop(['PROPERTY_USE_DESC'], axis=1, inplace=True)


# In[21]:


df["BOROUGH_DESC"].value_counts()


# In[22]:


df["ZIP_CODE"].value_counts()


# In[23]:


#Fill in nan for units on scene with the mean and round feature to integer
df['UNITS_ONSCENE'].replace([np.nan], df['UNITS_ONSCENE'].mean(), inplace = True)
df['UNITS_ONSCENE'] = df['UNITS_ONSCENE'].round(0).astype(int)
df.iloc[:1600000].info(verbose=True)
df.iloc[1600000:2348969].info(verbose=True)
df.describe()


# In[24]:


#assign counter/variable for while loop
b = 1


# In[25]:


#99999 is not a real zipcode; Cross match to borough and impute most common zip
#Using df2, filter the borough and zip and add count values
while b < 6:
    df2 = df.groupby(["BOROUGH_DESC", "ZIP_CODE"]).size().reset_index(name='counts')
    # get the most frequent zip for a borough
    df3 = df2.loc[(df2["BOROUGH_DESC"].str.contains(str(b)))].sort_values(by="counts", ascending=False).nlargest(1,"counts")
    #assign value to variable
    x = df3.iloc[0,1]
    #Assign highest count value per borough to 99999 records
    df.loc[(df["BOROUGH_DESC"].str.startswith(str(b))) & (df["ZIP_CODE"] == '99999'),"ZIP_CODE"] = x
    b += 1


# In[26]:


#verify that the 99999 is now replaced
df["ZIP_CODE"].value_counts()


# In[27]:


#Remove rows with no data
df.dropna(subset=["ZIP_CODE"], inplace = True)


# In[28]:


#Add day of the week and hour of the day to the dataset
df['Day_of_week'] = df['INCIDENT_DATE_TIME'].dt.day_name()
df['Hour_of_day'] = df['INCIDENT_DATE_TIME'].dt.hour


# In[29]:


#Convert incident duration from seconds to hours
df['TOTAL_INCIDENT_DURATION'] = df['TOTAL_INCIDENT_DURATION']/3600
df['TOTAL_INCIDENT_DURATION'] = df['TOTAL_INCIDENT_DURATION'].round(2)


# In[30]:


#Print correlation between units on scene and incident duration
print(df['UNITS_ONSCENE'].corr(df['TOTAL_INCIDENT_DURATION']))


# In[31]:


#Convert duration to category 
Durations = [(df['TOTAL_INCIDENT_DURATION'] <= .25),
             (df['TOTAL_INCIDENT_DURATION'] >.25) & (df['TOTAL_INCIDENT_DURATION'] <= .50),
             (df['TOTAL_INCIDENT_DURATION'] > .50) & (df['TOTAL_INCIDENT_DURATION'] <= .75),
             (df['TOTAL_INCIDENT_DURATION'] > .75) & (df['TOTAL_INCIDENT_DURATION'] <= 1.00),
             (df['TOTAL_INCIDENT_DURATION'] > 1.00) & (df['TOTAL_INCIDENT_DURATION'] <= 2.00),
             (df['TOTAL_INCIDENT_DURATION'] > 2.00) & (df['TOTAL_INCIDENT_DURATION'] <= 3.00),
             (df['TOTAL_INCIDENT_DURATION'] > 3.00)]

Duration_Categories = ['<=15min','15min-30min','30min-45min','45min-1hr','1-2hr','2-3hr','3hr>']

df['TOTAL_INCIDENT_DURATION'] = np.select(Durations, Duration_Categories)

df['TOTAL_INCIDENT_DURATION'].value_counts()


# In[32]:


#Review range of units on scene
df["UNITS_ONSCENE"].value_counts()


# In[33]:


#Convert units on scene to category 
df.loc[df['UNITS_ONSCENE'] >= 7, 'UNITS_ONSCENE'] = 7
df['UNITS_ONSCENE'].value_counts()


# In[34]:


#convert to object
df['UNITS_ONSCENE'] = df['UNITS_ONSCENE'].astype(str)


# In[35]:


#Rename 7 value
df.loc[df['UNITS_ONSCENE'].str.startswith('7'), 'UNITS_ONSCENE'] = '7 or more'
df['UNITS_ONSCENE'].value_counts()


# In[36]:


#Check data verification before export
df.iloc[:1600000].info(verbose=True)
df.iloc[1600000:2348969].info(verbose=True)
df.describe()
df.head(n=10)


# In[37]:


#Export clean datset for use and loading on Github
df.to_csv('fdip_clean.csv', index=False)

