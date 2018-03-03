"""
Confidence Interval Tests(frequentist approach)
"""

import pytest
import numpy as np
import pandas as pd
from BlackBox_Python import ci

#sample dataframe
name=np.repeat('A',4)
score=np.random.beta(3,2,size=4)
data={'name':name,'score':score}
df=pd.DataFrame(data)


#check input
def test_input():
    '''
    check if the input is valid for getConfidenceInterval()
    '''
    msg1='Input data must be a dataframe'
    with pytest.raises(TypeError,match=msg1):
        ci.getConfidenceInterval(c(1,2,3))

    msg2='need to pass in a dataframe'
    with pytest.raises(TypeError,match=msg2):
        ci.getConfidenceInterval()

    #valid dataframe must have at least 1 observations
    assert df.shape[0]>0

    #valid dataframe must include two columns only
    assert df.shape[1]==2

    #check if column2 is numeric
    assert df.iloc[:,1].dtype==np.int64 or df.iloc[:,1].dtype==np.float64

def test_output():
    '''
    check if the output interval is valid
    '''

    #the lower bound of confidence interval must be larger than the min of data
    assert ci.getConfidenceInterval(df)$lower>=df.iloc[:,1].min()
    #the upper bound of confidence interval must be smaller than the max of data
    assert ci.getConfidenceInterval(df)$upper>=df.iloc[:,1].max()

    #check if the interval is correct
    xbar=df.iloc[:,1].mean()
    n=df.shape[0]
    expected_lower=xbar-1.96*np.sqrt(xbar*(1-xbar))/np.sqrt(n)
    expected_upper=xbar+1.96*np.sqrt(xbar*(1-xbar))/np.sqrt(n)

    assert getCredibleInterval(df)$lower==expected_lower
    assert getCredibleInterval(df)$upper==expected_upper
