# This is a data cleaning application
# importing dependencies
import pandas as pd
import numpy as np
import time 
import openpyxl
import xlrd
import os
import random

data_path = "diwali_sales_data.csv"
data_name = 'Diwali Sales'

def data_cleaning_master(data_path,data_name):

    print("Thank you for giving the details")
    
    
# checking if the path exist
    if not os.path.exists(data_path):
        print('Please enter the correct path !')
        return
    else:
        #checking the file type
        if data_path.endswith('.csv'):
            print("Dataset is csv!")
            data = pd.read_csv(data_path,encoding_errors ='ignore')
            
        elif(data_path.endswith('.xlsx')):
            print("Dataset is excel file !")
            data = pd.read_excel(data_path)
            
        else:
            print("Unknown file Type")
            return
    # showing number of records
    print(f'Dataset cotnain total rows : {data.shape[0]}\n Total Columns :{data.shape[1]}')
    #start cleaning
    duplicates = data.duplicated()
    total_duplicates = data.duplicated().sum()

    print("Datasets has total duplicates :{total_duplicates}")

    # Saving the duplicates
    if total_duplicates>0:
        duplicate_records = data[duplicates]
        duplicate_records.to_csv(f'{data_name}_duplicates.csv', index = None)
    # deleting duplicates
    df = data.drop_duplicates()
    #find the missing values
    total_missing_values = df.isnull().sum().sum()
    missing_value_columns = df.isnull().sum()

    print(f'Dataset has total missing values : {total_missing_values}')
    print(f'Dataset contain missing value by columns \n {missing_value_columns}')
    # dealing with missing values
    # fillna - int and float
    # dropna - any object

    columns = df.columns

    for col in columns:
        # filling mean for numeric columns all rows
        if df[col].dtype in(int, float):
            df[col]=df[col].fillna(df[col].mean())
            
        else:
            # dropping all rows with non- number missing records
            df.dropna(subset=col, inplace = True)


    # Data is cleaned
    print(f"The Dataset is cleaned!\nNumber of Rows :{df.shape[0]}\nNumber of Columns: {df.shape[1]}")

    # Saving the clean dataset
    df.to_csv(f'{data_name}_Cleaned_Data.csv',index = None)
    print("Dataset is saved")
    
if __name__ == "__main__":

    

    # # Ask path and file name
    # data_path = input('Enter the path : ')
    # data_name = input('Enter a file name : ')
    
    #calling the function 
    data_cleaning_master(data_path,data_name)