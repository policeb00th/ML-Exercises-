# Logistic Regression
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


## Will add problems for regularization and logistic regression using sklearn.


