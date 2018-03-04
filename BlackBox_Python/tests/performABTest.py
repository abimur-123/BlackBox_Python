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
    check if the input is valid for performABtest_Freq function
    Try invalid and NULL input.
    '''
    msg1='Input data must be a dataframe'
    with pytest.raises(TypeError,match=msg1):
        AB.performABtest_Freq([1,2,3])

    msg2='need to pass in a dataframe'
    with pytest.raises(TypeError,match=msg2):
        AB.performABtest_Freq()

    # #valid dataframe must have at least 1 observations
    # assert df.shape[0] > 2

    #valid dataframe must include two columns only
    assert df.shape[1] == 2

    #check if column2 is numeric
    assert np.array_equal(df.iloc[:,1].unique(),[0,1])

def test_output():
    '''
    check if the output is in the valid range for the performABtest_Bayesian function
    '''

    assert AB.performABtest_Bayesian(df) > 0
    assert AB.performABtest_Bayesian(df) < 1
