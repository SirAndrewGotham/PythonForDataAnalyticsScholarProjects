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
# Looking around/Analysing the data
# ======================================================================================================================

orders_data.info() # three columns related to order_approval and order_deliveries (2) has null values
customers_data.info() # shows no null values
payments_data.info() # shows few (actually 2) nulls in payments value
