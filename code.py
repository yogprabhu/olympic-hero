# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data=pd.read_csv(path)
#Code starts here
data.rename(columns={'Total':'Total_Medals'}, inplace=True)
data.head(10)


# --------------
#Code starts here# two
chk = np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
data['Better_Event']= np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
data['Better_Event']= np.where(data['Total_Summer']==data['Total_Winter'],'Both',chk)
better_event = data.Better_Event.value_counts().idxmax()


# --------------
#Code starts here
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(top_countries.tail(1).index, inplace=True)
def top_ten(df,clm):
    country_list=[]
    df1=df.nlargest(10,clm)
    country_list=list(df1.Country_Name.values)
    return country_list
top_10_summer= top_ten(top_countries,'Total_Summer')
top_10_winter= top_ten(top_countries,'Total_Winter')
top_10= top_ten(top_countries,'Total_Medals')
common=list(set(top_10_summer).intersection(top_10_winter,top_10))
print(top_10_summer)
print(top_10_winter)
print(top_10)
print(common)


# --------------
#Code starts here
summer_df=data[data.Country_Name.isin(top_10_summer)]
winter_df=data[data.Country_Name.isin(top_10_winter)]
top_df=data[data.Country_Name.isin(top_10)]
sgrp=summer_df.groupby(by=['Country_Name'])['Total_Summer'].sum()
wgrp=winter_df.groupby(by=['Country_Name'])['Total_Winter'].sum()
tgrp=top_df.groupby(by=['Country_Name'])['Total_Medals'].sum()
sgrp.plot(kind='bar', title='Top10 countries in Summer')
plt.show()
wgrp.plot(kind='bar', title='Top10 countries in Winter')
plt.show()
tgrp.plot(kind='bar', title='Top10 countries in Top')
plt.show()


# --------------
#Code starts here
# FIVE
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=max(summer_df['Golden_Ratio'])
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=max(winter_df['Golden_Ratio'])
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=max(top_df['Golden_Ratio'])
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']


# --------------
#Code starts here
# SIX
data_1 = data.drop(data.tail(1).index)
data_1['Total_Points'] = (data_1['Gold_Total']*3)+(data_1['Silver_Total']*2)+(data_1['Bronze_Total']*1)
most_points = max(data_1['Total_Points'])
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']


# --------------
#Code starts here
#Seven Last
best= data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medal Tally')
plt.xticks(rotation=45)
plt.show()


