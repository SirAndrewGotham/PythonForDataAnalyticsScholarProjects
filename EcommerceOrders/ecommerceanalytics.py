"""
Ecommerce orders analyses project, see common README.md for a complete description.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# prepare a variable for the relative path to the source excel files
source_files_path = os.getcwd() + '\\EcommerceOrders\\SourceFiles'

# ======================================================================================================================
# Loading files
# ======================================================================================================================
customers_data = pd.read_excel(source_files_path + '\\customers.xlsx')
orders_data = pd.read_excel(source_files_path + '\\orders.xlsx')
payments_data = pd.read_excel(source_files_path + '\\order_payment.xlsx')

# ======================================================================================================================
# Looking around/Analysing the data and cleaning nulls
# ======================================================================================================================

# orders_data.info() # three columns related to order_approval and order_deliveries (2) has null values
# customers_data.info() # shows no null values
# payments_data.info() # shows few (actually 2) nulls in payments value

# Handling missing data
# Check for missing data in the Orders
# orders_data.isnull().sum()
# payments_data.isnull().sum()
# customers_data.isnull().sum()

# Filling missing data in the Orders data with default value
orders_data = orders_data.fillna('N/A')
# Confirm no null data left
# orders_data_cleaned.isnull().sum()

# Drop rows with missing data in the payments data
payments_data = payments_data.dropna()
# Confirm no null data left
payments_data.isnull().sum()

# Customers data has no null values, no cleaning actions needed

# ======================================================================================================================
# Removing Duplicate Data
# ======================================================================================================================

### ORDERS
# Check for duplicated in Orders data
orders_data.duplicated().sum() # shows 3 duplicates, warn the dev team!

# Remove duplicates from the Orders data
orders_data = orders_data.drop_duplicates()

# Verify no duplicates left in the Orders table
orders_data.duplicated().sum() # good, null duplicates

### PAYMENTS
# Check for duplicates in the Payments data
payments_data.duplicated().sum() # shows 1 duplicate

# Remove duplicates from the Payments data
payments_data = payments_data.drop_duplicates()

# Verify no duplicates left in the Payments table
payments_data.duplicated().sum() # good, null duplicates

### Customers
# Check for duplicates in the Customers data
customers_data.duplicated().sum() # no duplicates found

# ======================================================================================================================
# Filtering the Data
# ======================================================================================================================

# Select subset of the Orders data based on the order status (invoiced and not delivered yet)
invoiced_orders_data = orders_data[orders_data['order_status'] == 'invoiced']

# Reset index
invoiced_orders_data = invoiced_orders_data.reset_index(drop=True)

# Subset of the Payments data using credit card and value over 1000
credit_card_payments_over_1000_data = payments_data[(payments_data['payment_type'] == 'credit_card') & (payments_data['payment_value'] > 1000)]

# Select a subset of Customers
customers_from_sp = customers_data[customers_data['customer_state'] == 'SP']

# ======================================================================================================================
# Merge and Join Dataframes
# ======================================================================================================================

# Merge Orders data with Payments data on order_id column
merged_data = pd.merge(orders_data, payments_data, on='order_id')

# Join merged data with Customers on the customer_id column
joined_data = pd.merge(merged_data, customers_data, on='customer_id')

##### JOINED_DATA becomes main complete table to fork on

# ======================================================================================================================
# Data Visualization
# ======================================================================================================================

# Create a field called "month" from order_purchase_timestamp (add that column to the table)
joined_data["month_year"] = joined_data["order_purchase_timestamp"].dt.to_period("M")
joined_data["week_year"] = joined_data["order_purchase_timestamp"].dt.to_period("W")
joined_data["year"] = joined_data["order_purchase_timestamp"].dt.to_period("Y")

# Group and create a plot
# plt.plot(x, y) # this is the structure
payments_monthly_data = joined_data.groupby("month_year")['payment_value'].sum()
payments_monthly_data = payments_monthly_data.reset_index()

# convert month_year form period(M) to string
payments_monthly_data["month_year"] = payments_monthly_data["month_year"].astype(str)

# x axis would be "month_year" of the payments_monthly_data and y zxis would be "payment_value" of the payments_monthly_data
# plt.plot(payments_monthly_data["month_year"], payments_monthly_data["payment_value"], color='red', marker='o')
# plt.ticklabel_format(useOffset=False, axis="y", style="plain")
#
# # format plot
# plt.title("Payments by Month and Year")
# plt.xlabel('Month and Year')
# plt.xticks(rotation=90, fontsize=8)
#
# plt.ylabel('Payment Value')
# plt.yticks(fontsize=8)

# Scatter plot to see payments values dependency related to payment installments

scatter_df = joined_data.groupby("customer_unique_id").agg({'payment_value': 'sum', 'payment_installments': 'sum'})

plt.scatter(scatter_df["payment_value"], scatter_df["payment_installments"])

plt.xlabel("Payment Value")
plt.ylabel("Payment Installments")
plt.title("Payment Value vs Installments by Customer")

plt.show()
