# Week 1

Install matplotlib, numpy and csv on your systems using 
```
pip install matplotlib, numpy, csv
```

## NP.py

Go through the content of this file as most of the functions we'll be using in numpy are defined and the workings are explained.

**Remember you'll be using pip or pip3 depending on your python versions installed, just make sure you install it for python3 if you're running multiple versions of python on one system**

## Linear regression with one variable

Once you've installed, give yourself a moment and go through the test data 'ex1data.txt'.

You'll be using the above file for the first exercise, which is implementing linear regression with one variable.

The main components of the first part are given as below: 
* #### singleVariableMain.py
The main file for the program, which will be using the other files to run the program. Go through it once to see how we load in the data, visualize it, and preprocess it for training.

* #### computeCost.py
The main file for computing the cost between predicted and actual values. It's your job to complete this file to get the desired result, as mentioned in the comments whitin the file.

* #### gradientDescent.py
The main file for actually implementing the gradient descent algorithm. It's your job (Again) to complete this file to get the desired results as mentioned in the comments within the file.

In order to get the desire result, navigate the the directory containing the files i.e.:
```
cd your-path-to-the-folder/Week2
```
And run the file from there 

## Linear regression with two variables

You'll be using the data in 'ex1data2.txt' for this exercise.
* #### multiVariableMain.py
The main file for this exercise which will use the other files to run the program. Go through it to see how multiple features are read in and accoomodated for by the program. 
* #### featureNormalization.py
This is the only file you'll need to edit for the program to work. The task you need to complete will be mentioned within the file itself in the form of comments.

In order to get the desire result, navigate the the directory containing the files i.e.:
```
cd your-path-to-the-folder/Week2
```
And run the file from there 
