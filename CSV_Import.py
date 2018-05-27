import csv
import os
#csvreader = CSV_IMPORT/netflix_ratings.csv
with open(udemy_csv.csv, newline= '') as csvreader:
    csvreader = csv.reader(udemy_csv.csv, delimiter=',')
        #print the file formt he CSV
 print (csvreader)

    for row in csvreader:
        print(row)
