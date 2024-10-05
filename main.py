# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Set Data Analyst's name
data_analyst_name = 'Shazil Shahid'

# Load the dataset (replace 'sales_data.csv' with your actual dataset file path)
data = pd.read_csv('sales_data.csv')

# Display first few rows of the dataset
print("Dataset Head:")
print(data.head())

# 1. Data Cleaning: Remove missing values (if any)
data.dropna(inplace=True)

# 2. Add a new column 'TotalSales' (Price * Quantity)
data['TotalSales'] = data['Price'] * data['Quantity']

# 3. Calculate total sales per customer
customer_sales = data.groupby('CustomerID')['TotalSales'].sum().reset_index()
customer_sales.columns = ['CustomerID', 'TotalSales']

# 4. Analyze sales trends over time (group by month or day)
# Convert 'OrderDate' to datetime
data['OrderDate'] = pd.to_datetime(data['OrderDate'])

# Extract year and month
data['YearMonth'] = data['OrderDate'].dt.to_period('M')

# Calculate total sales per month
monthly_sales = data.groupby('YearMonth')['TotalSales'].sum().reset_index()

# --- First Window: Monthly Sales (Line Chart) ---
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales['YearMonth'].astype(str), monthly_sales['TotalSales'], marker='o', color='green', linestyle='-', linewidth=2)
plt.title(f'Monthly Sales Trend Analyzed by {data_analyst_name}', fontsize=14, fontweight='bold')
plt.xlabel('Year-Month', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# --- Second Window: Total Sales per Customer (Bar Chart) ---
plt.figure(figsize=(10, 6))
bars = plt.bar(customer_sales['CustomerID'], customer_sales['TotalSales'], color=plt.cm.Blues(customer_sales['TotalSales'] / customer_sales['TotalSales'].max()), edgecolor='black')
plt.title(f'Total Sales per Customer by {data_analyst_name}', fontsize=14, fontweight='bold')
plt.xlabel('CustomerID', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.xticks(rotation=90)

# Annotating the bar chart with total sales values
for i, total in enumerate(customer_sales['TotalSales']):
    plt.text(i, total + 100, f'{total:.2f}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

# --- Third Window: CSV Data Table (First 10 Rows) ---
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('tight')
ax.axis('off')

# Display only the first 10 rows of the data in a table format
table_data = data.head(10).values
columns = data.columns
table = ax.table(cellText=table_data, colLabels=columns, cellLoc='center', loc='center')

# Adjust layout and show the table
plt.title(f'CSV Data Information (First 10 Rows) by {data_analyst_name}', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
