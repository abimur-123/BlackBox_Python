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

    # Capture incorrect input data
    try:
        AB.performABtest_Freq()
    except(TypeError):
        assert True
    else:
        assert False

    # Capture incorrect alpha values
    try:
        AB.performABtest_Freq(data = data,alpha = 1.5)
    except(ValueError):
        assert True
    else:
        assert False


    try:
        data = {'name':name,'value':value,'value_copy':value}
        AB.performABtest_Freq(data = data)
    except(TypeError):
        assert True
    else:
        assert False

    try:
        #sample dataframe
        n = 20
        p = 0.5
        x = 2
        name = np.repeat(('A','B'),n/2)
        value= np.random.binomial(x, p,size = n)
        data = {'name':name,'value':value}
    except(TypeError):
        assert True
    else:
        False

    # Generate output
    n = 2500
    p = 0.5
    x = 1
    name = np.repeat(('A','B'),n/2)
    value= np.random.binomial(x, p,size = n)
    d = {'input':name,'event':value}
    inp = pd.DataFrame(data=d)
    op = AB_freq(inp,0.1)

    # Check if p-value is between 0 and 1
    op_p_val = True if op[1] > 0 and op[1] <= 1 else False
    
    #assert length and type of op
    assert len(op) == 3
    assert isinstance(data,pd.DataFrame) == True
    assert op_p_val == True

def test_output():
    '''
    check if the output is in the valid range for the performABtest_Bayesian function
    '''

    assert AB.performABtest_Bayesian(df) > 0
    assert AB.performABtest_Bayesian(df) < 1
