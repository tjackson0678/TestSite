# Evaluate the classifier performance in terms of accuracy, precision and recall
from sklearn import metrics
print("Accuracy - GaussianNB:", metrics.accuracy_score(Y_test,Y_pred_GNB))
print("Precision - GaussianNB:", metrics.precision_score(Y_test,Y_pred_GNB))
print("Recall - GaussianNB:", metrics.recall_score(Y_test,Y_pred_GNB))
