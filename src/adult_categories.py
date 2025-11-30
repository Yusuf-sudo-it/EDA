"""
Categorical Variables Analysis
This script analyzes the distribution and frequencies of categorical variables
in the Adult Census Income dataset.
"""

import pandas as pd

# Load the data
df = pd.read_csv('data/adult.data', na_values='?')

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
