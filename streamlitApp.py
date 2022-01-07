import streamlit as st
import pandas as pd
import numpy as np
st.title('Streamlit app assesment')


import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="streamlit"
)

mycursor = db.cursor()

mycursor.execute("select Country from `2015` ")
all_countries = mycursor.fetchall()
mycursor.execute("select Region from `2015` ")
all_regions = mycursor.fetchall()

user_country = st.selectbox("rank change", [x[0] for x in all_countries])



result = []

#sql = "select * from `2015` union all select * from `2016` union all select * from `2017` "


    
try:
    mycursor.execute("select `Happiness Rank` from `2015` where Country = %s ", (user_country,))
    result.append(mycursor.fetchall())
    mycursor.execute("select `Happiness Rank` from `2016` where Country = %s ", (user_country,))
    result.append(mycursor.fetchall())
    mycursor.execute("select `Happiness.Rank` from `2017` where Country = %s ", (user_country,))
    result.append(mycursor.fetchall())
    mycursor.execute("select `Overall rank` from `2018` where `Country or region` = %s ", (user_country,))
    result.append(mycursor.fetchall())
    mycursor.execute("select `Overall rank` from `2019` where `Country or region` = %s ", (user_country,))
    result.append(mycursor.fetchall())
    
except:
    db.rollback()

if len(result) != 0 and user_country != "":
    year = 2015
    for all in result:
        st.write(year, ': ', all[0][0])
        year += 1

user_region = st.selectbox("average region rank change",[x[0] for x in all_regions])

total =0
avg_2015 =0
avg_2016=0

try:
    mycursor.execute("select `Happiness Rank` from `2015` where Region = %s ", (user_region,))
    data = mycursor.fetchall()
    for country in data:
        total = total + country[0]
    avg_2015 = total/len(data)

    total = 0

    mycursor.execute("select `Happiness Rank` from `2016` where Region = %s ", (user_region,))
    for country in mycursor:
        total = total + country[0]
    avg_2016 = total/mycursor.len()
    
except:
    db.rollback()


diff = avg_2015-avg_2016
st.write(diff)