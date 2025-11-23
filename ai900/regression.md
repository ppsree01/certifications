# Regression

- models trained to predict numeric label values based on training data that includes both features and known labels

- Key elements of training process:
    - Split the training data, hold back a part of it for testing the model
    - Use an algorithm to train the model 
    - Use the validation you held back to test the model by predicting labels for the features
    - Compare actual and predicted values 

- Evaluating a regression model:
    - Regression evaluation metrics:
        - Mean Absolute Error ( MAE ) - absolute error for each prediction - summarised for the whole validation set - this is the mean average of absolute errors
        - Mean squared error - mean of squared absolute values (takes all discrepencies )
        - Root mean squared error - square root of MSE ( magnitude of errors )
        - Coefficient of determination (R2) measures the proportion of variance in the validation results that can be explained by the model, as opposed to some anomolous aspect og validation data

        R2 = 1 - Sigma(label - predicted)2 / Sigma(label - MAE)2

        Value ranges between 0 and 1
        The closer this value is to 1 -> the closer the model fits the validation data
        