import csv
import sys

# to check if command line argument consists of 3 elements.
if len(sys.argv) != 3:
    sys.exit("Usage: python dna.py data.csv sequence.txt")

# open the csv file to know how many str you're going to search for and sotre it in integer called X
with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        x = len(row) - 1
        break

# create a list which we will contain str counts        
str = [0] * x


# open the sequences txt and read it 
with open(sys.argv[2], "r") as dnafile:
    DNA = dnafile.read()
     
for j in range(x):
    for i in range(len(DNA)):
        counter = 0
        # L is the length of str sequence you will search for.
        L = len(row[j+1])
        # to check if the str sequence is found.
        if DNA[i: i+L] == row[j+1]:
            # to counts how many times the str sequence is repeated.
            while True:
                if DNA[i: i+L] != row[j+1]:
                    counter = 0
                    break
                else:
                    counter += 1   
                    if counter > str[j]:
                        str[j] = counter
                    i = i + L

# at first time, set the result which will print out to user to "No match"
result = "No match"

# open the csv file to check if str sequences matches one of the databases
with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    row_count = 0
    counter = 0
    # go through each row in the csv file
    for row in csv_reader:
        # to skip the first row
        if row_count == 0:
            row_count += 1
        else:
            for i in range(x):
                if str[i] == int(row[i+1]):
                    counter += 1
                    if counter == x:
                        result = row[0]
                else:
                    break
            row_count += 1
            counter = 0

print(result)
