#importing pandas as pd
import pandas as pd
  
# Read and store content
# of an excel file 
df = pd.read_excel ("C:/Users/Lars/VimDocs/testing_xlrd.xls")
  
iter_df = pd.DataFrame() 
data = {}

# show the dataframe
print(df)
for index, row in df.iterrows():
    data.clear()
    data[0] = row['Name']
    if row[3] > row['Number']:
        data[1] = "Error 1" 
        #print(data)
        #print(row['Name'])
    #print(row['Age'], row['Number'])
    if row['Name']=='Baker':
        data[2] = 'Error 2'
        print(data)
    iter_df = iter_df.append(data, ignore_index=True)

print(iter_df)
print(data)
