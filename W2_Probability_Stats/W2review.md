Review DSI
Week 0 and Week 1

SQL

* What is an RDBMS?

* What is a schema?

* What does SQL stand for and what is it?

* How do you access information stored in SQL databases?

* What are the two main parts of a SQL query?

* The following questions pertain to specific SQL commands:
    * How do you constrain the number of records returned by a query?
    * How do you sort sort the order of records returned by a query?
    * How do you group rows together?
    * How do you find specific rows in a table...
        * Before an aggregation?
        * After an aggregation?

* Name 3 types of joins and draw Venn diagram examples of them.

* How might you improve the readability of a large, complicated query?  Think both
  regarding syntax and the formation of other tables.


Probability

* What is Bayes rule?  What does it relate?
Relates prior belief to posterior belief given evidence.

* What is combinatorics?

* How many ways can I arrange n unique objects?
n!

* How many ways can I arrange k of n unique objects, where k < n?  What is this called?
n!/k!.  n Permute k.

* If order doesn't matter, how many ways can I pick k of n objects? What is this called?
n choose k, or k combinations from sample n.  n!/(k!(n-k)!)

* What is a random variable?
A function that maps outcomes (events) to values.

* How would you define the difference between discrete and continuous distributions?
Discrete: countable event space, usually integers.  PMF.
Continuous: event space is continuous, infinitely many values.  PDF.

* What distribution would you use to model the following cases:
    * What is the probability that the mean volume of 50 bottles is less than 500 ml?
        Normal.
    * Deciding to go for a run or not.
        Bernoulli (coin flip).
    * Determining how many days pass before you finally decide to go for a run.
        Geometric.
    * Determining how likely it is that you go for 10 runs in a month.
        Binomial.
    * Calculating how much water falls into an open swimming pool during a rain storm.
        Exponential.  Better -- Gamma!
    * Assuming you run at a 9 minute mile pace avg pace, determining how likely
      it is that you pass the 3 mile mark in a race in 25 minutes?
        Poisson.



Estimation-sampling

* What is the central limit theorem?
    As we sample from n iid distributions, the distribution of the samples approaches normal as n gets large.  Often applied to sample means in statistics, for n >= 30.

* How would you go about implementing a bootstrap, and why would you do it?
    From a sample S of size n, draw (with replacement!) k samples of size n from S.  Use to estimate population proportions and confidence in them without assuming a distribution.  Useful when your sample is small or the distribution of the parameter is unknown.

Hypothesis testing

* What are the general steps of a hypothesis tests?  Make one up (something you'd test)
  and go through the steps.
 ```
    How confident is the average DSI student in their understanding after two weeks?
    Survey a sample, ask them to rate self-confidence from 1-5.

    H0: Mean self-confidence is 3.0
    HA: Mean self confidence is not 3.0.
    Alpha = .1

    Calculate mean and standard error of sample.
    Use a 2-tailed t-test to determine p-value.
    If p < .1, reject H0 in favor of HA.
    Otherwise, do not reject H0.
```
* What is a p value?
    The probability that we would see the results assuming H0 is true.
* What is a type I error?
    A false positive: Rejecting H0 when H0 is true.
* What is a type II error?
    A false negative: Failing to reject H0 when H0 is false.


Power

* What are the four factors that influence power?
    * Effect size (eg, absolute difference between sample mean and null mean), significance level, sample size, standard deviation.
    *

* In Bayes rule, what are the posterior, the likelihood, and the prior distributions?
  How are they related?
  P(A|X), P(X|A), and P(A).  In each iteration, the posterior from the previous becomes the new prior.
