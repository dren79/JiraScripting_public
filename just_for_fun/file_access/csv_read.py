import csv

with open("input/example.csv") as infile:
    reader = csv.reader(infile, delimiter=",")

    next(reader, None)

    for row in reader:
        print(row)
        print(row[0])
        print(row[1])
