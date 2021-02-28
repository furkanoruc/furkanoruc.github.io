#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 03:40:03 2021

@author: furkanoruc
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 17:10:47 2020

@author: furkanoruc
"""

import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import seaborn as sns
from sklearn.metrics import (confusion_matrix, recall_score, precision_score, roc_auc_score,
                                accuracy_score, f1_score, plot_confusion_matrix, confusion_matrix,
                                roc_curve, auc)
"""

dataset = pd.read_csv('RESULTS-Area1_Mart_Nisan_Mayis_2014.csv',sep=',')

filenames = ['RESULTS-Area1_Aralik_2014_Ocak_Subat_2015.csv',
             'RESULTS-Area2_Aralik_2014_Ocak_Subat_2015.csv',
             'RESULTS-Area3_Aralik_2014_Ocak_Subat_2015.csv',
             'RESULTS-Area4_Aralik_2014_Ocak_Subat_2015.csv',
             'RESULTS-Area5_Aralik_2014_Ocak_Subat_2015.csv',
             'RESULTS-Area6_Aralik_2014_Ocak_Subat_2015.csv',
             'RESULTS-Area7_Aralik_2014_Ocak_Subat_2015.csv',
             'RESULTS-Area8_Aralik_2014_Ocak_Subat_2015.csv',
             'RESULTS-Area9_Aralik_2014_Ocak_Subat_2015.csv',
             'RESULTS-Area10_Aralik_2014_Ocak_Subat_2015.csv',
             'RESULTS-Area11_Aralik_2014_Ocak_Subat_2015.csv',
             'RESULTS-Area12_Aralik_2014_Ocak_Subat_2015.csv',
             'RESULTS-Area13_Aralik_2014_Ocak_Subat_2015.csv']


for file in filenames:
    df = pd.read_csv(file,sep=',')
    dataset = dataset.append(df)
"""

backuup_dataset = dataset
backup_dataset = backuup_dataset

dataset = dataset.drop_duplicates()

dataset = dataset.dropna()

dataset.head(10)

X = dataset.iloc[:, lambda dataset: [1,3]].values

R = dataset.iloc[:, 10].values

X_train, X_test, Y_train, Y_test = train_test_split(X, R, test_size = 0.25, random_state = 14)



X_test.shape

#KNN Implement

def KNeighbors(X, y, X_test, y_test):
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import roc_curve, roc_auc_score, accuracy_score, plot_confusion_matrix, auc
    import matplotlib.pyplot as plt
    accuracy_score_holder = []
    misclassified_sample_count = []
    precision_score_holder = []
    roc_auc_score_holder = []
    for i in range (7,8):
        knn=KNeighborsClassifier(n_neighbors=i, p=2, metric='minkowski') 
        knn.fit(X, y)
        myprediction_knn = knn.predict(X_test)
        accuracy_score_holder.append(accuracy_score(y_test, myprediction_knn))
        misclassified_sample_count.append((y_test != myprediction_knn).sum())
        roc_auc_score_holder.append(roc_auc_score(y_test, myprediction_knn))
        k = knn.predict(X_test)
        precision = precision_score(y_test, myprediction_knn, average = 'macro')
        recall = recall_score(y_test, myprediction_knn, average = 'macro')
        i = i + 1
    #print("Accuracy Score:", accuracy_score_holder)
    #print("Precision Score:", precision_score_holder)
    #print("Misclassified samples:", misclassified_sample_count)
    #print("ROC - AUC Score:", roc_auc_score_holder)
    plot_confusion_matrix(knn, X_test, y_test)
    plt.show()
    
    
    return accuracy_score_holder[0], roc_auc_score_holder[0], misclassified_sample_count[0], precision, recall

knn_accuracy, knn_roc_auc, knn_misclassified_count, knn_precision, knn_recall = KNeighbors(X_train, Y_train, X_test, Y_test)

violation_check_distribution = dataset["Violation Check"].value_counts()


def perceptron(X, y, X_test, y_test):
    from sklearn.linear_model import Perceptron
    from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve, plot_confusion_matrix, auc
    import matplotlib.pyplot as plt

    for i in range (30,31):
        myperceptron = Perceptron(penalty = 'elasticnet', max_iter = i, eta0 = 0.001, random_state = 60)
        myperceptron.fit(X, y)
        myprediction_perceptron = myperceptron.predict(X_test)
        precision = precision_score(y_test, myprediction_perceptron, average = 'macro')
        recall = recall_score(y_test, myprediction_perceptron, average = 'macro')
        #print(accuracy_score(y_test,myprediction_perceptron))
        
        #print("Accuracy Score: ", accuracy_score(y_test,myprediction_perceptron))
        #print("Number of Misclassified Samples: ", (y_test != myprediction_perceptron).sum())
        #print("ROC - AUC Score:", roc_auc_score(y_test, myprediction_perceptron))

    plot_confusion_matrix(myperceptron, X_test, y_test)
    plt.show()
    
    return accuracy_score(y_test,myprediction_perceptron), roc_auc_score(y_test, myprediction_perceptron), (y_test != myprediction_perceptron).sum(), precision, recall 


perceptron_accuracy, perceptron_roc_auc, perceptron_misclassified_count, perceptron_precision, perceptron_recall = perceptron(X_train, Y_train, X_test, Y_test)


from package import (data_balancer, MultiLayerPerceptron, softmax, sigmoid, Loss_Perceptron,Weight_Initialization,
                        KNeighbors, forest, svm, perceptron)


mlp_accuracy_train, mlp_accuracy_test, w1,w2,b1,b2,classes_train, classes_test = MultiLayerPerceptron(X_train, Y_train, X_test, Y_test, hidden_layer_units=100, alpha=0.03, epoch=10)


mlp_recall = recall_score(Y_test, classes_test, average = 'macro')
mlp_precision = precision_score(Y_test, classes_test, average = 'macro')
mlp_roc_auc = roc_auc_score(Y_test, classes_test)


f, ax = plt.subplots(1,2,figsize=(12,6))
sns.heatmap(confusion_matrix(Y_test, classes_test));
sns.heatmap(confusion_matrix(Y_train, classes_train), fmt='.0f', annot=True,ax=ax[0],
xticklabels=[0,1], yticklabels=[0,1], cmap = 'Oranges');
plt.show()


random_forest_accuracy, random_forest_Roc_Auc, random_forest_Misclassified_Count, random_forest_precision = forest(X_train, Y_train, X_test, Y_test)


#Some Desc Stat
length_mean = dataset.iloc[:,0].mean()
speed_mean = dataset.iloc[:,2].mean()

plt.hist(dataset.iloc[:,2], bins = 0.6);
plt.show()



plt.hist2d(dataset.iloc[:,0], dataset.iloc[:,2], bins=30, cmap='Blues')








