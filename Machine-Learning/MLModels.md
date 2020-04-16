Machine Learning Models Info

Data and Machine Learning
-------------------------
How data is used in Machine Learning is dependent on the ML task. There are two categories of learning: Supervised and Unsupervised. Class will focus on Supervised Learning.

Data
    - Up to now been interested in calculating aggregations (sum, min, max, count) grouped by chosen columns
    - Patterns/Relationships are uncovered
    - Machine Learning is about make pattern finding automatic

Machine Learning Data
    - Requires lots of data
    - Sensitive to bias if data is not 
        + representative of the task at hand
        + is imbalanced in the output labels
    - Prone to underfitting
        + model doesn't work for your data
        + unable to capture a relationship between the input values and the output target
    - Prone to overfitting
        + too little data
        + doesn't capture true relationships
        + has essentially memorized data
    - Data must be broken into 2 distinct groups
        + test data
        + train data

Test Data
    - The percent of the original dataset varies
    - Ranges from 20%  - 30%
    - Validates the Machine Learning model

Train Data
    - Remaing dataset is used here
    - Ranges from 70% - 80%
    - Trains the Machine Learning model

Test vs Train Data
    - Machine Learning model's score is compared
    - Overfitting
        + train score much greater than test score
        + model memorizes training data so it's totally lost on the test data
    - Underfitting
        + train score much smaller than it would be with more data
        + if score is really low then try to confirm online if other people could get much better scores than yours.
        + depends on problem, some tasks don't get above 70% other 50%


Supervised Machine Learning
---------------------------
Supervised Learning is any Machine Learning task were you need to predict a value (like tomorrow's stock price) or a category (hotdog vs nohotdog) given numeric inputs. The predicted value is learned in the training process. In training the free parameters of the Machine Learning model are iterativel tweaked to minimize the error between the predicted value and the known value. 

Terms used in ML when evaluating a model
    - Cost function
    - Mean Squared Error (MSE)
        + Regression problem
        + prediction is a real number value
        + Sum (predicted-true) over all data
        + Square result
    - Mean Average Error (MAE)
        + Classification problem
        + prediction is a categorical label
        + Correct Predictions / Total
    - False Positive Rate (FP)
        + wrong predictin
        + Predicted Cancer when there was No Cancer
    - False Negative Rate (FN)
        + wrong prediction
        + Predicted No Cancer when there was Cancer
    - True Positive Rate (TP)
        + correct prediction
        + Cancer
    - True Negative Rate (TN)
        + correct prediction
        + No Cancer
    - Precision (P)
        Compares True Positive Rate with False Positive Rate
        Formula: P = TP / (FP + TP)
    - Recall (R)
        Compares True Positive Rate with False Negative Rate
        Formula: R = TP / (FN + TP)
    - F1
        Harmonic mean of Precision and Recall
        Formula: 1/F1 = (1/P + 1/R)/2

Feature engineering
-------------------
Raw data is rarely useful out-of-the-box for Machine Learning. Even if every input is a number if there is a weak relationship between that input and the prediction then it is called a "non-informative" input. To create a high performing and robust Machine Learning model we want to maximize the number of informative inputs and drop non-informative ones.

Non-numeric inputs need to be dealt with in a special manner. Essentially the string needs to be converted into a number. There are a number of ways to do this which we'll explain the activity.
