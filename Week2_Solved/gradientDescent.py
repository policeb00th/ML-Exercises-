import numpy as np
from computeCost import computeCost
#returns updated value of theta
#Two functions doing the same thing
'''def gradientDescent(X, y, theta, alpha, iterations):
    # A.T implies using transpose of the matrix A
    m=len(y)
    for i in range(iterations):
        temp = np.dot(X, theta) - y
        temp = np.dot(X.T, temp)            #updating temp variable
        theta = theta - (alpha/m) * temp
        if(i%100==0):
            print('Updated value of theta after ',i,' iterations is: ',theta)
    return theta'''

def gradientDescent(X,y,theta,alpha,num_iters):
    """
    Take in numpy array X, y and theta and update theta by taking num_iters gradient steps
    with learning rate of alpha
    
    return theta updated
    """
    
    m=len(y)
    for i in range(num_iters):
        predictions = np.dot(X,theta)
        error = np.dot(X.T,(predictions -y))
        descent=alpha * 1/m * error
        theta= theta-descent
        if(i%100==0):
            print('Cost function after ',i,' iterations is ', computeCost(X,y,theta))
        
    return theta