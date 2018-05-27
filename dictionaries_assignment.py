#item = ["Football","Basketball","Shorts","Bats"]
#userchoice = {"item": "Football","Basketball","Shorts","Bats"}
#print(item)
#userchoice = input("Do you want to add more items?: ")  

#while (choice == "Yes"):
 #   order = input([userchoice])
  #  print("Superb your " + order + " will be ready")
   # choice = input("Do you want more? ")



import os
import csv
# Set path for file
csvpath = os.path.join("Resources", "store_items.csv")
# Open the CSV
with open(csvpath, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   # create a dictory
   d = {}
   for row in csvreader:
      d[row[0]] = row[1:]

   for i in d:
       print(i, d[i])