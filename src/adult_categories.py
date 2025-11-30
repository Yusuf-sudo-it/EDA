"""
Categorical Variables Analysis
This script analyzes the distribution and frequencies of categorical variables
in the Adult Census Income dataset.
"""

import pandas as pd
import os
import sys

# Load the data - handle different execution paths
data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'adult.data')
if not os.path.exists(data_path):
    data_path = os.path.join('data', 'adult.data')
    if not os.path.exists(data_path):
        data_path = os.path.join('..', 'data', 'adult.data')
        if not os.path.exists(data_path):
            print(f"ERROR: Dataset not found. Please make sure adult.data is in the data/ folder.")
            sys.exit(1)

# Define column names for Adult Census Income dataset
column_names = [
    'age', 'workclass', 'fnlwgt', 'education', 'education.num',
    'marital.status', 'occupation', 'relationship', 'race', 'sex',
    'capital.gain', 'capital.loss', 'hours.per.week', 'native.country', 'income'
]

# Load the data with column names
df = pd.read_csv(data_path, names=column_names, na_values='?', skipinitialspace=True)

print("=" * 80)
print("CATEGORICAL VARIABLES ANALYSIS")
print("=" * 80)

# Define categorical columns
cat_cols = ['workclass', 'education', 'education.num',
            'marital.status', 'occupation', 'relationship', 'race',
            'sex', 'native.country', 'income']

# Filter only existing columns
cat_cols = [col for col in cat_cols if col in df.columns]

print(f"\nAnalyzing {len(cat_cols)} categorical columns...")
print("-" * 80)

# Analyze each categorical column
for i, col in enumerate(cat_cols, 1):
    print(f"\n{i}. {col.upper()}")
    print("-" * 80)
    
    # Value counts
    value_counts = df[col].value_counts()
    value_counts_pct = df[col].value_counts(normalize=True) * 100
    
    print(f"\nValue counts:")
    print(value_counts)
    
    print(f"\nValue counts (%):")
    for val, count in value_counts.items():
        pct = value_counts_pct[val]
        print(f"  {val}: {count:,} ({pct:.2f}%)")
    
    # Additional statistics
    print(f"\nStatistics:")
    print(f"  Unique values: {df[col].nunique()}")
    print(f"  Missing values: {df[col].isna().sum()} ({(df[col].isna().sum() / len(df)) * 100:.2f}%)")
    print(f"  Most frequent: {df[col].mode().iloc[0] if len(df[col].mode()) > 0 else 'N/A'}")

print("\n" + "=" * 80)
print("Categorical analysis completed!")
print("=" * 80)
