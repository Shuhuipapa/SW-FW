# Import all libraries needed
import pandas as pd
import csv
import os
# define output file path
outputfile = r"C:\users\sding\PycharmProjects\SW-FW\example.csv"
ultiout = r"C:\users\sding\PycharmProjects\SW-FW\example1.csv"

#read txt file dataset
Textfile = r'C:\users\sding\PycharmProjects\SW-FW\example data.txt'
data = pd.read_csv(Textfile, sep='\t')
data = data.drop(['Line','MM/DD/YY hh:mm:ss.ms.us'], axis=1)
data = data.values
Count_row=data.shape[0]
Count_col=data.shape[1]
i = 0
list1 = []


# write responce payroll into csv file, combine mutiple lines
for i in range(0, Count_row):
        if data [i,1] != data[i,1]:
            with open(outputfile,"a") as f:
                 writer = csv.writer(f, delimiter = ',')
                 writer.writerow(list1)
            list1 = []
        else:
            s = data[i,1]
            s = s.split()
            s = [int(i, 16) for i in s]
            list1.extend(s)

# write the final line into csv file
with open(outputfile,"a") as f:
        writer = csv.writer(f, delimiter = ',')
        writer.writerow(list1)


# remove blank space in csv file
with open(outputfile) as input, open(ultiout, 'w', newline='') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)


os.remove(outputfile)