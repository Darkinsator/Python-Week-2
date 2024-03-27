# Python-Week-2
Python Week 2 breakdown

Day 1:
Learnt opening, reading and writing to text files in python.
 
Example code 
f = open('Example.txt', 'r')
print(f)

f.readline()
f.readlines()
f.close()

Python CSV READER
To write and read to a csv folder we use the import csv at the top of the python file:

import csv

with open('data.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        print(row)


JSON Files
jsonString = {"a": "apple", "b": "bear","c": "cat"}

Day 2:
Anatomy of a function
Variables and Scope
Functions as Variables
