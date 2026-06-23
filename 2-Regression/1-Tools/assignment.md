# Regression with Scikit-learn

## Instructions

Take a look at the [Linnerud dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_linnerud.html#sklearn.datasets.load_linnerud) in Scikit-learn. This dataset has multiple [targets](https://scikit-learn.org/stable/datasets/toy_dataset.html#linnerrud-dataset): 'It consists of three exercise (data) and three physiological (target) variables collected from twenty middle-aged men in a fitness club'.

In your own words, describe how to create a Regression model that would plot the relationship between the waistline and how many situps are accomplished. Do the same for the other datapoints in this dataset.

## Rubric

| Criteria                       | Exemplary                           | Adequate                      | Needs Improvement          |
| ------------------------------ | ----------------------------------- | ----------------------------- | -------------------------- |
| Submit a descriptive paragraph | Well-written paragraph is submitted | A few sentences are submitted | No description is supplied |

## My Answer

To build a regression model for the Linnerud dataset, I would first import the necessary libraries — numpy, matplotlib, and sklearn. Then I would load the dataset, setting X as the waistline measurements (input feature) and y as the number of situps completed (target). Next I would split the data into four variables — X_train, X_test, y_train, and y_test — using a 67/33 train/test split. I would then train the model using model.fit(X_train, y_train) so it learns the relationship between waistline and situps. After training, the model would predict situp values using model.predict(X_test), storing results in y_pred. Finally I would compare y_pred against y_test to evaluate accuracy, and plot the results using matplotlib — black dots for real data, blue line for the model's predictions.