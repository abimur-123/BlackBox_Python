"""
MAP vs MLE
"""
import pytest
import numpy as np
import pandas as pd

import sys
import os
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("../"))

from BlackBox_Python import MapVMle as MVM


# test inputs
def test_input_types():
  '''
  Check input types for getMLE function
  '''
  with pytest.raises(TypeError):
    MVM.getMLE(12345,12345)

  with pytest.raises(TypeError):
    MVM.getMLE("1233","1231")


def test_output():
    '''
    check if the output is valid
    '''
    # likelihood returned is between 0 and 1
    assert MVM.getMLE("binomial",[1,0,1,1,1,3,2]) >= 0 and MVM.getMLE("binomial",[1,0,1,1,1,3,2]) <= 1

    ### count returned is greater than 0
    assert (MVM.getMAP("poisson","[1,2,3]")) > 0
