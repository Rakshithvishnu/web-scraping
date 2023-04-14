#importing csv file using pandas
import pandas as pd
import sqlite3
df = pd.read_csv("14042023_verge.csv")

#printing csv file
#print(my_file)i

#create the database and connect to database
conDB = sqlite3.connect('VergeDB.db')
curr = conDB.cursor()

#create a table
curr.execute('CREATE TABLE IF NOT EXISTS VergeTable (id INTEGER, Url TEXT, Headline TEXT, Author TEXT, Date TEXT)')

#commit the query
conDB.commit()

#using to_sql() function to write to the database
df.to_sql('VergeTable', con=conDB, if_exists='replace', index=False, index_label='id', dtype = {'id': 'PRIMARY KEY'})

#Query data from database
#using pd.read_sql
readAllData = pd.read_sql('select * from VergeTable', con=conDB)
print(readAllData)

print('\n')

#sql queries with condition
selectAuthor = pd.read_sql('select * from VergeTable where author="James Vincent"', con=conDB)
print(selectAuthor)

print('\n')

#SetIdPrimaryKey = pd.read_sql('alter table VergeTable ADD PRIMARY KEY (id)', con=conDB)
#print(SetIdPrimaryKey)

