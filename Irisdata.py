import numpy as np
import pandas as pd
import csv
from matplotlib import pyplot as plt

print("Read CSV using pandas package")
print("=============================")
file_csv ="E:\MSc Data Science\Data Science Techniques and Applications\Labs\Irisdata.csv"
df = pd.read_csv(file_csv)
print(df.head())
df["Species"].unique()
print(df.groupby("Species").size())

setosa=df[df['Species']=='Iris-setosa']
versicolor =df[df['Species']=='Iris-versicolor']
virginica =df[df['Species']=='Iris-virginica']

print(setosa.describe())
print(versicolor.describe())
print(virginica.describe())

print(df.describe())


print("=============================")
print("=============================")

print("Read CSV using csv package")
print("=============================")
FILE = "E:\MSc Data Science\Data Science Techniques and Applications\Labs\Irisdata.csv"

setosa = [0,0,0,0,0]
versicolor = [0,0,0,0,0]
virginica = [0,0,0,0,0]

#Calculate total numbers of each species and sepal length and width and petal legnth and with
with open(FILE, 'r') as mycsvfile:
    dataset = csv.reader(mycsvfile, delimiter=',', quotechar='"')
    for row in dataset:
        #print rows as list of elements
        #print (row)
        if row[5] == "Iris-setosa":
            setosa[0] = setosa[0] + float(row[1])
            setosa[1] = setosa[1] + float(row[2])
            setosa[2] = setosa[2] + float(row[3])
            setosa[3] = setosa[3] + float(row[4])
            setosa[4] = setosa[4] + 1
        elif row[5] == "Iris-versicolor":
            versicolor[0] = versicolor[0] + float(row[1])
            versicolor[1] = versicolor[1] + float(row[2])
            versicolor[2] = versicolor[2] + float(row[3])
            versicolor[3] = versicolor[3] + float(row[4])
            versicolor[4] = versicolor[4] + 1
        elif row[5] == "Iris-virginica":
            virginica[0] = virginica[0] + float(row[1])
            virginica[1] = virginica[1] + float(row[2])
            virginica[2] = virginica[2] + float(row[3])
            virginica[3] = virginica[3] + float(row[4])
            virginica[4] = virginica[4] + 1

#Calculate means
setosa_mean = [setosa[0]/setosa[4],setosa[1]/setosa[4],setosa[2]/setosa[4],setosa[3]/setosa[4]]  
versicolar_mean = [versicolor[0]/versicolor[4],versicolor[1]/versicolor[4],versicolor[2]/versicolor[4],versicolor[3]/versicolor[4]]
virginica_mean = [virginica[0]/virginica[4],virginica[1]/virginica[4],virginica[2]/virginica[4],virginica[3]/virginica[4]]

# Calculate variances
setosa_var = [0,0,0,0]
versicolor_var = [0,0,0,0]
virginica_var = [0,0,0,0]
with open(FILE, 'r') as mycsvfile:
    dataset = csv.reader(mycsvfile, delimiter=',', quotechar='"')
    for row in dataset:
        if row[5] == "Iris-setosa":
            setosa_var[0] = setosa_var[0] + (float(row[1])-setosa_mean[0])**2
            setosa_var[1] = setosa_var[1] + (float(row[2])-setosa_mean[1])**2
            setosa_var[2] = setosa_var[2] + (float(row[3])-setosa_mean[2])**2
            setosa_var[3] = setosa_var[3] + (float(row[4])-setosa_mean[3])**2
        elif row[5] == "Iris-versicolor":
            versicolor_var[0] = versicolor_var[0] + (float(row[1])-versicolar_mean[0])**2
            versicolor_var[1] = versicolor_var[1] + (float(row[2])-versicolar_mean[1])**2
            versicolor_var[2] = versicolor_var[2] + (float(row[3])-versicolar_mean[2])**2
            versicolor_var[3] = versicolor_var[3] + (float(row[4])-versicolar_mean[3])**2
        elif row[5] == "Iris-virginica":
            virginica_var[0] = virginica_var[0] + (float(row[1])-virginica_mean[0])**2
            virginica_var[1] = virginica_var[1] + (float(row[2])-virginica_mean[1])**2
            virginica_var[2] = virginica_var[2] + (float(row[3])-virginica_mean[2])**2
            virginica_var[3] = virginica_var[3] + (float(row[4])-virginica_mean[3])**2
for i in range(0,4):
    setosa_var[i] = setosa_var[i]/setosa[4]
    versicolor_var[i] = versicolor_var[i]/versicolor[4]
    virginica_var[i] = virginica_var[i]/setosa[4]

#Print CSV results

print("Setosa")
print("======")
print("Setosa total = ", setosa[4])
print("Mean")
print("sepal lenth: ", setosa_mean[0] , "sepal width: ", setosa_mean[1], "petal lenth: ", setosa_mean[2], "petal width: ", setosa_mean[3])
print("Variance")
print("Sepal length:",setosa_var[0],"sepal width:",setosa_var[1],"petal length:",setosa_var[2],"petal width:",setosa_var[3])

print("Versicolor")
print("==========")
print("Versicolor total = ", versicolor[4])
print("Mean")
print("sepal lenth: ", versicolar_mean[0] , "sepal width: ", versicolar_mean[1], "petal lenth: ", versicolar_mean[2], "petal width: ", versicolar_mean[3])
print("Variance")
print("Sepal length:",versicolor_var[0],"sepal width:",versicolor_var[1],"petal length:",versicolor_var[2],"petal width:",versicolor_var[3])

print("Virginica")
print("=========")
print("Virginica total = ", virginica[4])
print("Mean")
print("sepal lenth: ", virginica_mean[0], "sepal width: ", virginica_mean[1], "petal lenth: ", virginica_mean[2], "petal width: ", virginica_mean[3])
print("Variance")
print("Sepal length:",virginica_var[0],"sepal width:",virginica_var[1],"petal length:",virginica_var[2],"petal width:",virginica_var[3])

plt.plot(setosa_mean,color="green",marker="o",linestyle="solid")
plt.plot(versicolar_mean,color="red",marker="o",linestyle="solid")
plt.plot(virginica_mean,color="blue",marker="o",linestyle="solid")
plt.show()


setosa_sl=[]
setosa_sw=[]
setosa_pl=[]
setosa_pw=[]
versicolor_sl=[]
versicolor_sw=[]
versicolor_pl=[]
versicolor_pw=[]
virginica_sl=[]
virginica_sw=[]
virginica_pl=[]
virginica_pw=[]
with open(FILE, 'r') as mycsvfile:
    dataset = csv.reader(mycsvfile, delimiter=',', quotechar='"')
    for row in dataset:
        #print rows as list of elements
        #print (row)
        if row[5] == "Iris-setosa":
            setosa_sl.append(row[1])
            setosa_sw.append(row[2])
            setosa_pl.append(row[3])
            setosa_pw.append(row[4])
        elif row[5] == "Iris-versicolor":
            versicolor_sl.append(row[1])
            versicolor_sw.append(row[2])
            versicolor_pl.append(row[3])
            versicolor_pw.append(row[4])
        elif row[5] == "Iris-virginica":
            virginica_sl.append(row[1])
            virginica_sw.append(row[2])
            virginica_pl.append(row[3])
            virginica_pw.append(row[4])
    
plt.scatter(setosa_pl,setosa_pw,color="green",marker="o")
plt.scatter(versicolor_pl,versicolor_pw,color="red",marker="o")
plt.scatter(virginica_pl,virginica_pw,color="blue",marker="o")
plt.xlabel("Petal length")
plt.ylabel("Petal width")
plt.show()

plt.scatter(setosa_sl,setosa_sw,color="green",marker="o")
plt.scatter(versicolor_sl,versicolor_sw,color="red",marker="o")
plt.scatter(virginica_sl,virginica_sw,color="blue",marker="o")
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.show()





