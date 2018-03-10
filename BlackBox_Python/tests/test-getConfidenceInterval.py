"""
Confidence Interval Tests(frequentist approach)
"""

import pytest
import numpy as np
from BlackBox_Python import ci

#sample vector
sample=np.array([1,3,4,5])


#check input
def test_input():
    '''
    check if the input is valid for getConfidenceInterval()
    '''
    msg1='Input data must be numpy array with one column only'
    with pytest.raises(TypeError,match=msg1):
        ci.getConfidenceInterval(np.array([1,2,3],[2,3,4]))

    msg2='need to pass in a dataframe'
    with pytest.raises(TypeError,match=msg2):
        ci.getConfidenceInterval()

    #valid dataframe must have at least 1 observations
    assert sample.shape[0]>0

    #valid dataframe must include two columns only
    assert len(sample.shape)==1

    #check if column2 is numeric
    assert sample.dtype==np.int64 or sample.dtype==np.float64

def test_output():
    '''
    check if the output interval is valid
    '''

    #output is a list with two elements
    assert len(ci.getConfidenceInterval(sample))==2

    #the lower bound of confidence interval must be larger than the min of data
    assert ci.getConfidenceInterval(sample)[0]>=sample.min()
    #the upper bound of confidence interval must be smaller than the max of data
    assert ci.getConfidenceInterval(sample)[1]<=sample.max()

    #check if the interval is correct
    expected_lower=1.576331
    expected_upper=4.923668

    assert abs(getCredibleInterval(sample)[0]-expected_lower)<1e-5
    assert abs(getCredibleInterval(sample)[1]-expected_upper)<1e-5
