# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col, mean, stddev, min, max, count, isnan, when, lit
# from pyspark.sql import functions as F

# Initialize Spark
# spark = SparkSession.builder \
#     .appName("StatisticAnalysisSpark") \
#     .getOrCreate()


# class StatisticAnalysisSpark:
    
#     def __init__(self, df):
#         self.df = df
#         self.statistics = []
#         self.outliers_dict = {}
    
#     def __len__(self):
#         return self.df.count()
    
#     def __repr__(self):
#         return f"StatisticAnalysisSpark(rows={self.df.count()}, columns={len(self.df.columns)})"
    
#     def compute_statistics(self):
#         numeric_cols = [f.name for f in self.df.schema.fields if str(f.dataType) in ['IntegerType', 'DoubleType', 'LongType', 'FloatType']]
        
#         stats = []
#         for col_name in numeric_cols:
#             summary = self.df.select(
#                 mean(col(col_name)).alias("mean"),
#                 F.expr(f'percentile({col_name}, 0.5)').alias("median"),
#                 stddev(col(col_name)).alias("std"),
#                 min(col(col_name)).alias("min"),
#                 max(col(col_name)).alias("max")
#             ).collect()[0]
            
#             stats.append({
#                 "column": col_name,
#                 "mean": summary["mean"],
#                 "median": summary["median"],
#                 "std": summary["std"],
#                 "min": summary["min"],
#                 "max": summary["max"]
#             })
        
#         return stats

#     def normalize(self):
#         numeric_cols = [f.name for f in self.df.schema.fields if str(f.dataType) in ['IntegerType', 'DoubleType', 'LongType', 'FloatType']]
        
#         normalized_df = self.df
#         for col_name in numeric_cols:
#             min_val = self.df.agg(min(col_name)).collect()[0][0]
#             max_val = self.df.agg(max(col_name)).collect()[0][0]
#             normalized_df = normalized_df.withColumn(col_name, (col(col_name) - lit(min_val)) / (lit(max_val) - lit(min_val)))
        
#         return normalized_df
    
#     def outliers_detection(self):
#         numeric_cols = [f.name for f in self.df.schema.fields if str(f.dataType) in ['IntegerType', 'DoubleType', 'LongType', 'FloatType']]
        
#         for col_name in numeric_cols:
#             q1, q3 = self.df.approxQuantile(col_name, [0.25, 0.75], 0.05)
#             iqr = q3 - q1
#             lower = q1 - 1.5 * iqr
#             upper = q3 + 1.5 * iqr
            
#             outliers = self.df.filter((col(col_name) < lower) | (col(col_name) > upper))
#             self.outliers_dict[col_name] = outliers
        
#         return self.outliers_dict

#     def correlation_analysis(self):
#         numeric_cols = [f.name for f in self.df.schema.fields if str(f.dataType) in ['IntegerType', 'DoubleType', 'LongType', 'FloatType']]
        
#         corr_dict = {}
#         for i, col1 in enumerate(numeric_cols):
#             corr_dict[col1] = {}
#             for col2 in numeric_cols:
#                 corr_dict[col1][col2] = self.df.stat.corr(col1, col2)
        
#         return corr_dict
    
#     def counting_values(self):
#         counts_dict = {}
#         for col_name in self.df.columns:
#             counts_dict[col_name] = self.df.groupBy(col_name).count().collect()
#         return counts_dict
    
#     def checking_null_data(self):
#         total_rows = self.df.count()
#         for col_name in self.df.columns:
#             null_count = self.df.filter(col(col_name).isNull() | isnan(col(col_name))).count()
#             if null_count > 0:
#                 print("="*60)
#                 print(f"Column: {col_name}")
#                 print(f"Missing values: {null_count}")
#                 print(f"Percentage: {null_count / total_rows * 100:.2f}%")
#                 print("="*60)
    
#     def duplicated_data(self):
#         duplicate_count = self.df.count() - self.df.dropDuplicates().count()
#         if duplicate_count > 0:
#             print("="*60)
#             print(f"Total duplicated rows: {duplicate_count}")
#             print("="*60)