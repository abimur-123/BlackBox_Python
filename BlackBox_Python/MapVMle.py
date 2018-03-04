import pandas as pd
def getMLE(distribution,column):
    """
    compute the log likelihood of data given the distribution

    Args:
    distribution: type of distribution of the data. for example (binomial, poisson). Support for 2 as of now.
    column: the list of numeric data over which we perform the maximum likelihood

    Return:
    the log likelihood of the data
    """
    if(isinstance(distribution,str) == False):
        raise TypeError("Not a string value")

    if(isinstance(column,list) == False):
        raise TypeError("Not a list")

    pass

def getMAP(column,prior = None):
    """
    calculate the maximum a posteriori (MAP) estimation. MAP estimate is the mode of the posterior distribution.
    MAP is proportional to likelihood function and prior.

    Args:
    column: the column is a list of numerical binomial data. Support for only binomial currently.
    We will be using Beta-Binomial Conjugacy as an example for first time learners.
    prior: prior assumptions of the data

    Return:
    the MAP estimate of the posterior.
    """
    if(isinstance(column,list) == False):
        raise TypeError("Not a list")

    pass
