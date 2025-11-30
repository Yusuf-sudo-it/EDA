"""
Y-Profiling Analysis: Target Variable (Income) Profiling
This script analyzes the relationships between the target variable (income)
and other variables, and identifies which features have the strongest
impact on income level.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the data
df = pd.read_csv('data/adult.csv', na_values='?')

# Target variable
target = 'income'

print("=" * 80)
print("Y-PROFILING ANALYSIS: TARGET VARIABLE (INCOME) ANALYSIS")
print("=" * 80)

# 1. Target Variable Distribution
print("\n1. TARGET VARIABLE DISTRIBUTION")
print("-" * 80)
target_dist = df[target].value_counts()
target_dist_pct = df[target].value_counts(normalize=True) * 100
print(f"\n{target} Distribution:")
print(target_dist)
print(f"\n{target} Distribution (%):")
print(target_dist_pct.round(2))

# 2. Numerical Features vs Target
print("\n\n2. NUMERICAL FEATURES vs TARGET")
print("-" * 80)
numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
numerical_cols = [col for col in numerical_cols if col != 'fnlwgt']  # fnlwgt is usually excluded from analysis

print("\nNumerical Features Statistical Summary by Income:")
for col in numerical_cols:
    print(f"\n{col}:")
    summary = df.groupby(target)[col].describe()
    print(summary)
    
    # Statistical test (t-test for means)
    group1 = df[df[target] == df[target].unique()[0]][col].dropna()
    group2 = df[df[target] == df[target].unique()[1]][col].dropna()
    t_stat, p_value = stats.ttest_ind(group1, group2)
    print(f"  T-test p-value: {p_value:.6f} ({'Significant' if p_value < 0.05 else 'Not Significant'})")

# 3. Categorical Features vs Target
print("\n\n3. CATEGORICAL FEATURES vs TARGET")
print("-" * 80)
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
categorical_cols = [col for col in categorical_cols if col != target]

print("\nCategorical Features Cross-tabulation with Income:")
for col in categorical_cols:
    print(f"\n{col}:")
    crosstab = pd.crosstab(df[col], df[target], margins=True)
    crosstab_pct = pd.crosstab(df[col], df[target], normalize='index') * 100
    print("\nCount:")
    print(crosstab)
    print("\nPercentage (%):")
    print(crosstab_pct.round(2))
    
    # Chi-square test
    contingency_table = pd.crosstab(df[col], df[target])
    chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
    print(f"\n  Chi-square test p-value: {p_value:.6f} ({'Significant' if p_value < 0.05 else 'Not Significant'})")

# 4. Feature Importance Ranking (Correlation with Target)
print("\n\n4. FEATURE IMPORTANCE RANKING")
print("-" * 80)

# For numerical features: correlation
print("\nNumerical Features Correlation with Target:")
target_encoded = df[target].map({df[target].unique()[0]: 0, df[target].unique()[1]: 1})
correlations = {}
for col in numerical_cols:
    corr = df[col].corr(target_encoded)
    correlations[col] = abs(corr)
    print(f"  {col}: {corr:.4f}")

# For categorical features: Cramér's V
print("\nCategorical Features Cramér's V with Target:")
cramers_v = {}
for col in categorical_cols:
    contingency_table = pd.crosstab(df[col], df[target])
    chi2, _, _, _ = stats.chi2_contingency(contingency_table)
    n = contingency_table.sum().sum()
    cramers_v_value = np.sqrt(chi2 / (n * (min(contingency_table.shape) - 1)))
    cramers_v[col] = cramers_v_value
    print(f"  {col}: {cramers_v_value:.4f}")

# Combined ranking
print("\n\nTOP FEATURES BY IMPORTANCE (Combined Ranking):")
all_importances = {**correlations, **cramers_v}
sorted_importances = sorted(all_importances.items(), key=lambda x: x[1], reverse=True)
for i, (feature, importance) in enumerate(sorted_importances[:10], 1):
    print(f"  {i}. {feature}: {importance:.4f}")

# 5. Key Insights
print("\n\n5. KEY INSIGHTS")
print("-" * 80)
print("\nVariables with highest significance (Strong relationship with Target):")
top_features = sorted_importances[:5]
for feature, importance in top_features:
    print(f"  - {feature}: {importance:.4f}")

print("\n\nAnalysis completed! Check the output above for detailed insights.")
print("=" * 80)

