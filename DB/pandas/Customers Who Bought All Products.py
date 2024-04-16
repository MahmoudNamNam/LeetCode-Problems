import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    result = customer.drop_duplicates(keep = 'first').groupby('customer_id').count().reset_index()
    return result[result.product_key == len(product)][['customer_id']]

customer_data = {
    'customer_id': [1, 2, 3, 3, 1],
    'product_key': [5, 6, 5, 6, 6]
}

product_data = {
    'product_key': [5, 6]
}

# Create DataFrames
customer = pd.DataFrame(customer_data)
product = pd.DataFrame(product_data)
result = customer.drop_duplicates(keep = 'first').groupby('customer_id').count().reset_index()
print(result)
print(result[result.product_key == len(product)][['customer_id']])
