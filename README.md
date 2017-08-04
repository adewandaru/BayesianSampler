# Description
BayesianSampler is a simple, extensible module for understanding Bayesian Network, Joint Probability and Sampling process.
It built on top of Numpy and Pandas to provide an intuitive and working numbers so student can learn better about probabilistic model.

## How to use:
1. Define the experiment's random variable and their possible values. 
In this example, we will start solving simple problem taken from Downey's ebook Think Bayes.
    Suppose there are two bowls of cookies.
    Bowl 1 contains 30 of Vanilla and 10 of Chocolates.
    Bowl 2 contains 20 of Vanilla and 20 of Chocolates.
    Suppose choosing bowl randomly and picking one of the cookies. 
    The cookie is vanilla. What is the probability it comes from Bowl 1?


Examples:
```
#Monty Hall case:

ex = Experiment(["Prize","Door","Strategy"], [["1","2","3"], ["1","2","3"], ["switch","stick"]] )
```

2. That will create a full set of combination for each case of the experiment. We call this the Omega of the Experiment.
Each of the entry will have "Tally" or the Count of that particular entry.



## References:

 - Allen Downey's ebook: Think Bayes
 - Pieter Abbeel youtube videos
