from matplotlib import pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

import pandas as pd
from tabulate import tabulate

from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.model_selection import train_test_split

import time




features = ["mcg", "gvh", "lip", "chg", "aac", "alm1", "alm2"]


def countchar(dataset):
    count = 0;
    while dataset[count] != "\n":
        count = count + 1
    a = len(dataset[0:count])
    return a

def countline(dataset):
    count = 0
    for i in range(len(dataset)):
        if dataset[i:(i+1)] == "\n":
            count += 1
    return count

def clean(dataset):
    clean = dataset.split("\n")
    for i in range(len(clean)):
        clean[i] = clean[i].split(" ")
    copy = []
    for i in range(len(clean)):
        clean1 = []
        for j in range(len(clean[i])):
            if clean[i][j] != "":
                if clean[i][j][0] == '0':
                    clean[i][j] = float(clean[i][j])
                clean1.append(clean[i][j])
        copy.append(clean1)
    del copy[len(copy)-1]    
    return copy

def encode(dataset):
    columns = ["seqlabel", "mcg", "gvh", "lip", "chg", "aac", "alm1", "alm2", "classdist"]
    df = pd.DataFrame(dataset)
    df.columns = columns
    for row in df:
        if row in features:
            df[row] = df[row].astype(float)
    return df

def stringToFloat(x):
    temp = x.split(".")
    x = int(temp[0]) + (int(temp[1])/(10 ** len(temp)))    
    return x

def rankFeatures(df):
    X = df.iloc[:,1:8]
    Y = df.iloc[:,-1]
    model = ExtraTreesClassifier()
    model.fit(X,Y)
    feat_importances = pd.Series(model.feature_importances_, index = X.columns)  
    return feat_importances

def separator():
    print("\n")
    print("************************************************************")
    print("\n")

def main():
    
    # Reading ecoli dataset from text file and printing results
    
    file = "E:\MSc Data Science\Machine Learning\Coursework\ecoli.data"
    with open(file,'r') as datafile:
        dataset = datafile.read()
        
    file = "E:\MSc Data Science\Machine Learning\Coursework\ecoli.names"
    with open(file,'r') as datafile:
        names = datafile.read()
        
    print("Description of dataset")
    print(names)
    
    separator()
        
    print(len(dataset), "characters")
    print(countchar(dataset), "characters per line")
    print(countline(dataset), "lines")

    separator()
    
    # Cleaning dataset and labelling columns
    
    print("Dataset converted to DataFrame using Pandas")
    print("\n")
    df = encode(clean(dataset))
    print("\n")
    print("First five rows of dataset:")
    print("\n")
    print(df.head(5))
    print("\n")
    print("Last five rows of dataset:")
    print("\n")
    print(df.tail(5))
    print("\n")
    print("Datatypes of each column (feature):")
    print("\n")
    print(df.dtypes)
    
    separator()
    
    # Identification of classification groups (response variable)
    
    print("Classes of response")
    print("\n")
    number_of_classes = df.groupby("classdist").size()
    print("Number of classes:", number_of_classes)
    
    separator()
    
    # Identification of importance of features (x variables)
    
    print("Feature importance evaluation")
    print("\n")
    featsel1 = rankFeatures(df).sort_values()
    featsel2 = rankFeatures(df).sort_values()
    featsel3 = rankFeatures(df).sort_values()
    print("Feature selection 1:")
    print("\n")
    print(featsel1)
    print("\n")
    print("Feature selection 2:")
    print("\n")
    print(featsel2)
    print("\n")
    print("Feature selection 3:")
    print("\n")
    print(featsel3)
    plt.plot(featsel1)
    plt.plot(featsel2)
    plt.plot(featsel3)
    plt.xlabel("Feature")
    plt.ylabel("Relative importance")
    plt.show()
    
    # Bagging of feature importance evaluation results
    
    print("\n")
    print("Bagging of Feature importance evaluation results")
    print("\n")
    
    features_bag = []
    for i in range(len(features)):
        feature_rank = rankFeatures(df).sort_index()
        features_bag.append(feature_rank)
    features_bag = pd.DataFrame(features_bag)
    
    features_mean = []
    for i in features:
        features_mean.append(features_bag[i].mean())    
    
    plt.bar(features,features_mean)
    plt.xlabel("Features")
    plt.ylabel("Relative Importance (Reduced Executional Variance)")
    plt.show()

    separator()
    
    # Creating a model for a decision tree
     
    print("Create Decision Tree Model using most important feature only")
    print("\n")
    
    maxfeature_val = 0
    maxfeature_label = ""
    for i in range(len(features)):
        if features_mean[i] > maxfeature_val:
            maxfeature_val = features_mean[i]
            maxfeature_label = features[i]
        else:
            continue
    
    Y = df.loc[:,"classdist"]
    X = df.loc[:,maxfeature_label]
    X = X.values.reshape(-1,1)
    
    test = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9] 
    accuracy = []
    for i in test:
        xtrain, xtest, ytrain, ytest = train_test_split(X,Y,test_size = i,random_state = 1)    
        dftree = tree.DecisionTreeClassifier(max_depth = len(number_of_classes))
        dftree.fit(xtrain,ytrain)
        y_predict = dftree.predict(xtest)
        accuracy.append(accuracy_score(ytest,y_predict))
    plt.plot(test,accuracy)
    plt.xlabel("Test size")
    plt.ylabel("Accuracy rate")
    plt.show
    
    
    besttestsize = 0
    bestaccuracy = 0
    for i in range(len(accuracy)):
        if accuracy[i] > bestaccuracy:
            bestaccuracy = accuracy[i]
            besttestsize = test[i]
        else:
            continue
        
    print("Best Test size = ",besttestsize)
    print("Accuracy rate: ",bestaccuracy)
    print("Most important feature = ",maxfeature_label)
     
    separator()
    
    # Having determined the best test size with one feature, create model using more than one feature
    
    print("Models using more than one feature to determine maximum highest accuracy rate")
    print("\n")
    
    threshold = []
    bestaccuracy = []
    maxfeatarray = []
    print("Best Test size = ",besttestsize,"\n")
    mfv = maxfeature_val
    
    for i in range(1,9):
           
        maxfeature_threshold = mfv * (i / 10)
        maxfeature_val = []
        maxfeature_label = []
        
        
        for j in range(len(features)):
            if features_mean[j] > maxfeature_threshold:
                maxfeature_val.append(features_mean[j])
                maxfeature_label.append(features[j])
            else:
                continue
        
        Y = df.loc[:,"classdist"]
        X = df.loc[:,maxfeature_label]
        X = X.values.reshape(336,len(maxfeature_label))
        
        test = 0.3
        xtrain, xtest, ytrain, ytest = train_test_split(X,Y,test_size = test,random_state = 1)    
        dftree = tree.DecisionTreeClassifier(max_depth = len(number_of_classes))
        dftree.fit(xtrain,ytrain)
        y_predict = dftree.predict(xtest)
        bestaccuracy.append(accuracy_score(ytest,y_predict))
        maxfeatarray.append(maxfeature_label)
        threshold.append(maxfeature_threshold)

    print(tabulate(zip(threshold,bestaccuracy,maxfeatarray), headers = ["Threshold","Accuracy rate","Features used"]  ))
    
    plt.figure(0) 
    plt.plot(threshold,bestaccuracy)
    plt.xlabel("Threshold")
    plt.ylabel("Accuracy Rate")
    plt.show()
    
    separator()
    
    # Computational Cost
    
    print("Assessing Computational Cost of using four and five features")
    print("\n")
    
    for f in range(1,4):
        compcost = []
        threshold = []
        bestaccuracy = []
        maxfeatarray = []
        timearray = []
        
        for i in range(1,9):
                    
            maxfeature_threshold = mfv * (i / 10)
            maxfeature_val = []
            maxfeature_label = []
            
            for j in range(len(features)):
                if features_mean[j] > maxfeature_threshold:
                    maxfeature_val.append(features_mean[j])
                    maxfeature_label.append(features[j])
                else:
                    continue
            
            Y = df.loc[:,"classdist"]
            X = df.loc[:,maxfeature_label]
            X = X.values.reshape(336,len(maxfeature_label))
            
            test = 0.3
            if len(maxfeature_label) == 4 or len(maxfeature_label) == 5:
                starttime = time.time()
                xtrain, xtest, ytrain, ytest = train_test_split(X,Y,test_size = test,random_state = 1)    
                dftree = tree.DecisionTreeClassifier(max_depth = len(number_of_classes))
                dftree.fit(xtrain,ytrain)       
                endtime = time.time()
                y_predict = dftree.predict(xtest)
                bestaccuracy.append(accuracy_score(ytest,y_predict))
                maxfeatarray.append(maxfeature_label)
                threshold.append(maxfeature_threshold)
                endtime = time.time()
                timearray.append(endtime - starttime)
                
                
        print("Model",f,":")
        compcost = zip(threshold,timearray,bestaccuracy,maxfeatarray)
        print (tabulate(compcost,headers = ["Threshold","Time","Accuracy","Features Used"]))
                
        fig = plt.figure(f)
        ax = fig.gca(projection='3d')
        ax.plot(threshold, bestaccuracy, timearray, label='parametric curve')
        ax.set_xlabel('Threshold')
        ax.set_ylabel('Accuracy Rate')
        ax.set_zlabel('Computational Cost')
        ax.legend()
        plt.show()
        
        
        
    
    


main()
