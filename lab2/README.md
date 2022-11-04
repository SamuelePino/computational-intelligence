# Lab 2: Set Covering with Genetic Algorithm

## Introduction

This lab aims to solve the **_Set Covering_** problem using `Genetic algorithms`.

## Method:



### Structure:

* Gene: in this solution is represented as an index which corresponds to a specific list of the problem.
* Genome: it is a list of genes (indexes of the problem) with a specific lenght given by the parameter GENOME_LENGTH.
* Individual (IND): it is a `Tuple` containing a Genome and its fitness value.
* Population: it is a list containing a fixed number of individuals.

* Endocoding: The idea is to have a fixed-length genome as a list of indexes, each one corresponding to a list in the problem. Then a dictionary is used to translate indexes in list.

### Problem management
The problem is at first generated, then sorted by `-len()` and its duplicates are removed.

The problem is then transformed in a list of sets.

Then we use a `coverage table` which is a dictionary, used to faster translate indexes in the corresponding list. Really useful for Integers Coverage Check (ICC) in the solution/genome.

### Fitness Function:

The fitness function is defined as follows:

```python
def fitness_function(genome):
  
    MIN = -1000_000
    numbers = 0

    if covered_by(genome):
        
        for index in genome:  
            numbers = numbers + len(coverage_table[index])
        return -numbers

    return MIN
```
At first it checks acceptability of the solution (ICC).

If the genome leads to an unacceptable solution (it does not contain all integers), its value will be MIN= -1000_000, set as a default value.

Otherwise it returns the count of integers present in the whole IND's genome, but negative in order to simplify sorting.


The aim is to minimize, or better maximize (given that the fitness score are negative), the results of the fitness function.

### Implementation of the Null Set
This idea allows an IND to mutate its genes avoiding to choose a list from problem, but choosing instead a void one. 
This strongly compensates the decision of using a fixed-length genome, which is useful for Recombination/Mating of INDs.

### Offspring Generation
The main idea is to:
  1) select a specific part of the population given a p percentage, as the 'top';

  2) save these top INDs unmutated (added in the offspring during the matin);

  3) let these top INDs have a mating session at random couple (then extracted), 
     where their direct offspring genome is obtained as a part of the genome of 
     parent 1 and the other part from parent 2. 

  4) the 'child' is then mutated and added to the offspring list, together with both its parents.    
    NB: parents are extracted from the top_pop list, and added to the offspring.

  
    RECAP:
    The population will be composed by the top p% of the population, and by their offspring, obtained through
    a sort of Recombination/crossover followed by a mutation

## Experimental results

The experimental results for the _Set Covering_ Algorithm are reported in the following table.

[This are minimum found tuning properly the algorithm]

| N | W(Cost) | Bloat | Population Size | Offspring size| Elapsed Time|
| --| ------- | -------- |------------- | ----------- |  ----------- |
|5 | 5 | 15% | 100 |3 | 0.003 s |
| 10 | 10 | 100% | 2000 | 100 | 0.09 s|
|20|26| 130% |100000 | 1000 |17.6 s|
|50|75| 150% |100000 | 1000 |18.0 s|
|100|203| 203% |100000| 1000| 18.1 s|
|500| 1607 | 321% | 100000| 1000| 36.1 s|
|1000| 3744 | 374% | 100000| 1000| 71.3 s|

## Conclusions

The experimental results show that the algorithm can find reasonable results by spending a reasonable amount of time. 
Obviously, in this algorithm, the goodness of results depends in a non-negligible way on the `POPULATION_SIZE`, `OFFSPRING_SIZE`, and `NUM_GENERATIONS`.

## Authors

This code has been developed after discussing it with [Marco Pratticò 294815](https://github.com/marcopra). However, our code is different.