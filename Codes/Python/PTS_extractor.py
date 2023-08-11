import pandas as pd

# Load the Excel file
file_path = r"EnhancedDataset.xlsx"
df = pd.read_excel(file_path)

country_name = input("Enter the country name: ")
# Filter the data based on the 'Country' column
filtered_df = df[df['Country'] == country_name]

# Select specific columns
selected_columns = ['StockCode', 'InvoiceDate', 'Supplier']
filtered_df = filtered_df[selected_columns]

# Save the filtered data to a new Excel file
output_file = r"country_name.xlsx"
filtered_df.to_excel(output_file, index=False)

print("Filtered data saved to", output_file)