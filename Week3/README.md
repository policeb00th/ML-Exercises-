# Week 3
Install scipy and sklearn on your system using 
```
pip install scipy, sklearn
```
## Logistic Regression

Once the above is installed, take a moment to go through the file 'ex2data1.txt' as it'll be containing the text data we'll be using for this exercise
The first column represents the marks of students in Exam 1 and the second oclumn represents the marks of students in Exam 2. The third column is a 1 or 0 valued column, indicating whether the student was selected in the program or not.

The main components of  the file are given below:
* __logisticmain.py__
The main file for the program, which will be using the other files to run the program. Go through it once to see how we load in the data, visualize it, and preprocess it for training. This time we'll be using the _minimize_ function provided by **scipy** to help the computer determine the best parameters for our model by itself.

* __loadData.py__
The file that contains the function for loading the data into the program, it's been completed already so you can see how we load data here, no need to edit it.

* __plotData.py__
The file that contains the function for plotting the data. It's been separated so as to allow us to plot multiple times if we want to.

* __costFunction.py__
The file that contains the cost function and gradient descend algorithms that need to be completed by you

* __sigmoid.py__
The file that contains the function for applying sigmoid to a numpy array. **Make sure you complete this file first before proceeding to the costFunction file.**


## Regularization
Take a moment to go through the data in 'ex2data2.txt' as that is the data we'll be using for the regularization problem.
Here the data is shown of whether a microchip is of quality or not.
The first column contains the results of tests it underwent for test 1.
The second column contains the results of tests it underwent for test 2.
The third column shows whether it was selected or rejected.

The components for the exercise is given below:

* __regularizationmain.py__
The main file for the program, which will be using other files to  run the program.
An important difference is the use of feature mapping to increase the number of features. This is done to generate more features from existing ones, since the data we're fitting is non linear hence a line will never be able to fit it.
To enable this, we include the features and their polynomials raised to the sixth power as features too.

* __costFunctionReg.py__
The file contains the cost function that needs to be completed by you, keep in mind to use the regularization forumla.
The gradient function has already been completed for your ease.

# Sklearn implementation
The Sklearn libary is a boon to the community of machine learning, as it tremendously simplify the amount of code we have to write to achieve an accurate model. 
* __sklearn_log.py__
Contains the sklearn implementation of the Logistic regression problem we've implemented. Please go through it as it'll show you how our vast and multi file program reduces to merely 20 lines of code. Sklearn by default takes care of a lot of things for us, but allows us to customise functions as per our need. 
Read the documentation about sklearn and try implemting our previous exercises using sklearn


