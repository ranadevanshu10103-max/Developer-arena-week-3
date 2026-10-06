# Sales Data Analysis Report

## 1. Project Overview

This project analyzes a sales dataset using Python and Pandas.

The main objective is to explore the dataset, check data quality, calculate important sales metrics, identify the best-selling product, and create a clean sales report.

## 2. Dataset Information

The dataset contains 100 rows and 7 columns.

Columns:
- Date
- Product
- Quantity
- Price
- Customer_ID
- Region
- Total_Sales

## 3. Tools and Technologies

- Python
- Pandas
- CSV
- IDLE

## 4. Data Loading

The dataset was loaded using the Pandas library.

```python
import pandas as pd
df = pd.read_csv("sales_data.csv")

## 5. Data Exploration

The following Pandas functions were used to explore the dataset:
- head() - displays the first five rows
- shape - shows the number of rows and columns
- columns - displays column names
- info() - displays data types and basic information
The dataset contains 100 rows and 7 columns.

## 6. Data Cleaning
Missing values were checked using:
df.isnull().sum()

All columns contained 0 missing values.
Duplicate rows were checked using:
df.duplicated().sum()

he dataset contained 0 duplicate rows.
Therefore, no records needed to be removed.

## 7. Sales Analysis
The following metrics were calculated:

Total Sales
12,365,048

Average Sales
123,650.48

Highest Sale
373,932

Lowest Sale
6,540

Best-Selling Product
Laptop

## 8. Key Findings
- Total sales were 12,365,048.
- Average sales were 123,650.48.
- The highest individual sale was 373,932.
- The lowest individual sale was 6,540.
- Laptop was identified as the best-selling product based on total sales.

## 9. Clean Formatted Report
The Python program displays the final analysis in a formatted report containing:
- Total Sales
- Average Sales
- Highest Sale
- Lowest Sale
- Best-Selling Product

## 10. Conclusion
This project demonstrates how Python and Pandas can be used to load, explore, clean, and analyze sales data.
The analysis successfully identified important sales metrics and the best-selling product from the dataset.


### ⚠️ Important
Paste karne ke baad **Ctrl + S** karo.

Phir mujhe **`analysis_report.md` ka screenshot** bhej dena. Main check karunga ki formatting/content sahi hai, uske baad next **GitHub upload** karenge.