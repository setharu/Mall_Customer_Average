'''Find out the average of Male and Female Spending Score '''

import pandas as pd

file_path=r'D:/Mall_Customers_Excercise/machineLearningAZ-master/machineLearningAZ-master/Machine Learning A-Z Template Folder/Part 4 - Clustering/Section 24 - K-Means Clustering/Mall_Customers.csv'
df= pd.read_csv(file_path)
new_df = df.groupby(['Genre']).mean().sort_values('Spending Score (1-100)', ascending= False)
print(new_df)

'''OutPut

============== RESTART: D:/Pandas/pandas_mall_genre_average.py ==============
        CustomerID        Age  Annual Income (k$)  Spending Score (1-100)
Genre                                                                    
Female   97.562500  38.098214           59.250000               51.526786
Male    104.238636  39.806818           62.227273               48.511364

'''
