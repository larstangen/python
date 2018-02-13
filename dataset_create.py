import csv
f = open("nfl_suspensions_data.csv", "r")
nfl_suspensions = list(csv.reader(f))
nfl_suspensions = nfl_suspensions[1:len(nfl_suspensions)]
years = {}
for row in nfl_suspensions:
    row_year = row[5]
    if row_year in years:
        years[row_year] += 1
    else:
        years[row_year] = 1
print(years)
#print(nfl_suspensions[:2])

#class Dataset:
#    def __init__(self, data):
#        self.header = data[0]
#        self.data = data[1:]
#    
#    def column(self, label):
#        if label not in self.header:
#            return None
#        
#        index = 0
#        for idx, element in enumerate(self.header):
#            if label == element:
#                index = idx
#        
#        column = []
#        for row in self.data:
#            column.append(row[index])
#        return column
#
#    def count_unique(self, label):
#        count = set(self.column(label)
#
#nfl_dataset = Dataset(nfl_data)
#year_column = nfl_dataset.column('year')
#print(year_column)
#player_column = nfl_dataset.column('player')
#
#
##class Dataset:
##    def __init__(self, data):
##        self.data = data
##    def print_data(self, num_rows):
##        print(self.data[:num_rows])
##    # Your method goes here
##nfl_dataset = Dataset(nfl_data)
##dataset_data = nfl_dataset.data
##nfl_dataset.print_data(5)
##
