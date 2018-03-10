import scipy.stats as stats
import numpy as np
import pandas as pd
import math

def performABtest_Freq(data,alpha = 0.05):
    """
    Get results of A/B tests done using the frequentist approach

    Args:
    data: first column is event(string), second column is value(numeric)
    alpha: false positive rate

    Return:
    1. p-value indicating significance
    2. graph tracing p-values across runs
    3. method used to compute p-value
    """

    #Tests
    if data is None or (not isinstance(data,pd.DataFrame)):
        raise TypeError("Input data must be a dataframe")

    if (alpha > 1 | alpha < 0):
        raise ValueError("Alpha/False positive rate cannot be greater than 1 or less than 0")

    if df.shape[1] != 2:
        raise TypeError("Input data must have 2 columns")

    if (!np.array_equal(data.iloc[:,1].unique(),[0,1])):
        raise TypeError("Input events can have values of just 0 and 1")

    if (len(np.unique(data.iloc[:,0])) != 2):
        raise TypeError("Can have only 2 events for the test")

    # Construct contingency table(2 x 2 table)
    conti_tab = data.groupby('input').agg({'event': ['sum', 'count']})
    conti_tab['event']['count'] = conti_tab['event']['count'] - conti_tab['event']['sum']

    start_iter = floor(0.75 * len(inp))

    #compute p-value for records
    ip = {'index':[],'p_val':[]}
    if len(data) < 2000:
        method = "Fisher"
        for i in range(start_iter,len(inp)):
            conti_tab = inp[0:i].groupby('input').agg({'event': ['sum', 'count']})
            conti_tab['event']['count'] = conti_tab['event']['count'] - conti_tab['event']['sum']
            ip['index'].append(i)
            pval = stats.fisher_exact(conti_tab['event'])[1]
            ip['p_val'].append(round(pval,4))
    else:
        method = "Chi square test"
        for i in range(start_iter,len(inp)):
            conti_tab = inp[0:i].groupby('input').agg({'event': ['sum', 'count']})
            conti_tab['event']['count'] = conti_tab['event']['count'] - conti_tab['event']['sum']
            ip['index'].append(i)
            pval = stats.chi2_contingency(conti_tab['event'])[1]
            ip['p_val'].append(round(pval,4))

    f, ax = plt.subplots(figsize=(7,5))
    ax.plot(ip['index'],ip['p_val'], "-or")
    ax.axhline(y=alpha, color='g', linestyle='-')
    ax.set_xlabel("Record number")
    ax.set_ylabel("p-value")
    ax.set_title("Variation of p-values",fontsize = 15)
    ax.annotate('Alpha value = ' + str(alpha),xy=(len(data) - len(data)//4,alpha + 0.02),fontsize = 12)

    return [ip['p_val'][-1],ax,method]

def performABtest_Bayesian(df,prior = None):
    """
    Get results of A/B tests done using the Bayesian approach

    Args:
    dataframe: first column is event(string), second column is value(numeric)
    prior: prior assumptions of the data

    Return:
    p-value indicating significance.
    """
    if(isinstance(df,pd.DataFrame) == False):
        raise TypeError("Not a data frame")

    dummy_p_value = -0.5
    return dummy_p_value
