import numpy as np
import pandas as pd

msg = "pandas single-dimentional: series object ,  multi-dimentional: DataFrame"
print(msg)
msg1 = "\nSeries object"
s1 = pd.Series([1, 2, 3, 4, 5])
print(msg1)
print(s1)

msg2 = "\ninstead of 0,1,2,3 index . I want a,b,c,d index"
print(msg2)
s1 = pd.Series(data=[1, 2, 3, 4, 5],
               index=['a', 'b', 'c', 'd', 'e'])  # length of index & data must be same
print(s1)
print("Describe Series Object Dataframe")
print(s1.describe())

msg3 = "\nSeries Object from dictionary"
print(msg3)
s2 = pd.Series({'abul': 300, 'babul': 500, 'masum': 400, 'dishum': 900})
print(s2)
print("changing index position of dictionary Objects in pandas")
s3 = pd.Series(data={'abul': 300, 'babul': 500, 'masum': 400, 'dishum': 900},
               index=['dishum', 'abul', 'babul', 'masum'])
print(s3)

msg4 = "\nExtracting individual elements"
print(msg4)
s4 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
s5 = pd.Series([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(s4[:])
print(s4[:-2])

msg5 = "\nBasic Math Operations"
print('adding scaler value')
print(s4+5)
print('adding two series objects')
print(s4+s5)

msg6 = "\nDataFrames is 2-Dimentional data structiure"
print(msg6)
df1 = pd.DataFrame(data={'name':["Abdullah","Masum","Mollah"],'marks':[50,90,60]})
print(df1)

msg7 = "\nDataFrames Built-in Functions\nhead()\ttail()\tshape()\tdescribe"
print(msg7)
my_file = pd.read_csv('Amazons_bamboo_for_pandas.csv')
print("this will give first 5 recorda in dataframe")
print(my_file.head())
print("this will give last 5 records in dataframe")
print(my_file.tail())
print("this will show How many rows & colums present in dataframes")
print(my_file.shape)
print(type(my_file.shape))
x = my_file.shape
print(f"total rows present : {x[0]} \ntotal column present : {x[1]}")
print(my_file.describe())

msg8 = "\nExtract exact number of rows & columns data: using iloc()"
print(msg8)
print("i have printed 1st 3 rows and colums of high & low's data")
print(my_file.iloc[0:3,2:4])
print("\nNow i want to extract data using column name: using loc()")
print(my_file.loc[20:25,('High','Low','Date')]) # row 20~25 & colums are high,low,date

msg9 = "\nNow I want to drop any columns of my csv file"
print(msg9)
my_file = my_file.drop(columns='Volume',axis=1) # axis:1 means columns
print("After droping. Total columns :",my_file.shape[1])
arr = np.arange(100,200)
my_file = my_file.drop(arr,axis=0) # axis:0 means rows
print("After droping. Total rows :",my_file.shape[0])

msg10 = "\nSome useful funtions in pandas"
print(msg10)
print("mean of my csv file for each column :\n",my_file.mean())
print("median of my csv file for each column :\n",my_file.median())
print("Standard_Deviation of my csv file for each column :\n",my_file.std())

def dhoka(s):
    return s*2
print("Now i want to fool clients by increasing price of High & Low columns :')")
my_file= my_file[['High','Low']].apply(dhoka)
print(my_file)

print("\nNow i want to sort my values according to specific columns data")
my_file = my_file.sort_values(by='High') # column wise sort of value according to High column
print(my_file)

