# Machine Learning:

- intersection of two disciplines:
    - data science
    - software engineering

- goal is to use data to create a predictive model that can be incorporated into a software app / service.
- achieving this goal requires collaboration between data scientists who explore and prepare this data before using it train the model, and software engineers that use this model in app where its used to predict new data values - inferencing

- fundamental idea - use past data/observations to predict new unknown outcomes / values

# Machine Learning Models:
- ml model is a software app that encapsulates a fn to calculate an output value based on one or more input values
- training - process of defining that function
- inferencing - using that function to predict unknown outcomes
- features - attributes 
- label - the output / known value

- features - x, label - y
- an observation usually contains multiple feature values - so x is a vector - an array with multiple values - [x1, x2, x3, x4...]

Icecream sales scenario:
- features - temperature, rainfall, windspeed
- label - number of icecreams sold

Medical scenario:
- features - weight, glucose level, 
- label - yes ( diabetic ), no

Antarctic Research Scenario:
- features - length of flippers, width of bill
- label - 0 Adelie , 1 Gentoo, 2 Chinstrap

- An algorithm is applied to the data to try to establish / determine the relation between feature and label
- fit the data to a function
- result of the algorithms is a model that encapsulates calculation derived by the algorithm as a function - 
y = f(x)
- inferencing - the output is a predicted value - we refer to y-hat
