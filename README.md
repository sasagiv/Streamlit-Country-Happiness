# Streamlit-Country-Happiness

This web application was made as an assessment.

I first began by importing the database from kaggle into mySQL Workbench. I later worked on each query assigned individually in my IDE of choice- visual studios code, in which I connected to the database in mySQL workbench using mysql.connector.

On the first assignment: rank change, I implemented the query by having a result array that will append for each year (all tables in my database). Next I implemented the rank change assignment, in which I added all the scores of countries in a given region, and divided by the number of countries in that region. This was done for both tables 2015 and 2016 in my data table since between the years 2017-2019 no data on a country's region was stated. I then subtracted the average rank of 2016 from 2015 to get the difference of change between the two years.

Lastly, I used Streamlit to create a very basic web application on my local machine. I imported both queries I previously wrote and changed their inputs and outputs so they will be able to be functionally used through the web application.
