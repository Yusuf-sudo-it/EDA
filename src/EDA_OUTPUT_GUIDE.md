# Example EDA Outputs – Step-by-Step Guide

This document outlines the types of outputs to expect at each stage of Exploratory Data Analysis (EDA) and explains how to interpret them.

## 📋 Table of Contents

1. [Dataset Overview Outputs](#1-dataset-overview-outputs)
2. [Categorical Variable Analysis Outputs](#2-categorical-variable-analysis-outputs)
3. [Target Variable Profiling Outputs](#3-target-variable-profiling-outputs)
4. [YData Profiling Report Outputs](#4-ydata-profiling-report-outputs)

---

## 1. Dataset Overview Outputs

### 1.1 Dataset Shape
```
Number of rows: 32,561
Number of columns: 15
Total cells: 488,415
```
**Interpretation:** Shows the overall size of your dataset. This informs you about whether you have enough data for analysis and modeling.

### 1.2 Data Types
```
age                int64
workclass         object
fnlwgt             int64
education         object
...
```
**Interpretation:** Lists the data types for each column. Helps distinguish between numerical (int64, float64) and categorical (object) variables.

### 1.3 Missing Values Analysis
```
Columns with missing values:
Column          Missing Count  Missing Percentage
occupation           1843                   5.66
workclass            1836                   5.63
native.country        583                   1.79

Total missing cells: 4,262
Total missing percentage: 0.87%
```
**Interpretation:**
- Shows which columns have missing values and their proportions
- If the proportion is greater than 5%, pay special attention
- You must define a missing value handling strategy (removal, imputation, etc.)

### 1.4 Duplicate Rows
```
Number of duplicate rows: 24
Duplicate percentage: 0.07%
```
**Interpretation:** 
- Indicates the number and proportion of duplicate records
- A high number may signal data quality issues
- Under 1% is generally considered acceptable

### 1.5 Basic Statistics (Numerical Columns)
```
              age      fnlwgt  education.num  capital.gain  capital.loss  hours.per.week
count  32561.0000  32561.0000    32561.0000    32561.0000   32561.0000     32561.0000
mean      38.5816  189778.3665       10.0807     1077.6488     87.3038        40.4375
std       13.6405  105549.9777        2.5727     7385.2921    402.9602        12.3474
min       17.0000   12285.0000        1.0000        0.0000      0.0000         1.0000
25%       28.0000  117827.0000        9.0000        0.0000      0.0000        40.0000
50%       37.0000  178356.0000       10.0000        0.0000      0.0000        40.0000
75%       48.0000  237051.0000       12.0000        0.0000      0.0000        45.0000
max       90.0000  1484705.0000      16.0000    99999.0000   4356.0000        99.0000
```
**Interpretation:**
- **count:** Number of non-missing observations
- **mean:** Average value
- **std:** Standard deviation (measure of variance)
- **min/max:** Minimum and maximum values
- **25%, 50%, 75%:** Quartiles (median = 50%)

---

## 2. Categorical Variable Analysis Outputs

### 2.1 Value Counts
```
1. WORKCLASS
Value counts:
Private             22696
Self-emp-not-inc     2541
Local-gov            2093
State-gov            1298
Self-emp-inc         1116
Federal-gov           960
Without-pay            14
Never-worked            7

Value counts (%):
Private: 22,696 (69.70%)
Self-emp-not-inc: 2,541 (7.80%)
...
```
**Interpretation:**
- Shows frequency for each category
- Helps assess whether categories are balanced
- Watch out for rare categories (very low counts)

### 2.2 Statistics
```
Statistics:
  Unique values: 8
  Missing values: 1836 (5.63%)
  Most frequent: Private
```
**Interpretation:**
- **Unique values:** Number of categories (lots of categories may make encoding harder)
- **Missing values:** Count and percent of missing data
- **Most frequent:** Most common category (mode)

---

## 3. Target Variable Profiling Outputs

### 3.1 Target Variable Distribution
```
1. TARGET VARIABLE DISTRIBUTION
income Distribution:
<=50K    24720
>50K      7841

income Distribution (%):
<=50K    75.92%
>50K     24.08%
```
**Interpretation:**
- **Class Imbalance:** Is the target variable unbalanced?
- In this example, 75.92% vs 24.08% → **Imbalanced dataset**
- This must be accounted for in modeling (SMOTE, class weights, etc.)

### 3.2 Numerical Features vs Target
```
age:
        <=50K        >50K
count  24720.0    7841.0
mean     36.78     44.25
std      14.02     10.52
min      17.00     19.00
25%      25.00     36.00
50%      34.00     43.00
75%      46.00     52.00
max      90.00     90.00

T-test p-value: 0.000000 (Significant)
```
**Interpretation:**
- Summary statistics for numerical features by target group
- **T-test:** Is there a statistically significant difference between groups?
  - p-value < 0.05 → **Significant** (difference exists)
  - p-value ≥ 0.05 → **Not Significant**
- In this example, older ages are significantly associated with higher income

### 3.3 Categorical Features vs Target
```
relationship:
Count:
                <=50K   >50K  All
Husband          13193   6662  19855
Not-in-family     8305    981   9286
Own-child         5068     76   5144
Unmarried         3446    410   3856
Wife              1568   1128   2696
Other-relative     981     64   1045
All              24720   7841  32561

Percentage (%):
                <=50K      >50K
Husband         66.48    84.96
Not-in-family   89.43    10.57
Own-child       98.52     1.48
...

Chi-square test p-value: 0.000000 (Significant)
```
**Interpretation:**
- **Cross-tabulation:** Distribution of the target across categories
- **Percentage:** Share of target classes within each category
  - For example, 84.96% of "Husband" are high income
- **Chi-square test:** Is there a relationship between the categorical variable and the target?
  - p-value < 0.05 → **Significant** relationship
  - In this example, "relationship" and "income" are strongly related

### 3.4 Feature Importance Ranking
```
TOP FEATURES BY IMPORTANCE (Combined Ranking):
1. relationship: 0.4523
2. marital.status: 0.4121
3. age: 0.2345
4. education.num: 0.2234
5. hours.per.week: 0.1987
6. capital.gain: 0.1543
7. occupation: 0.1421
8. sex: 0.1234
9. workclass: 0.0987
10. race: 0.0456
```
**Interpretation:**
- **Numerical features:** Use correlation coefficient (absolute value, 0 to 1)
- **Categorical features:** Use Cramér's V statistic (0 to 1)
- Interpretation:
  - 0.0 – 0.1: Very weak relationship
  - 0.1 – 0.3: Weak
  - 0.3 – 0.5: Moderate
  - 0.5 – 0.7: Strong
  - 0.7 – 1.0: Very strong
- Here, "relationship" and "marital.status" are the most important features

### 3.5 Key Insights
```
Most significant variables (strong relation with the target):
  - relationship: 0.4523
  - marital.status: 0.4121
  - age: 0.2345
  - education.num: 0.2234
  - hours.per.week: 0.1987
```
**Interpretation:**
- These are the most important features for modeling
- Use this ranking to select features if needed
- Features with low importance (e.g., race: 0.0456) may be dropped from the model

---

## 4. YData Profiling Report Outputs

### 4.1 HTML Report Structure

YData Profiling creates an interactive HTML report, e.g., `adult_report.html`.

#### 4.1.1 Overview Section
- **Dataset info:** Number of rows/columns, percent of missing values
- **Variables:** Number of numerical/categorical variables
- **Warnings:** Data quality alerts

#### 4.1.2 Variables Section
For each variable:
- **Statistics:** Basic statistics
- **Histogram:** Distribution plot
- **Common values:** Most frequent values
- **Extreme values:** Outliers

#### 4.1.3 Interactions Section
- **Scatter plots:** Relationships between numerical variables
- **Correlation matrix:** Matrix of variable correlations

#### 4.1.4 Correlations Section
- **Pearson correlation:** For numerical variables
- **Spearman correlation:** For ordinal/ranked variables
- **Kendall correlation:** For small datasets
- **Cramér's V:** For categorical variables

#### 4.1.5 Missing Values Section
- **Missing values matrix:** Visualization of missing data
- **Missing values heatmap:** Correlation of missing patterns

#### 4.1.6 Sample Section
- **First rows:** First 10 rows of the data
- **Last rows:** Last 10 rows

### 4.2 How to Interpret the Report

1. **Check the Overview:** What is the overall data quality?
2. **Review Warnings:** Are there any potential data issues?
3. **Focus on Correlations:** Which variables are related?
4. **Examine Missing Values:** Are missing patterns random or systematic?
5. **Explore Interactions:** Any unexpected relationships?

---

## 📊 General EDA Output Checklist

For every EDA project, verify that you have:

- [ ] Understood dataset size and structure
- [ ] Detected & handled missing values
- [ ] Checked for duplicate records
- [ ] Examined distributions of numerical variables
- [ ] Analyzed frequency of categorical variables
- [ ] Checked target variable distribution (class imbalance?)
- [ ] Analyzed relationship between each feature and the target variable
- [ ] Created feature importance ranking
- [ ] Reviewed correlation matrix (multicollinearity?)
- [ ] Detected outliers
- [ ] Generated and reviewed visuals/plots
- [ ] Summarized key insights

---

## 🎯 Next Steps

After completing EDA:

1. **Data Preprocessing:** Handle missing values, encode categorical variables, scale features
2. **Feature Engineering:** Create new features if needed
3. **Feature Selection:** Select the most important features
4. **Model Training:** Train the chosen machine learning models
5. **Model Evaluation:** Assess model performance

---

## 📚 References

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [YData Profiling Documentation](https://ydata-profiling.ydata.ai/)
- [Statistical Tests Guide](https://www.statstest.com/)
