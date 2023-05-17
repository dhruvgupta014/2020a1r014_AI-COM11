import csv
num_attributes = 3
a = []
print("\n the given training data set \n")
with open('C:/Users/kerni/Documents/2020A1R002.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        a.append(row)
        print(row)
print("\n the initial value of hypothesis:")
hypothesis=['0']*num_attributes
print(hypothesis)

for j in range(0,num_attributes):
    hypothesis[j] = a[0][j];

print("\n find s: finding a maximally specific hypothesis\n")

for i in range(0,len(a)):
    if a[i][num_attributes] =='Positive':
        for j in range(0,num_attributes):
            if a[i][j]!=hypothesis[j]:
                hypothesis[j]='?'
            else:
                hypothesis[j]= a[i][j]
    
    print("for training instance no:(0) the hypothesis is".format(i),hypothesis)
print("\n the maximally specific hypothesis for a given training examples :\n")
print(hypothesis)

