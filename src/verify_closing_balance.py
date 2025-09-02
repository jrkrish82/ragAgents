import pandas as pd

# Load the CSV file
file_path = "cash_flow_data.csv"  # Replace with the correct path to your CSV file
data = pd.read_csv(file_path)

# Ensure numeric columns are properly converted
numeric_columns = ['Opening Balance', 'Cash In', 'Cash Out', 'Closing Balance']
data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Calculate the expected Closing Balance
data['Calculated Closing Balance'] = data['Opening Balance'] + data['Cash In'] - data['Cash Out']

# Check for mismatches
mismatches = data[data['Closing Balance'] != data['Calculated Closing Balance']]

# Output the results
if mismatches.empty:
    print("All Closing Balance values are correct.")
else:
    print("Mismatches found in Closing Balance:")
    print(mismatches[['Date', 'Branch', 'Opening Balance', 'Cash In', 'Cash Out', 'Closing Balance', 'Calculated Closing Balance']])
