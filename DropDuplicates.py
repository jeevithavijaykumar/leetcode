""" 2882. Drop Duplicate Rows """
"""There are some duplicate rows in the DataFrame based on the email column.
Write a solution to remove these duplicate rows and keep only the first occurrence."""

import pandas as pd

def dropDuplicates(customers):
    customers.drop_duplicates(subset=['name','email'],keep='first',inplace=True)
    return(customers)