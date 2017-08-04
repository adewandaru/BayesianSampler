# Description
BayesianSampler is a simple, extensible module for understanding Bayesian Network, Joint Probability and Sampling process.
It built on top of Numpy and Pandas to provide an intuitive and working numbers so student can learn better about probabilistic model.

## How to use:
1. Define the experiment's random variable and their possible values. 
In this example, "Prize" can have 1,2,3 indicating the door known by the host which contain the prize. The "Door" is the door selected initially by the player. The "Strategy" can be of either "switch" or "stick".

Examples:
```
#Monty Hall case:

ex = Experiment(["Prize","Door","Strategy"], [["1","2","3"], ["1","2","3"], ["switch","stick"]] )
```

2. That will create 

## References:

 - Allen Downey's ebook: Think Bayes
 - Pieter Abbeel youtube videos
