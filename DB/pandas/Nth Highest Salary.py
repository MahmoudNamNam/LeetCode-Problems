import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted_salaries = employee['salary'].sort_values(
        ascending=False
    ).drop_duplicates()
    return pd.DataFrame({
        f'getNthHighestSalary({N})': [None if sorted_salaries.size < N or N<=0 else sorted_salaries.iloc[N-1]]
    })
