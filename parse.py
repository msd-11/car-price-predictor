import csv

def delete_rows(file, column, value):
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
    with open(file, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in rows:
            if row[column] != value:
                writer.writerow(row)

file = input("Enter the name of the .csv file: ")
column = int(input("Enter the index of the column to check (0-indexed): "))
value = input("Enter the value to check for: ")
delete_rows(file, column, value)
