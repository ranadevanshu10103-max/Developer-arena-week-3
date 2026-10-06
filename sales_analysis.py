import pandas as pd

# Load the sales dataset
df = pd.read_csv("sales_data.csv")

# Display the first few rows
print(df.head())

# Check the number of rows and columns
print(df.shape)

# Display column names
print(df.columns)

# Display basic information and data types
df.info()

# Check for missing values
print(df.isnull().sum())

# Check for duplicate rows
print("Duplicate rows:", df.duplicated().sum())

# Calculate total sales
total_sales = df["Total_Sales"].sum()
print("Total Sales:", total_sales)

# Calculate average sales
average_sales = df["Total_Sales"].mean()
print("Average Sales:", average_sales)

# Find the highest sale
highest_sale = df["Total_Sales"].max()
print("Highest Sale:", highest_sale)

# Find the lowest sale
lowest_sale = df["Total_Sales"].min()
print("Lowest Sale:", lowest_sale)

# Find the best-selling product
best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()
print("Best-Selling Product:", best_product)

# Display a clean formatted sales report
print("\n" + "=" * 40)
print("       SALES DATA ANALYSIS REPORT")
print("=" * 40)
print(f"Total Sales          : {total_sales:,.2f}")
print(f"Average Sales        : {average_sales:,.2f}")
print(f"Highest Sale         : {highest_sale:,.2f}")
print(f"Lowest Sale          : {lowest_sale:,.2f}")
print(f"Best-Selling Product : {best_product}")
print("=" * 40)
