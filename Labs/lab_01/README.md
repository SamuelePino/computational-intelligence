# LAB 01
This lab aims to find a solution for [problem]

## Approach Explained
The first approach is a Breadth Search (BS).  
The state space exploration is obtained through the function _'combinations'_ from *'itertools'*. This function generates each possible combination of a given list. The dimension of the set obtained can be specified through a second parameter (*here is 'dim'*).

Then each combination is tested through *'check_solution'*. 
There is a main for-loop from 0 to N, where N is the number of lists in the main problem list.

at each step the variable dim is increased by 1, so the combinations searched are of length = 'dim'.

With this algorithm we take as solution the
