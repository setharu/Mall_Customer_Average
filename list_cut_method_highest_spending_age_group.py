import pandas as pd

file_path=r'D:/Mall_Customers_Excercise/machineLearningAZ-master/machineLearningAZ-master/Machine Learning A-Z Template Folder/Part 4 - Clustering/Section 24 - K-Means Clustering/Mall_Customers.csv'
df = pd.read_csv(file_path)

#print(df)

bins = [0,18,29,39,49,59,69,99]
group_names = ['0-18','19-29','30-39','40-49','50-59','20-69','70-79']

df['AgeGroup'] = pd.cut(df.Age, bins, labels= group_names)


new_df = df.groupby(['AgeGroup']).sum().sort_values('Spending Score (1-100)', ascending= False)


print(new_df[['Spending Score (1-100)']][:1])
