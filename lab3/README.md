# Lab 2: Set Covering with Genetic Algorithm

# Introduction

This lab aims to create various version of an agent able to play Nim:

Task 1: Fixed-Rules
Task 2: Evolvable Agent (EA) [lost files due to wrong versionig]
Task 3: MinMax
Task 4: Reinforcment Learnig (RL)

## Task 1
I implemented a simple agent which counts its own turns, and if the turn is even it will take a single element from the shortes row, otherwise it will take max amount of objects from the longest row

## Task 2 [LOST]
Unfortunately lost the whole implementation due to missed push on github.
The main idea was to define an Individual IND as a class with a `genome` and a `fitness`.
The genome was a tuple containing 2 arrays of float. These 2 arrays were 2 discrete distribution.
The first Distribution was used to decide which function use to choose the row, while the second distribution was used to decide which function use to choose the number of objects to take.

Each IND had a method `get_functions_index` which returned a tuple of 2 integers. These 2 integers were indexes used to access 2 arrays. These arrays contained some functions. There were an array containing functions to choose the row, and another one to choose the number of objects.

### Genetic Implementation
Initialization was Random, creating two arrays of random numbers, and then normalizing like:

    ```py
    prob = [random.random() for i in range(num_functions)]
    prob = [p/sum(prob) for p in prob]
    ```

Fitness Score, was evaluated using the `evaluation` function against the agent from Task 1.

Mutation was a slight modification in the probabilities vector of the genome. The modification occurred mantaining the distribution property of Sum 1.


The strategy consisted in taking the best IND 
# Method:


# Experimental results


# Conclusions



# Authors

This code has been developed after discussing it with [Marco Pratticò 294815](https://github.com/marcopra). However, our approach and code is different.

# Appendix: Code for Tests


```python
#@title Population Creation [Test Version]
f
```
