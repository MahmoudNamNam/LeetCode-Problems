import pandas as pd

# Input data
accounts_data = {
    'account_id': [3, 2, 8, 6],
    'income': [108939, 12747, 87709, 91796]
}

# Creating DataFrame
accounts = pd.DataFrame(accounts_data)

# print(accounts)


import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # Define salary categories
    bins = [-float("inf"), 20000, 50001, float("inf")]
    labels = ['Low Salary', 'Average Salary', 'High Salary']

    # Categorize incomes into salary categories
    accounts['category'] = pd.cut(accounts['income'], bins=bins, labels=labels, right=False)
    # Count the number of accounts for each category
    counts = accounts['category'].value_counts().reset_index()
    counts.columns = ['category', 'accounts_count']
    # Sort categories in the desired order
    counts = counts.sort_values(by='category')

    return counts


print(count_salary_categories(accounts))