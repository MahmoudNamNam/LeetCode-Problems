import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # Perform a self-merge to match employees with their managers
    merged_df = pd.merge(employee, employee, left_on='managerId', right_on='id', suffixes=('_emp', '_mgr'))

    # Filter the DataFrame to select rows where an employee's salary is greater than their manager's salary
    filtered_df = merged_df[merged_df['salary_emp'] > merged_df['salary_mgr']]

    # Select the 'name' column of the resulting DataFrame
    result = filtered_df[['name_emp']]

    # Rename the column to 'Employee'
    result.columns = ['Employee']

    return result

# Example usage:
employee_data = {
    'id': [1, 2, 3, 4],
    'name': ['John', 'Alice', 'Bob', 'Mary'],
    'salary': [50000, 60000, 55000, 70000],
    'managerId': [None, 1, 2, 2]
}
employee_df = pd.DataFrame(employee_data)
print(employee_df)
result = find_employees(employee_df)
print(result)
