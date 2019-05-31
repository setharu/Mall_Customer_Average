'''Find out the average of Male and Female Spending Score Using Dictionary of list'''

file_path=r'D:/Mall_Customers_Excercise/machineLearningAZ-master/machineLearningAZ-master/Machine Learning A-Z Template Folder/Part 4 - Clustering/Section 24 - K-Means Clustering/Mall_Customers.csv'

infile = open(file_path,'r')
gender_dict = dict()

for line in infile:
    columns = line.split(',')
    gender, score = columns[1], columns[4]
    if line[0].isalpha():
        continue
    if gender in gender_dict:
        gender_dict[gender].append(int(score))
    else:
        gender_dict[gender]=list()

print(gender_dict)

for gender, score in gender_dict.items():
    print(gender, sum(score)/len(score))

infile.close()

print("End of the Program")
