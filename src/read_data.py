# Run this file from phys3116-comp-assessment directory
import csv

# Imported and printed HarrisPartI.csv file to check proper read
# https://www.pythontutorial.net/python-basics/python-read-csv-file/
with open('data/HarrisPartI.csv', 'r') as harrisP1_file: # 'r' for read-only import
    harrisP1_reader = csv.reader(harrisP1_file)
    for line in harrisP1_reader:
        print(line)
harrisP1_file.close() # Closes file after use

#Imported and printed HarrisPartIII.cvs file to check proper read
with open('data/HarrisPartIII.csv', 'r') as harrisP3_file: # 'r' for read-only import
    harrisP3_reader = csv.reader(harrisP3_file)
    for line in harrisP3_reader:
        print(line)
harrisP3_file.close() # Closes file after use

# Imported and printed Krause21.csv file to check proper read
with open('data/Krause21.csv', 'r') as krause21_file: # 'r' for read-only import
    krause21_reader = csv.reader(krause21_file)
    for line in krause21_reader:
        print(line)
krause21_file.close() # Closes file after use

# Imported and printed vandenBerg_table2.csv file to check proper read
with open('data/vandenBerg_table2.csv', 'r') as vandenBerg_file: # 'r' for read-only import
    vandenBerg_reader = csv.reader(vandenBerg_file)
    for line in vandenBerg_reader:
        print(line)
vandenBerg_file.close() # Closes file after use
