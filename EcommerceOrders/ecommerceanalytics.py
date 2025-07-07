"""
Ecommerce orders analyses project, see common README.md for a complete description.
"""

import os
import pandas as pd

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
orders_data_cleaned = orders_data.fillna('N/A')
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
orders_data_cleaned.duplicated().sum() # shows 3 duplicates, warn the dev team!

# Remove duplicates from the Orders data
orders_data_cleaned = orders_data_cleaned.drop_duplicates()

# Verify no duplicates left in the Orders table
orders_data_cleaned.duplicated().sum() # good, null duplicates

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

