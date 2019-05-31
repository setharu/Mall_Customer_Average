'''Find out the average of Male and Female Spending Score '''

file_path=r'D:/Mall_Customers_Excercise/machineLearningAZ-master/machineLearningAZ-master/Machine Learning A-Z Template Folder/Part 4 - Clustering/Section 24 - K-Means Clustering/Mall_Customers.csv'

infile = open(file_path,'r')
male_score = list()
female_score = list()
for line in infile:
    columns = line.split(',')
    gender, score = columns[1], columns[4]
    if gender == 'Male':
        male_score.append(int(score))
    if gender == 'Female':
        female_score.append(int(score))

#print(male_score)
#print(female_score)
        
male_score_average = sum(male_score)/len(male_score)
female_score_average = sum(female_score)/len(female_score)

print("Average Male Spending Score is ", male_score_average)
print("Average Female Spending Score is ", female_score_average)

infile.close()

print("End of the Program")
