import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    sales['rank'] = sales.groupby('product_id')['year'].rank(method='min',ascending = True)
    res = sales.loc[sales['rank']==1,['product_id','year','quantity','price']].rename(columns = {'year':'first_year'})
    return res

sales_data = {
    'sale_id': [1, 2, 7],
    'product_id': [100, 100, 200],
    'year': [2008, 2009, 2011],
    'quantity': [10, 12, 15],
    'price': [5000, 5000, 9000]
}

product_data = {
    'product_id': [100, 200, 300],
    'product_name': ['Nokia', 'Apple', 'Samsung']
}

sales = pd.DataFrame(sales_data)
product = pd.DataFrame(product_data)

print(sales_analysis(sales, product))

