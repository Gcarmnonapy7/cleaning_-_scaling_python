import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns



def checking_null_data(data: pd.DataFrame):
    
    total_rows = len(data)

    for col in data.columns:
        is_null = data[col].isna().sum()
        percent = (is_null / total_rows) * 100

        if is_null > 0:
            print("=" * 60)
            print(f"Column: {col}")
            print(f"Missing values: {is_null}\n")
            print(f"Percentage: {percent:.2f}%\n")
            print("=" * 60)
            
            
def duplicated_data(data:pd.DataFrame):
    
    total = len(data)
    
    for col in data.columns:
        
        is_duplicated = data[col].duplicated.sum()
        percent = (is_duplicated / total) * 100
        
    if is_duplicated > 0 :
        print("=" * 60)
        print()
        print("=" * 60)
        


class StatisticAnalysis:
    
    def __init__(self):
        pass