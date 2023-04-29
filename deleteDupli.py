import csv

# Open the input and output files
with open('input.csv', 'r') as input_file, open('output.csv', 'w', newline='') as output_file:
    # Create a CSV reader and writer
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Create a set to keep track of unique rows
    unique_rows = set()

    # Iterate over the rows in the input file
    for row in reader:
        # Convert the row to a tuple
        row_tuple = tuple(row)
        # If the row is not already in the set of unique rows
        if row_tuple not in unique_rows:
            # Add the row to the set of unique rows
            unique_rows.add(row_tuple)
            # Write the row to the output file
            writer.writerow(row)

