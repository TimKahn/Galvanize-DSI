Linear Regression
   * What type of values does linear regression predict?
   * What relationship does linear regression assume?  How would you write it?
   Ax = y.
   * What is the error/loss function for LR?  How do you solve for the coefficients?
   * How do you interpret the coefficients in a linear regression?
   * What assumption are necessary for a linear regression model to be valid?
    Continuous (linear) response, normally distributed residuals, homoskedasticity...
   * What are the advantages/disadvantages of linear regression?

Cross Validation
   * What is cross validation?
   * Why is it used?
   * Explain step-by-step how one would take a data set, tune it, and
     then predict on new data.  Use kFold cross validation.

Regularization
   * What is regularization in general?
   * How, and why, does it work?
   * Name two different types of shrinkage one might use.  Contrast them.

Logistic Regression
   * In what situations would you use logistic regression instead of linear?
   -When we'd like to classify data, rather than predict a (linear) response to a change in a predictor.
   * What is a link function?
   Relates a linear combination to the mean of the response.
   * What are odds, and how does one go from odds to probabilities?
   * How does one interpret the coefficients in a logistic regression?

Review Week 4

Gradient Descent

Curse of Dimensionality
   * What is the Curse of Dimensionality?
   * Why does it occur?
   * How can you prevent it?
   Curse of dimensionality refers to the decline in model performance as feature space grows in dimension.


Decision Trees
   * Explain how a decision tree is built.
   * In a node, how do you determine which feature to split on?
   Split on feature that gives greatest information gain, which is determined from the disorder metric.
   * Explain the different "disorder" metrics for regression/classification.
   RSS vs Gini or Entropy.
   * What are some advantages/disadvantages of Decision trees?
   Deterministic.  Fast predictions once built.  Flexible, but prone to overfitting.

kNNs
   * Explain how kNN works.
   * What are advantages/disadvantages of kNN?
   Expensive.

Random Forests & Boosting
   * Compare and contrast Random Forests & Boosting (table)
