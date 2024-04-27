import pandas as pd

# Define the data as a list of dictionaries
data = [
    {"id": 121, "country": "US", "state": "approved", "amount": 1000, "trans_date": "2018-12-18"},
    {"id": 122, "country": "US", "state": "declined", "amount": 2000, "trans_date": "2018-12-19"},
    {"id": 123, "country": "US", "state": "approved", "amount": 2000, "trans_date": "2019-01-01"},
    {"id": 124, "country": "DE", "state": "approved", "amount": 2000, "trans_date": "2019-01-07"}
]

# Convert the data to a DataFrame
df = pd.DataFrame(data)

df['trans_date'] = pd.to_datetime(df['trans_date'])
df['month']= df['trans_date'].dt.month
# Display the DataFrame
print(df)
print(df.groupby('month')['state'])