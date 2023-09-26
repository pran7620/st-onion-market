import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

st.title("Satana Market yearly analysis")
df = pd.read_csv('/Users/pranavaher/Desktop/projects/satana.csv')
df
#df['Price 2023'] = df['Price 2023'].astype(str)
df['Price 2023'] = pd.to_datetime(df['Price 2023'])
df['Price 2021'] = pd.to_datetime(df['Price 2021'])
df['Price 2020'] = pd.to_datetime(df['Price 2020'])
df['Price 2019'] = pd.to_datetime(df['Price 2019'])
df['Price 2018'] = pd.to_datetime(df['Price 2018'])
df['Price 2017'] = pd.to_datetime(df['Price 2017'])
df['Price 2016'] = pd.to_datetime(df['Price 2016'])
df['Price 2015'] = pd.to_datetime(df['Price 2015'])
df['Price 2014'] = pd.to_datetime(df['Price 2014'])
df['Price 2013'] = pd.to_datetime(df['Price 2013'])
df['Price 2012'] = pd.to_datetime(df['Price 2012'])
df['Price 2011'] = pd.to_datetime(df['Price 2011'])
df['Price 2010'] = pd.to_datetime(df['Price 2010'])
df['Price 2009'] = pd.to_datetime(df['Price 2009'])
df['Price 2008'] = pd.to_datetime(df['Price 2008'])
df['Price 2007'] = pd.to_datetime(df['Price 2007'])
df['Price 2006'] = pd.to_datetime(df['Price 2006'])


st.title("Max Price of Satana Market")

selected_year = st.selectbox("Select a year", ['2023', '2021','2020','2019','2018','2017','2016','2015','2014','2013','2012','2011','2010','2009','2008','2007','2006'])

if selected_year == '2023':
    x_col = 'Price 2023'
    y_col = 'Max Price (2023)'
    title = "Max Price for 2023"
elif selected_year == '2021':
    x_col = 'Price 2021'
    y_col = 'Max Price (2021)'
    title = "Max Price for 2021"
elif selected_year == '2019':
    x_col = 'Price 2019'
    y_col = 'Max Price (2019)'
    title = "Max Price for 2019"
elif selected_year == '2018':
    x_col = 'Price 2018'
    y_col = 'Max Price (2018)'
    title = "Max Price for 2018"
elif selected_year == '2017':
    x_col = 'Price 2017'
    y_col = 'Max Price (2017)'
    title = "Max Price for 2017"            
elif selected_year == '2016':
    x_col = 'Price 2016'
    y_col = 'Max Price (2016)'
    title = "Max Price for 2016"
elif selected_year == '2015':
    x_col = 'Price 2015'
    y_col = 'Max Price (2015)'
    title = "Max Price for 2015"
elif selected_year == '2014':
    x_col = 'Price 2014'
    y_col = 'Max Price (2014)'
    title = "Max Price for 2014"
elif selected_year == '2013':
    x_col = 'Price 2013'
    y_col = 'Max Price (2013)'
    title = "Max Price for 2013"
elif selected_year == '2012':
    x_col = 'Price 2012'
    y_col = 'Max Price (2012)'
    title = "Max Price for 2012"
elif selected_year == '2011':
    x_col = 'Price 2011'
    y_col = 'Max Price (2011)'
    title = "Max Price for 2011"                    
elif selected_year == '2010':
    x_col = 'Price 2010'
    y_col = 'Max Price (2010)'
    title = "Max Price for 2010" 
elif selected_year == '2009':
    x_col = 'Price 2009'
    y_col = 'Max Price (2009)'
    title = "Max Price for 2009" 
elif selected_year == '2008':
    x_col = 'Price 2008'
    y_col = 'Max Price (2008)'
    title = "Max Price for 2008" 
elif selected_year == '2007':
    x_col = 'Price 2007'
    y_col = 'Max Price (2007)'
    title = "Max Price for 2007" 
elif selected_year == '2006':
    x_col = 'Price 2006'
    y_col = 'Max Price (2006)'
    title = "Max Price for 2006" 
else:
    x_col = 'Price 2020'
    y_col = 'Max Price (2020)'
    title = "Max Price for 2020"
# Plot the selected year's graph
#plt.figure(figsize=(30, 130),dpi=500)
#plt.plot(df[x_col], df[y_col], label='Max Price', color='blue', marker='o')
register_matplotlib_converters()
plt.figure(figsize=(12, 6), dpi=300)
plt.bar(df[x_col],df[y_col], color='blue', alpha=1, edgecolor='black')

x_values = df['Price 2023'].tolist()

plt.xlabel('Month')
plt.ylabel('Max Price')
plt.title('mp')
plt.xticks(rotation=45)
#plt.legend()
plt.grid(True)

st.pyplot(plt)
