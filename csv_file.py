import csv
with open('test.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for element in spamreader:
        print(element)
        