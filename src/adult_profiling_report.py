"""
YData Profiling Report Generation
This script generates a comprehensive automated EDA report using YData Profiling.
"""

import pandas as pd
import sys

# Try to import ProfileReport with error handling
try:
    from ydata_profiling import ProfileReport
except ImportError as e:
    print(f"Error importing ydata_profiling: {e}")
    print("Trying alternative import...")
    try:
        from pandas_profiling import ProfileReport
    except ImportError:
        print("ERROR: ydata-profiling is not installed.")
        print("Please install it using: pip install ydata-profiling")
        sys.exit(1)

# Load the data
import os
data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'adult.data')
if not os.path.exists(data_path):
    data_path = os.path.join('data', 'adult.data')
    if not os.path.exists(data_path):
        data_path = os.path.join('..', 'data', 'adult.data')

# Define column names for Adult Census Income dataset
column_names = [
    'age', 'workclass', 'fnlwgt', 'education', 'education.num',
    'marital.status', 'occupation', 'relationship', 'race', 'sex',
    'capital.gain', 'capital.loss', 'hours.per.week', 'native.country', 'income'
]

try:
    df = pd.read_csv(data_path, names=column_names, na_values='?', skipinitialspace=True)
except FileNotFoundError:
    print(f"ERROR: Dataset not found at {data_path}")
    print("Please make sure the dataset is in the data/ folder.")
    sys.exit(1)

# Generate the report
print("Generating profile report...")
print("This may take a few minutes...")

try:
    profile = ProfileReport(
        df, 
        title="Adult Census Profile",
        minimal=False,
        progress_bar=True
    )
    
    # Save the report to .html
    output_file = "adult_report.html"
    profile.to_file(output_file)
    print(f"✓ Report successfully saved to {output_file}")
except Exception as e:
    print(f"ERROR generating report: {e}")
    print("This might be due to a version incompatibility.")
    print("Try reinstalling: pip install --upgrade ydata-profiling")
    sys.exit(1) 