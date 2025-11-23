# Classification:

- Algorithms used to train classification models calculate probability values for class assignment
- evaluation metrics used to assess model performace compare predicted classes to actual classes

- predicts true / false
- logistic regression - the function produced by the algorithm describes the probability of y being true for a given value of x.

f(x) = P(y = 1| x)

- threshold value at which the model predicts true / false

Evaluating the model:
- confusion matrix
- TN, TP, FN, FP
- arrangement of confusion matrix is such that the correct predictions falls on the diagonal from top left to bottom right - if color intensity was used to indicate the number of predictions in each cell, a quick glance at a model that predicts well should reveal a deeply shaded diagonal trend.

- Accuracy: the proportion of predictions the model got right: ( TN + TP ) / (TN + TP + FN+ FP)

- Recall: propotion of postive cases that the model identified correctly = TP / (TP + FN)

- Precision: propertion of predicted positive cases where true label is actually positive: TP / (TP + FP)

- F1 Score: ( 2 * Precision * Recall) / (Precision + Recall)
    - overall metric that combnes precision and recall

AUC - Area under the curve:
- Another name for recall - TPR, equivalent metric - FPR = FP (FP + TN)