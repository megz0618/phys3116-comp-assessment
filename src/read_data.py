# Run this file from phys3116-comp-assessment directory
import csv

# Imported and printed HarrisPartI.csv file to check proper read
# https://www.pythontutorial.net/python-basics/python-read-csv-file/
with open('data/HarrisPartI.csv', 'r') as harrisP1_file: # 'r' for read-only import
    harrisP1_reader = csv.reader(harrisP1_file)
    for line in harrisP1_reader:
        print(line)
harrisP1_file.close() # Closes file after use

# Imported and printed HarrisPartIII.csv file to check proper read
# Imported and printed Krause21.csv file to check proper read
# Imported and printed vandenBerg_table2.csv file to check proper read
