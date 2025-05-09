# Evaluate the classifier performance in terms of accuracy, precision and recall
from sklearn import metrics
print("Accuracy:", metrics.accuracy_score(Y_test,Y_pred))
print("Precision:", metrics.precision_score(Y_test,Y_pred))
print("Recall:", metrics.recall_score(Y_test,Y_pred))


## Second model for predictiosn 

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

# Evaluate the classifier performance in terms of accuracy, precision and recall
from sklearn import metrics
print("Accuracy - GaussianNB:", metrics.accuracy_score(Y_test,Y_pred_GNB))
print("Precision - GaussianNB:", metrics.precision_score(Y_test,Y_pred_GNB))
print("Recall - GaussianNB:", metrics.recall_score(Y_test,Y_pred_GNB))

###########################



from sklearn.naive_bayes import GaussianNB
classifier_GNB = GaussianNB()
classifier_GNB.fit(X_train, Y_train)

# Now predict the target for the test data
Y_pred_GNB = classifier_GNB.predict(X_test)

print("MSE: ", 1 - mean_squared_error(Y_test, Y_pred_GNB))
print("RMSE: ", 1 - rmse_sklearn(Y_test, Y_pred_GNB))
print("R2: ", r2_score(Y_test, Y_pred_GNB))

#Display the plotted predictions 
#plot_predictions(Y_test, Y_pred_GNB)