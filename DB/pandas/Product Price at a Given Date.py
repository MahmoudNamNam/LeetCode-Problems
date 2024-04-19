import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    
    # Filter the products DataFrame based on the given_date
    filtered_products = products[products['change_date'] <= '2019-08-16']
    
    # Sort the filtered DataFrame by 'change_date' in ascending order
    filtered_products.sort_values(by='change_date', ascending=True, inplace=True)
    
    # Keep only the last recorded price for each product
    filtered_products.drop_duplicates(subset='product_id', keep='last', inplace=True)
    
    # Create a DataFrame with unique product IDs
    ids = pd.DataFrame({'product_id': products['product_id'].unique()})
    
    # Merge the filtered DataFrame with the DataFrame containing unique product IDs
    output = pd.merge(ids, filtered_products, on='product_id', how='left')
    
    # Rename the 'new_price' column to 'price' and fill missing values with 10
    output['price'] = output['new_price'].fillna(10)
    
    # Keep only 'product_id' and 'price' columns
    output = output[['product_id', 'price']]
    
    return output

# Example usage:
products_data = {
    'product_id': [1, 2, 1, 1, 2, 3],
    'new_price': [20, 50, 30, 35, 65, 20],
    'change_date': ['2019-08-14', '2019-08-14', '2019-08-15', '2019-08-16', '2019-08-17', '2019-08-18']
}

products_df = pd.DataFrame(products_data)

result_df = price_at_given_date(products_df)
print(result_df)
