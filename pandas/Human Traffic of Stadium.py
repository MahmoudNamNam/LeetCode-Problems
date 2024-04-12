import pandas as pd

import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    # Select rows where the number of people is greater than or equal to 100
    df = stadium[stadium['people'] >= 100]
    
    # Create a flag to identify consecutive rows based on 'id' column
    df['flag'] = ((df['id'].diff() == 1) & (df['id'].diff().shift(1) == 1))
    
    # Filter rows to keep only groups of consecutive rows with 'flag' set to True
    df = df[(df['flag'] == True) | (df['flag'].shift(-1) == True) | (df['flag'].shift(-2) == True)]
    
    # Remove the 'flag' column and sort the DataFrame by 'visit_date'
    return df.loc[:, df.columns != 'flag'].sort_values(by='visit_date')

# Explanation:
# 1. Select rows with 100 or more people.
# 2. Identify consecutive rows using the 'id' column.
# 3. Keep only groups of consecutive rows with 100 or more people.
# 4. Remove the 'flag' column and sort by visit_date.

data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8],
    'visit_date': ['2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04',
                   '2017-01-05', '2017-01-06', '2017-01-07', '2017-01-09'],
    'people': [10, 109, 150, 99, 145, 1455, 199, 188]
}
stadium = pd.DataFrame(data)
df = stadium[stadium['people'] >= 100]
df['flag'] = ((df['id'].diff() == 1) & (df['id'].diff().shift(1) == 1))
df = df[(df['flag'] == True)| (df['flag'].shift(-1) == True) | (df['flag'].shift(-2) == True)]

print(df)

# result = human_traffic(stadium_df)
# print(result)




def find_consecutive_records(df):
    # Sort DataFrame by visit_date
    df = df.sort_values(by='visit_date')

    # Calculate the difference between consecutive ids
    df['id_diff'] = df['id'].diff().fillna(1)

    # Reset group counter whenever there's a gap in consecutive ids
    df['grp'] = (df['id_diff'] != 1).cumsum()

    # Filter groups where people count is greater than or equal to 100
    consecutive_groups = df[df['people'] >= 100].groupby('grp').filter(lambda x: len(x) >= 3)

    # Remove intermediate columns
    consecutive_groups = consecutive_groups.drop(columns=['id_diff', 'grp'])

    return consecutive_groups[['id', 'visit_date', 'people']]


# stadium_df = pd.DataFrame(data)

# result = find_consecutive_records(stadium_df)
# # print(result)
# print(stadium_df)
# print('-'*50)
# stadium_df = stadium_df[stadium_df['people']>100]
# stadium_df['id_diff'] = stadium_df['id'].diff().fillna(1)
# stadium_df['grp'] = (stadium_df['id_diff'] != 1).cumsum()
# consecutive_groups = stadium_df[stadium_df['people'] >= 100].groupby('grp').filter(lambda x: len(x) >= 3)

# print(stadium_df )

# print()
# print('--'*50)
# print(consecutive_groups)