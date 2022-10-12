import csv

data = ["I", "love", "Python", "Hangouts"]

with open('outputs/example.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(data)
