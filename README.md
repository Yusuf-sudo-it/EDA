# Adult Census Income - Exploratory Data Analysis (EDA) Portfolio

This project contains a comprehensive Exploratory Data Analysis (EDA) study on the Adult Census Income dataset. The project includes detailed dataset analysis, target variable profiling, and ydata profiling report generation.

## 📊 About the Dataset

**Adult Census Income Dataset** (UCI Machine Learning Repository)
- **Number of Records**: 32,561
- **Number of Features**: 15 (14 features + 1 target)
- **Target Variable**: `income` (>50K or <=50K)
- **Missing Values**: Some categorical variables contain missing values marked as '?'

### Features

**Numerical Features:**
- `age`: Age
- `fnlwgt`: Final weight (population weight)
- `education.num`: Education level (numerical)
- `capital.gain`: Capital gain
- `capital.loss`: Capital loss
- `hours.per.week`: Hours worked per week

**Categorical Features:**
- `workclass`: Work class
- `education`: Education level
- `marital.status`: Marital status
- `occupation`: Occupation
- `relationship`: Relationship status
- `race`: Race
- `sex`: Sex
- `native.country`: Native country
- `income`: Income level (target variable)

## 📁 Project Structure

```
.
├── data/
│   └── adult.csv              # Dataset (not included in project)
├── adult_dataset_overview.py   # Dataset overview analysis
├── adult_categories.py         # Categorical variables analysis
├── adult_y_profiling.py        # Target variable (Y) profiling analysis
├── adult_profiling_report.py   # YData Profiling HTML report generation
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore file
└── README.md                   # This file
```

## 🚀 Installation

### 1. Requirements

Python 3.7+ is required.

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the Dataset

Download the dataset from [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/adult) and save it as `adult.csv` in the `data/` folder.

## 📝 EDA Steps and Outputs

### Step 1: Dataset Overview (`adult_dataset_overview.py`)

**Purpose**: Understand the basic characteristics of the dataset

**Outputs**:
- Dataset size (rows × columns)
- Data types (dtypes)
- Missing values analysis
- Duplicate records check
- Basic statistical summary

**Example Output**:
```
Shape: (32561, 15)
Missing values:
- workclass: 1836
- occupation: 1843
- native.country: 583
```

### Step 2: Categorical Variables Analysis (`adult_categories.py`)

**Purpose**: Examine the distribution of categorical variables

**Outputs**:
- Category counts for each categorical variable
- Category frequencies
- Category distribution ratios

**Example Output**:
```
workclass:
Private             22696
Self-emp-not-inc     2541
Local-gov            2093
...
```

### Step 3: Target Variable Profiling (`adult_y_profiling.py`)

**Purpose**: Analyze relationships between target variable (income) and other features

**Outputs**:

1. **Target Variable Distribution**
   - Income level distribution (count and percentage)
   - Class imbalance check

2. **Numerical Features vs Target**
   - Statistical summary by income groups for each numerical feature
   - T-test results (significance of differences between groups)

3. **Categorical Features vs Target**
   - Cross-tabulation tables
   - Chi-square test results
   - Income level distribution for each category

4. **Feature Importance Ranking**
   - Numerical features: Correlation coefficients
   - Categorical features: Cramér's V values
   - Top 10 most important features list

5. **Key Insights**
   - Variables with highest significance
   - Features with strong relationship with target

**Example Output**:
```
TOP FEATURES BY IMPORTANCE:
1. relationship: 0.4523
2. marital.status: 0.4121
3. age: 0.2345
4. education.num: 0.2234
5. hours.per.week: 0.1987
```

### Step 4: YData Profiling Report (`adult_profiling_report.py`)

**Purpose**: Generate an automatic, comprehensive EDA report

**Outputs**:
- `adult_report.html`: Interactive HTML report
- Report content:
  - Dataset overview
  - Variable analysis (detailed analysis for each variable)
  - Interactions (relationships between variables)
  - Correlations (correlation matrix)
  - Missing values (missing values visualization)
  - Sample data (sample records)

## 🎯 EDA Output Examples

### 1. Basic Statistics
- Dataset size and structure
- Missing values percentage
- Duplicate records count

### 2. Variable Analysis
- **Numerical Variables**: Mean, median, std, min, max, quartiles
- **Categorical Variables**: Unique value count, frequency distribution, mode

### 3. Target Variable Analysis
- Class distribution (balanced/imbalanced)
- Statistics grouped by target for each feature
- Feature importance ranking

### 4. Relationship Analysis
- Correlation matrix (numerical variables)
- Cramér's V (categorical variables)
- Cross-tabulation tables

### 5. Visualizations (YData Profiling)
- Histograms
- Box plots
- Scatter plots
- Heatmaps

## 🔍 Key Findings

Based on Y-profiling analysis, the features with the strongest relationship with income level are:

1. **relationship**: Highest correlation (Cramér's V)
2. **marital.status**: Strong relationship
3. **age**: Positive correlation between age and income
4. **education.num**: Positive correlation between education level and income
5. **hours.per.week**: Positive correlation between working hours and income

## 📊 Running the Scripts

### Run all analyses sequentially:

```bash
# 1. Dataset overview
python adult_dataset_overview.py

# 2. Categorical variables analysis
python adult_categories.py

# 3. Target variable profiling
python adult_y_profiling.py

# 4. Generate YData Profiling report
python adult_profiling_report.py
```

## 📦 Dependencies

- `pandas`: Data manipulation
- `numpy`: Numerical computations
- `matplotlib`: Visualization
- `seaborn`: Advanced visualization
- `ydata_profiling`: Automatic EDA report
- `scipy`: Statistical tests

## 📄 License

This project is for educational purposes. The dataset is from UCI Machine Learning Repository.

## 👤 Author

Exploratory Data Analysis Portfolio Project

## 🔗 Resources

- [UCI Adult Dataset](https://archive.ics.uci.edu/ml/datasets/adult)
- [YData Profiling Documentation](https://ydata-profiling.ydata.ai/)
