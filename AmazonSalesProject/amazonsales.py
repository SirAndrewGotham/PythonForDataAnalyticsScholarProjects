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

