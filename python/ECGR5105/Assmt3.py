# Terrence Jackson
# Intro to Machine Lerning
# UNCC - Spring 2025
# Final Project  


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Split the dataset into training and test data. Training data will be used to
# train a logistic model and test data will be used to validate our model.

# Load dataset 
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
breast = load_breast_cancer()
X = breast.data
print(X.shape)
Y = breast.target

breast_input = pd.DataFrame(X)
breast_input.head()

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.20, random_state=0)

# Feature scaling to scale data between 0 and 1.
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)

# Import Logistic Regrsession and train the model on the training data

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, Y_train)

# Now predict the target for the test data
Y_pred = classifier.predict(X_test)
print(Y_pred.size, Y_test.size)

# Performance evaluation: we can use confusion matrix to see the performance of the model

from sklearn.metrics import confusion_matrix
cnf_matrix = confusion_matrix(Y_test, Y_pred)
cnf_matrix

# Visualize the confusion matrix using a heatmap
import seaborn as sns
class_names = [0,1]
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix), annot = True, fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix')
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
#plt.show(block=False)  
#plt.pause(2.5)

# Evaluate the classifier performance in terms of accuracy, precision and recall
from sklearn import metrics
print("Accuracy:", metrics.accuracy_score(Y_test,Y_pred))
print("Precision:", metrics.precision_score(Y_test,Y_pred))
print("Recall:", metrics.recall_score(Y_test,Y_pred))



## Problem 2
# Import Naive Gaussian Bayes and train the model on the training data

from sklearn.naive_bayes import GaussianNB
classifier_GNB = GaussianNB()
classifier_GNB.fit(X_train, Y_train)

# Now predict the target for the test data
Y_pred_GNB = classifier_GNB.predict(X_test)
print(Y_pred_GNB)

# Performance evaluation: we can use confusion matrix to see the performance of the model

from sklearn.metrics import confusion_matrix
cnf_matrix_GNB = confusion_matrix(Y_test, Y_pred_GNB)
cnf_matrix_GNB

# Visualize the confusion matrix using a heatmap
import seaborn as sns
class_names = [0,1]
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix_GNB), annot = True, fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix')
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
#plt.show(block=False)  
#plt.pause(2.5)

# Evaluate the classifier performance in terms of accuracy, precision and recall
from sklearn import metrics
print("Accuracy - GaussianNB:", metrics.accuracy_score(Y_test,Y_pred_GNB))
print("Precision - GaussianNB:", metrics.precision_score(Y_test,Y_pred_GNB))
print("Recall - GaussianNB:", metrics.recall_score(Y_test,Y_pred_GNB))

##---Gaussian Model looks to be slightly less accurate---##

## Problem 3
# Import SVM Classifier and model on the training data

from sklearn.svm import SVC
classifier_SVM = SVC(kernel='linear', C=1.0)
classifier_SVM.fit(X_train, Y_train)

# Now predict the target for the test data
Y_pred_SVM = classifier_SVM.predict(X_test)
print(Y_pred_SVM)

# Performance evaluation: we can use confusion matrix to see the performance of the model

from sklearn.metrics import confusion_matrix
cnf_matrix_SVM = confusion_matrix(Y_test, Y_pred_SVM)
cnf_matrix_SVM

# Visualize the confusion matrix using a heatmap
import seaborn as sns
class_names = [0,1]
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix_SVM), annot = True, fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix')
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
#plt.show(block=False)  
#plt.pause(2.5)

# Evaluate the classifier performance in terms of accuracy, precision and recall
from sklearn import metrics
print("Accuracy - SVM:", metrics.accuracy_score(Y_test,Y_pred_SVM))
print("Precision - SVM:", metrics.precision_score(Y_test,Y_pred_SVM))
print("Recall - SVM:", metrics.recall_score(Y_test,Y_pred_SVM))

##---SVM Model looks to be slightly more accurate than the other models---##

## Problem 4
# Import SVM Classifier and model on the training data

from sklearn.decomposition import PCA
pca = PCA(n_components=.65) # Retain 95% of variance
X_pca_train = pca.fit_transform(X_train)


##### -- NEW STUFF  FROM PCA COLAB  
#####
print(f"Original shape: {X_train.shape}")
print(f"PCA-reduced shape: {X_pca_train.shape}")

# Plot explained variance
plt.figure(figsize=(6, 4))
plt.plot(np.cumsum(pca.explained_variance_ratio_), marker='o')
plt.xlabel('Number of components')
plt.ylabel('Cumulative explained variance')
plt.title('Variance Explained by PCA Components')
plt.grid(True)
plt.show()

##### ---- END NEW STUFF FROM PCA COLAB 

X_pca = sc_X.fit_transform(X_pca_train)
print(X_pca)

# Import Logistic Regrsession and train the model on the training data

from sklearn.linear_model import LogisticRegression
classifier_PCA = LogisticRegression(random_state=0)
classifier_PCA.fit(X_pca, Y_train)

Y_pred_PCA = classifier.predict(X_test)
print(Y_pred_PCA)

# Performance evaluation: we can use confusion matrix to see the performance of the model

from sklearn.metrics import confusion_matrix
cnf_matrix_PCA = confusion_matrix(Y_test, Y_pred_PCA)
cnf_matrix_PCA

# Visualize the confusion matrix using a heatmap
import seaborn as sns
class_names = [0,1]
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix_PCA), annot = True, fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix')
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
#plt.show(block=False)  
#plt.pause(2.5)

# Evaluate the classifier performance in terms of accuracy, precision and recall
from sklearn import metrics

print("Accuracy - PCA:", metrics.accuracy_score(Y_test,Y_pred_PCA))
print("Precision - PCA:", metrics.precision_score(Y_test,Y_pred_PCA))
print("Recall - PCA:", metrics.recall_score(Y_test,Y_pred_PCA))
print("F1 score - PCA:", metrics.f1_score(Y_test,Y_pred_PCA))  



