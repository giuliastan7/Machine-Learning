# Machine-Learning
this project uses a dataset of heart disease data to train 
a logistic model that can make predictions about whether a person is sick or not, based on medical characteristics provided as input data.
Importing Libraries: At the beginning of the project, the necessary libraries are imported, such as NumPy for mathematical operations, 
Pandas for data manipulation and read/write functions,
and various modules from scikit-learn for machine learning.

Uploading the Data: The heart disease dataset is uploaded from a file called data.csv.

Viewing the Data: The first few rows of the data (data_heart.head()) and the last few rows (data_heart.tail()) are displayed to get an idea of what the data looks like.

Data Information: data_inima.info() provides information about the data types and whether there are any missing values in the dataset.

Missing Data Check: date_inima.isnull().sum() counts how many missing values there are in each column of the dataset.

Statistical Description of Data: data_inima.describe() provides basic statistics about the distribution of the data (such as median, standard deviation, etc.).

Target Variable Analysis: data_inima["target"].value_counts() displays how many examples of each class of the target variable exist in the dataset. 
In this case, there appear to be two classes (0 and 1), suggesting a binary classification problem.

Data Separation: The predictor variable (X) and the target variable (Y) are defined by removing the "target" column.

Splitting Data into Training and Test Sets: The train_test_split function is used to split the data into training and test sets. Approximately 80% of the data is used
for training and 20% for testing.

Logistic Regression Model Training: LogisticRegression() from scikit-learn is used to initialize a logistic model and model.fit() to train it.

Model Evaluation: The accuracy of the model is evaluated on the training and testing datasets using accuracy_score.

Predictions Using the Trained Model: A new example is defined in the input_data variable, then prepared for use in the model.
It is transformed into a numpy array, then a prediction is made using the logistic model. The result is then displayed and interpreted: 0 means the person is not sick, and 1 means the person is sick.
