import numpy as np
import pandas as pd

# Prices table
prices_data = {
    'product_id': [1, 1, 2, 2],
    'start_date': ['2019-02-17', '2019-03-01', '2019-02-01', '2019-02-21'],
    'end_date': ['2019-02-28', '2019-03-22', '2019-02-20', '2019-03-31'],
    'price': [5, 20, 15, 30]
}

prices_df = pd.DataFrame(prices_data)

# Convert date columns to datetime
prices_df['start_date'] = pd.to_datetime(prices_df['start_date'])
prices_df['end_date'] = pd.to_datetime(prices_df['end_date'])

# UnitsSold table
units_sold_data = {
    'product_id': [1, 1, 2, 2],
    'purchase_date': ['2019-02-25', '2019-03-01', '2019-02-10', '2019-03-22'],
    'units': [100, 15, 200, 30]
}

units_df=pd.DataFrame(units_sold_data)
import pandas as pd
def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(prices, units_sold, on='product_id', how='left')
    df = df[df.purchase_date.isna() | ((df.purchase_date >= df.start_date) & (df.purchase_date <= df.end_date))]
    df['total_price'] = df['price'] * df['units']
    df = df.groupby('product_id').agg(total_price=('total_price', 'sum'), total_units_sold=('units', 'sum')).reset_index()
    df['average_price'] = np.where(df.total_units_sold != 0, round(df.total_price/df.total_units_sold,2), 0)
    return df[['product_id','average_price']]


print(average_selling_price(prices_df,units_df))