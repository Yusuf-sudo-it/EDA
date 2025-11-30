"""
Dataset Overview Analysis
This script analyzes the general characteristics of the Adult Census Income dataset:
- Dataset size and structure
- Data types
- Missing values analysis
- Duplicate records check
"""

import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv('data/adult.data', na_values='?')

print("=" * 80)
print("ADULT CENSUS INCOME DATASET - OVERVIEW ANALYSIS")
print("=" * 80)

# 1. Dataset Shape
print("\n1. DATASET SHAPE")
print("-" * 80)
print(f"Number of rows: {df.shape[0]:,}")
print(f"Number of columns: {df.shape[1]}")
print(f"Total cells: {df.size:,}")

# 2. Data Types
print("\n\n2. DATA TYPES")
print("-" * 80)
print("\nData types summary:")
print(df.dtypes)
print(f"\nNumerical columns: {len(df.select_dtypes(include=[np.number]).columns)}")
print(f"Categorical columns: {len(df.select_dtypes(include=['object']).columns)}")

# 3. First Few Rows
print("\n\n3. FIRST 5 ROWS")
print("-" * 80)
print(df.head())

# 4. Column Names
print("\n\n4. COLUMN NAMES")
print("-" * 80)
print("\nColumns:")
for i, col in enumerate(df.columns, 1):
    print(f"  {i}. {col}")

# 5. Missing Values Analysis
print("\n\n5. MISSING VALUES ANALYSIS")
print("-" * 80)
missing = df.isna().sum()
missing_pct = (missing / len(df)) * 100
missing_df = pd.DataFrame({
    'Column': missing.index,
    'Missing Count': missing.values,
    'Missing Percentage': missing_pct.values
})
missing_df = missing_df[missing_df['Missing Count'] > 0].sort_values('Missing Count', ascending=False)

if len(missing_df) > 0:
    print("\nColumns with missing values:")
    print(missing_df.to_string(index=False))
else:
    print("\nNo missing values found!")

total_missing = df.isna().sum().sum()
total_missing_pct = round((total_missing / df.size) * 100, 2)
print(f"\nTotal missing cells: {total_missing:,}")
print(f"Total missing percentage: {total_missing_pct}%")

# 6. Duplicate Rows
print("\n\n6. DUPLICATE ROWS")
print("-" * 80)
duplicated_count = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicated_count}")
if duplicated_count > 0:
    print(f"Duplicate percentage: {round((duplicated_count / len(df)) * 100, 2)}%")
    print("\nSample duplicate rows:")
    print(df[df.duplicated()].head())

# 7. Basic Statistics for Numerical Columns
print("\n\n7. BASIC STATISTICS (NUMERICAL COLUMNS)")
print("-" * 80)
numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
if len(numerical_cols) > 0:
    print(df[numerical_cols].describe())
else:
    print("No numerical columns found!")

# 8. Summary
print("\n\n8. SUMMARY")
print("-" * 80)
print(f"✓ Dataset loaded successfully")
print(f"✓ Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"✓ Missing values: {total_missing:,} ({total_missing_pct}%)")
print(f"✓ Duplicate rows: {duplicated_count}")
print(f"✓ Numerical features: {len(numerical_cols)}")
print(f"✓ Categorical features: {len(df.select_dtypes(include=['object']).columns)}")

print("\n" + "=" * 80)
print("Analysis completed!")
print("=" * 80)
