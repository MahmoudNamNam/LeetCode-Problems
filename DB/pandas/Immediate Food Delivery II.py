import pandas as pd

# Define the delivery data as a list of dictionaries
delivery_data = [
    {'delivery_id': 1, 'customer_id': 1, 'order_date': '2019-08-01', 'customer_pref_delivery_date': '2019-08-02'},
    {'delivery_id': 2, 'customer_id': 2, 'order_date': '2019-08-02', 'customer_pref_delivery_date': '2019-08-02'},
    {'delivery_id': 3, 'customer_id': 1, 'order_date': '2019-08-11', 'customer_pref_delivery_date': '2019-08-12'},
    {'delivery_id': 4, 'customer_id': 3, 'order_date': '2019-08-24', 'customer_pref_delivery_date': '2019-08-24'},
    {'delivery_id': 5, 'customer_id': 3, 'order_date': '2019-08-21', 'customer_pref_delivery_date': '2019-08-22'},
    {'delivery_id': 6, 'customer_id': 2, 'order_date': '2019-08-11', 'customer_pref_delivery_date': '2019-08-13'},
    {'delivery_id': 7, 'customer_id': 4, 'order_date': '2019-08-09', 'customer_pref_delivery_date': '2019-08-09'}
]

# Create a DataFrame from the delivery data
df = pd.DataFrame(delivery_data)

# Convert 'order_date' and 'customer_pref_delivery_date' columns to datetime format
df['order_date'] = pd.to_datetime(df['order_date'])
df['customer_pref_delivery_date'] = pd.to_datetime(df['customer_pref_delivery_date'])



def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    grouped_df = delivery.groupby("customer_id").min().reset_index()

    immediate_deliveries = grouped_df[grouped_df['order_date'] == grouped_df['customer_pref_delivery_date']]
    num_immediate_deliveries = len(immediate_deliveries)

    total_customers = len(grouped_df)

    if total_customers > 0:
        immediate_percentage = (num_immediate_deliveries / total_customers) * 100
    else:
        immediate_percentage = 0.0  

    result_df = pd.DataFrame({"immediate_percentage": [immediate_percentage]}).round(2)
    
    return result_df


print(immediate_food_delivery(df))




def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery['rank'] = delivery.groupby('customer_id')['order_date'].rank(method = 'dense', ascending = True)
    delivery = delivery[delivery['rank'] == 1]
    delivery['status'] = delivery.apply(lambda x: 1 if x['order_date'] == x['customer_pref_delivery_date'] else 0, axis = 1)
    total_immdiate = delivery['status'].sum()
    print(total_immdiate)
    res = pd.DataFrame([round(total_immdiate/delivery.shape[0]*100,2)], columns = ['immediate_percentage'])
    return res
    