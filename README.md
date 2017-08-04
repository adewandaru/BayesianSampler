# Description
BayesianSampler is a simple, extensible module for understanding Bayesian Network, Joint Probability and Sampling process.
It built on top of Numpy and Pandas to provide an intuitive and working numbers so student can learn better about probabilistic model.

## How to use:
1. Define the experiment's random variable and their possible values by instantiating Experiment class.
In this example, we will start solving simple problem taken from Downey's ebook Think Bayes.

```
    Suppose there are two bowls of cookies.
    Bowl 1 contains 30 of Vanilla and 10 of Chocolates.
    Bowl 2 contains 20 of Vanilla and 20 of Chocolates.
    Suppose choosing bowl randomly and picking one of the cookies. 
    The cookie is vanilla. What is the probability it comes from Bowl 1?
```
We can model this as "Bowl" random variable and "Flavor" random variable. The Bowl is having two possible value, bowl 1 (b1) and bowl 2 (b2).

Examples:
```
ex = Experiment(["Flavor","Bowl"], [["vanilla","choco"], ["b1","b2"]] )
```

2. Instantiating an Experiment will create a full set of combination for each case of the experiment. We call this the Omega of the Experiment. Each of the entry will have "Tally" or the count of that particular entry. The Tally will be updated by generated samples or can be set manually. In our case, we will infuse values to reflect the knowledge about the problem:
```
# we will set the tally to match the experiment configuration.
ex.set( (ex.omega["Bowl"]=="b1") & (ex.omega["Flavor"]=="vanilla"), 30 )
ex.set( (ex.omega["Bowl"]=="b1") & (ex.omega["Flavor"]=="choco"), 10 )

ex.set( (ex.omega["Bowl"]=="b2") & (ex.omega["Flavor"]=="vanilla"), 20 )
ex.set( (ex.omega["Bowl"]=="b2") & (ex.omega["Flavor"]=="choco"), 20 )
```
3. Let's print the full probability table.

```
print ex
```
It will display as such:

| Flavor   | Bowl  | Tally |
| -------- |:-----:| -----:|
| vanilla  | b1    | 30    |
| vanilla  | b2    | 20    |
| choco    | b1    | 10    |
| choco    | b2    | 20    |

4. Now let's inquiry the model. Use the ex.p () function for simple probability. Use the ex.p_given () for conditional probability.

What is the probability of Bowl1 and Vanilla both picked?
```
print ex.p( ( ex.omega["Bowl"]=="b1" ) & ( ex.omega["Flavor"]=="vanilla" ) ) 
```

What is the probability of Bowl1 given Vanilla? == P(b1|vanilla) 
```
print ex.p_given( ex.omega["Bowl"]=="b1", ex.omega["Flavor"]=="vanilla" ) 
```
It will return 0.6, logically we expect b1 is more likely to be picked given that vanilla is more than chocolate in bowl 1.

## References:

 - Allen Downey's ebook: Think Bayes
 - Pieter Abbeel youtube videos
