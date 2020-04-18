import numpy as np
def featureNormalization(X):
    """
    Take in numpy array of X values and return normalize X values,
    the mean and standard deviation of each feature
    """
    mean=np.mean(X)
    std=np.std(X)
    
    X_norm = (X - mean)/std
    
    return X_norm