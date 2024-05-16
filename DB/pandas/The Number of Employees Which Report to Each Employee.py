import math
import pandas as pd

# Define the original data
data = [
    {'employee_id': 1, 'name': 'Michael', 'reports_to': None, 'age': 45},
    {'employee_id': 2, 'name': 'Alice', 'reports_to': 1, 'age': 38},
    {'employee_id': 3, 'name': 'Bob', 'reports_to': 1, 'age': 42},
    {'employee_id': 4, 'name': 'Charlie', 'reports_to': 2, 'age': 34},
    {'employee_id': 5, 'name': 'David', 'reports_to': 2, 'age': 40},
    {'employee_id': 6, 'name': 'Eve', 'reports_to': 3, 'age': 37},
    {'employee_id': 7, 'name': 'Frank', 'reports_to': None, 'age': 50},
    {'employee_id': 8, 'name': 'Grace', 'reports_to': None, 'age': 48}
]

# Create DataFrame from the data
df = pd.DataFrame(data)


def count_employees(df: pd.DataFrame) -> pd.DataFrame:
    merged_df = df.merge(df, left_on='employee_id', right_on='reports_to', suffixes=('_x', '_y'))
    summary_df = merged_df.groupby(['employee_id_x', 'name_x']).agg(
        reports_count=pd.NamedAgg(column='employee_id_y', aggfunc='count'),
        average_age=pd.NamedAgg(column='age_y', aggfunc='mean')
    ).reset_index()

    summary_df.columns = ['employee_id', 'name', 'reports_count', 'average_age']
    summary_df['average_age'] = summary_df['average_age'].apply(math.ceil)
    return summary_df



print(count_employees(df))