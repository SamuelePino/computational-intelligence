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


The strategy consisted in taking the best IND (after selection through a tournament + elitism) and use its discrete distribution to choose at each turn a strategy for choosing both the row and the amount of objects to remove.

## Task 3
Not implemented yet, I focused on RL Agent ...

## Task 4
I implemented RL Agent using a specific `state-possible_action` dictionary of a dictionary. For each state seen by the agent, a relative `possible_action` list (implemented as a dictionary) was saved. For each of these actions, a g score was saved. The g is the expected value of that action in that state.

The Agent check at it each turn the state of the Nim table (the tuple of rows), and use it to understand if that state was already seen or not. If the state is new, the agent initialize a new "g distribution" for that state and its possible_action list, otherwise the Agent tries playing by choosing the action for that state with max g value.

The random factor is kept at 20% as from the Maze file...

The learn function simply increase or decrease the g value of the take action, using the reward obtained at the end of each match (1 for wins and -1 for defeats).

## Problems [WIP]
There may be some bugs in the learn function or in the training loop and in the play loop, because the Agent sometimes wins 9500-500 against my `fast` strategy, other timese is a 5000-5000, other times 500-9500. 

I tried some different inits but it seems to be useless.

In the play loop the Agent Always loses, and I cannot undestand why
