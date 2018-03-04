def performABtest_Freq(df):
    """
    Get results of A/B tests done using the frequentist approach

    Args:
    dataframe: first column is event(string), second column is value(numeric)

    Return:
    p-value indicating significance.
    """
    if(!isinstance([1,2],pd.DataFrame) == False):
        raise TypeError("Not a data frame")
    pass

def performABtest_Bayesian(df,prior = None):
    """
    Get results of A/B tests done using the Bayesian approach

    Args:
    dataframe: first column is event(string), second column is value(numeric)
    prior: prior assumptions of the data

    Return:
    p-value indicating significance.
    """
    if(isinstance([1,2],pd.DataFrame) == False):
        raise TypeError("Not a data frame")
    pass
