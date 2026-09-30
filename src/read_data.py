# Run this file from phys3116-comp-assessment directory
import csv

# Imported and printed HarrisPartI.csv file to check proper read
# https://www.pythontutorial.net/python-basics/python-read-csv-file/
with open('data/HarrisPartI.csv', 'r') as HarrisPartI: # 'r' for read-only import
    csv_reader = csv.reader(HarrisPartI)
    for line in csv_reader:
        print(line)

HarrisPartI.close() # Closes file after use

