"""
Amazon Sales Data Analytics Project to study Python, NumPy and Pandas based on Indian Amazon Sales Report saved to Excel file (128974 records total).
Objective:
The merchant wants to know:
- How many sales over 1000 made;
- How many sales made in the "Tops" category with quantities of 3;
- Total sales by category;
- Average amount by category and status;
- Total Sales by fulfilment and shipment type.
Last 2 tables (averages and total sales) should be exported for further emailing.

Created on Sun Jul 06 21:50:24 2025
@author: SirAndrewGotham
"""

import os
import pandas as pd

# use os for correct relative path
sales_data = pd.read_excel(os.getcwd() + '\\AmazonSalesProject\\sales_data.xlsx')

# OBJECTIVE 1: How many sales over 1000 made
amount_data = sales_data[sales_data['Amount'] > 1000]
# print(amount_data)

# OBJECTIVE 2: How many sales made in the "Tops" category with quantities of 3
amount_and_qty_data = sales_data[(sales_data['Amount'] > 1000) & (sales_data['Qty'] == 3)]
# print(amount_and_qty_data)

# OBJECTIVE 3: Total sales by category
category_totals = sales_data.groupby('Category')['Amount'].sum().reset_index()
category_totals = category_totals.sort_values(by=['Amount'], ascending=False)

# OBJECTIVE 4: Average amount by category and status
# Average amount by category and fulfilment
fulfilment_averages = sales_data.groupby(['Category', 'Fulfilment'], as_index=False)['Amount'].mean().sort_values(by=['Amount'], ascending=False)
# Average amount by category and status
category_and_status_average = sales_data.groupby(['Category', 'Status'], as_index=False)['Amount'].mean().sort_values(by=['Amount'], ascending=False)

# OBJECTIVE 5: Total Sales by fulfilment and shipment type
fulfilment_and_shipment_totals = sales_data.groupby(['Fulfilment', 'Courier Status'], as_index=False)['Amount'].sum().sort_values(by=['Amount'], ascending=False)
