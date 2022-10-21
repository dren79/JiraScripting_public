import csv
from random import randrange

with open("input/MOCK_DATA.csv") as infile:
    reader = csv.reader(infile, delimiter=",")
with open('input/MOCK_DATA.csv', 'r') as csv_input:
    with open('output/MOCK_DATA_WITH_PROJECT.csv', 'w') as csv_output:
        writer = csv.writer(csv_output, lineterminator='\n')
        reader = csv.reader(csv_input)

        new_contents = []
        row = next(reader)
        row.append('project')
        new_contents.append(row)

        for row in reader:
            projects = ['D1', 'D2', 'D3']
            row.append(projects[randrange(3)])
            new_contents.append(row)

        writer.writerows(new_contents)
