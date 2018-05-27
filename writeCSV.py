import os
import csv
output_path = os.path.join('Assignment 1','udemy_csv.csv')
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['1010101010', 'Abhinav is testing this again', 'http://test', ])