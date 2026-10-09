import pandas as pd

file = r"D:\Data Analytics\APEX PLANET Internship\Task_1_Final.xlsx"

df = pd.read_excel(file)

print("Rows and Columns:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

# Missing Value Handling

df["Age"] = df["Age"].fillna(df["Age"].median())
df["City"] = df["City"].fillna("Unknown")

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Duplicate Check

print("\nDuplicate Rows Before Cleaning:", df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicate Rows After Cleaning:", df.duplicated().sum())

# Date Conversion

df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

print("\nOrder_Date Data Type:")
print(df["Order_Date"].dtype)

# Text Cleaning

text_columns = ["Customer_Name", "Gender", "City", "Product", "Category"]

for col in text_columns:
    df[col] = df[col].str.strip()

print("\nText Cleaning Completed.")

# Total Sales Validation

df["Calculated_Sales"] = df["Quantity"] * df["Unit_Price"]

df["Sales_Check"] = (
    df["Calculated_Sales"].round(2) == df["Total_Sales"].round(2)
)

print("\nSales Validation:")
print(df["Sales_Check"].value_counts())


# Outlier Detection

numeric_columns = ["Age", "Quantity", "Unit_Price", "Total_Sales"]

for col in numeric_columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = ((df[col] < lower_limit) | (df[col] > upper_limit)).sum()

    print(f"{col}: {outliers} outliers")
    
    # Remove Temporary Validation Columns
    
df = df.drop(columns=["Calculated_Sales", "Sales_Check"])

print("\nTemporary validation columns removed.")
print("\nFinal Columns:")
print(df.columns.tolist())

# Save Cleaned Data

output_file = r"D:\Data Analytics\APEX PLANET Internship\Cleaned_Data.xlsx"

df.to_excel(output_file, index=False)

print("\nCleaned data saved successfully.")
print(output_file)