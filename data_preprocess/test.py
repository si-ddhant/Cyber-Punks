import csv

# Define the input and output file names
input_file = 'h1b.csv'
output_file = 'processed.csv'

# Define the specific columns you want to include
columns_to_include = [ "CASE_SUBMITTED", 'CASE_STATUS' ,"VISA_CLASS", "EMPLOYER_NAME", "EMPLOYER_ADDRESS", "EMPLOYER_CITY", "EMPLOYER_STATE", "EMPLOYER_POSTAL_CODE", "EMPLOYER_COUNTRY",  "EMPLOYER_PHONE", "AGENT_ATTORNEY_NAME",  "JOB_TITLE", "SOC_CODE", "SOC_NAME", "NAIC_CODE", "TOTAL_WORKERS", "PREVAILING_WAGE", "PW_UNIT_OF_PAY", "PW_WAGE_SOURCE", "PW_SOURCE_YEAR",  "WAGE_RATE_OF_PAY_FROM", "WAGE_RATE_OF_PAY_TO", "WAGE_UNIT_OF_PAY"]

# Open the input file for reading and the output file for writing
with open(input_file, 'r', newline='') as csv_in, open(output_file, 'w', newline='') as csv_out:
    reader = csv.reader(csv_in)
    writer = csv.writer(csv_out)

    # Find the column indices for the selected columns
    header = next(reader)
    column_indices = [header.index(column) for column in columns_to_include]

    # Write the header row to the output file
    writer.writerow(columns_to_include)

    # Iterate through the rows in the input file and select specific columns
    for row in reader:
        selected_row = [row[i] for i in column_indices]
        writer.writerow(selected_row)

print("New CSV file created with specific columns:", output_file)
