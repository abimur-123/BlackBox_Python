"""
AB Tests(frequentist approach)
"""
import pytest
import numpy as np
import pandas as pd

import sys
import os
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("../"))

from BlackBox_Python import ABtests as AB

#sample dataframes
n = 2
p = 0.5
x = 1
name = np.repeat(('A','B'),n/2)
value= np.random.binomial(x, p,size = n)
data = {'name':name,'value':value}
df=pd.DataFrame(data)

#check input
def test_input():
    '''
    check if the input is valid for getConfidenceInterval()
    '''
    msg1='Input data must be a dataframe'
    with pytest.raises(TypeError,match=pd.DataFrame):
        AB.performABtest_Freq((1,2,3))

    msg2='need to pass in a dataframe'
    with pytest.raises(TypeError,match=msg2):
        AB.performABtest_Freq()

    #valid dataframe must have at least 1 observations
    assert df.shape[0] > 2

    #valid dataframe must include two columns only
    assert df.shape[1] == 2

    #check if column2 is numeric
    assert np.array_equal(df.iloc[:,1].unique(),[0,1])

# def test_output():
#     '''
#     check if the output interval is valid
#     '''
#
#     #the lower bound of confidence interval must be larger than the min of data
#     assert ci.getConfidenceInterval(df)$lower>=df.iloc[:,1].min()
#     #the upper bound of confidence interval must be smaller than the max of data
#     assert ci.getConfidenceInterval(df)$upper>=df.iloc[:,1].max()
#
#     #check if the interval is correct
#     xbar=df.iloc[:,1].mean()
#     n=df.shape[0]
#     expected_lower=xbar-1.96*np.sqrt(xbar*(1-xbar))/np.sqrt(n)
#     expected_upper=xbar+1.96*np.sqrt(xbar*(1-xbar))/np.sqrt(n)
#
#     assert getCredibleInterval(df)$lower==expected_lower
#     assert getCredibleInterval(df)$upper==expected_upper
