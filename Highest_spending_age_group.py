'''Find out the Highest Spending age group
Age Group 1 = 1-19
Age Group 2 = 20-29
'''

file_path=r'D:/Mall_Customers_Excercise/machineLearningAZ-master/machineLearningAZ-master/Machine Learning A-Z Template Folder/Part 4 - Clustering/Section 24 - K-Means Clustering/Mall_Customers.csv'

infile = open(file_path,'r')
age_group_dict = dict()
age_group_1 = '1-19'
age_group_2 = '20-29'
for line in infile:
    columns = line.split(',')
    age = columns[2].strip()
    score = columns[4].strip()
    if line[0].isalpha():
        continue
    if int(age) in range(1,20):
        if age_group_1 in age_group_dict:
            age_group_dict[age_group_1].append(int(score))
        else:
            age_group_dict[age_group_1] = list()
    else:
        if int(age) in range(20,30):
            if age_group_2 in age_group_dict:
                age_group_dict[age_group_2].append(int(score))
            else:
                age_group_dict[age_group_2] = list()

infile.close()
print(age_group_dict)

for age_group, score in age_group_dict.items():
    print("Age Group ", age_group, " spends ", sum(score))
    

for age_group, score in sorted(list(age_group_dict.items()), key = lambda x: sum(x[1]), reverse= True)[:1]:
    print("Highest spending age goup is ", age_group)
    print("Total Expenditure is ", sum(score))
    
