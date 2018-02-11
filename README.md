# BlackBox_Python


Outline the package you would like to build in a README.md file which should live in each of the project's root directory (this can be identical for both projects at this point in the project). In this document include:
the names of the contributors (the students on the teams)
a summary paragraph that descibes the project at a high level
a bulleted list of the functions (and datasets if applicable) that will be included in the package (this should be a 1-2 sentence description for each function/dataset)
a paragraph describing where your packages fit into the Python and R ecosystems (are there any other Python or R software packages that have the same/similar functionality? Provide links to any that do. if none exist, then clearly state this as well).

### Contributors

1. Siddharth Arora(@sarora)
2. Yinghua Guan(@vinverguan)
3. Abishek Murali(@abimur-123)

### Summary

Our package is aimed towards novice (ML/programming language) users who can get a birdseye view of their dataset, and possible models which could be used for a given problem.


### Functions
|Function Name|Result|
|--|:----:|
|getEDA()|return the summary of dataset provided by the user. This could include graphs and tables.|
|getModelSummary()|return the summary of different models (classification/regression) used to evaluate the given problem.|
|getResources()|returns resources for the user to investigate more about the different models used on their dataset.|
|getCodeSummary()|returns code snippet for the best model evaluated. |


### Similar Packages

The [scikit learn](http://scikit-learn.org/stable/) module in Python helps streamline the model feature selection and prediction problems. Our package would utilize functions from this package to help visualize and compare the predictive power of various models for a given dataset.
