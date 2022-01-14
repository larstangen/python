#importing pandas as pd
import pandas as pd
  
# Read and store content
# of an excel file 
df = pd.read_excel ("C:/Users/Lars/VimDocs/testing_xlrd.xls")
  
  
# show the dataframe
print(df)

for index, row in df.iterrows():
    if row[3] > row['Number']:
        print(row['Name'])
    #print(row['Age'], row['Number'])


#print(df.Title)
#print (Name[1])
#print(df.loc[1])

# for i in number of rows - check if column x is > y
# print Name where Age > Number


## Conversion to CSV steps that are not needed...yet
# Write the dataframe object
# into csv file
#read_file.to_csv ("Test.csv", 
                  #index = None,
                  #header=True)
    
# read csv file and convert 
# into a dataframe object
#df = pd.DataFrame(pd.read_csv("Test.csv"))
