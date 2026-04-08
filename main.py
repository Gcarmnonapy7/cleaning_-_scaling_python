import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
  
class StatisticAnalysis:

    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.statistics = []
        self.null_results = []
        self.duplicated = []
        self.outliers = {}
        
    def __len__(self):
        
        return len(self.data)
    
    def __repr__(self):
        rows,cols = self.data.shape
        return f"StatisticAnalysis(rows={rows},columns={cols})"

    def __getitem__(self, key):
        
        return self.data[key]
    
    def __setitem__(self, key, value):
        
        self.data[key] = value 
    
    def __iter__(self):
        """_summary_
        
        Allows : for loops (iter)

        Returns:
            _type_: _description_
        """
        return iter(self.data.columns)
    
    def __contains__(self, item):
        
        return item in self.data.columns # Boolean return
    
    def compute_statistics(self):

        numeric_data = self.data.select_dtypes(include="number")

        for col in numeric_data.columns:
            stats = {
                "column": col,
                "mean": numeric_data[col].mean(),
                "median": numeric_data[col].median(),
                "std": numeric_data[col].std(),
                "min": numeric_data[col].min(),
                "max": numeric_data[col].max()
            }

            self.statistics.append(stats)

        return pd.DataFrame(self.statistics).T

    def normalize(self):
        """
        Min-max normalization for numeric columns
        """
        
        numeric = self.data.select_dtypes(include="number")
        
        normalized = (numeric - numeric.min()) / (numeric.max() - numeric.min())
        
        return normalized
        
    def outliers_detection(self):
        
        numeric = self.data.select_dtypes(include="number")
        
        for col in numeric.columns:
            
            Q1 = numeric[col].quantile(0.25)
            Q3 = numeric[col].quantile(0.75)
            
            IQR = Q3 - Q1
            
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR

            self.outliers[col] = numeric[(numeric[col] < lower) | (numeric[col] > upper)][col]

        return self.outliers

    def correlation_analysis(self):
        
        numeric = self.data.select_dtypes(include="number")
        
        return numeric.corr()

    def counting_values(self):
        
        numeric = self.data.select_dtypes(include="number")
        counts = {}
        
        for col in numeric.columns:
            
            counts[col] = self.data[col].value_counts()
            
        return counts
    
    def isnull_data(self):
        
        
        
        for col in self.data.columns:
            pass
            
    
    def duplicated_data(self):
        pass
    
    

            
        
        

                    
        