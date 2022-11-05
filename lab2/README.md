# Lab 2: Set Covering with Genetic Algorithm

# Introduction

This lab aims to solve the **_Set Covering_** problem using `Genetic algorithms`.

# Method:

## Structure:

* Gene: in this solution is represented as an index which corresponds to a specific list of the problem.
* Genome: it is a list of genes (indexes of the problem) with a specific lenght given by the parameter GENOME_LENGTH.
* Individual (IND): it is a `Tuple` containing a Genome and its fitness value.
* Population: it is a list containing a fixed number of individuals.

* Endocoding: The idea is to have a fixed-length genome as a list of indexes, each one corresponding to a list in the problem. Then a dictionary is used to translate indexes in list.

## Problem management
The problem is at first generated, then sorted by `-len()` and its duplicates are removed.

The problem is then transformed in a list of sets.

Then we use a `coverage table` which is a dictionary, used to faster translate indexes in the corresponding list. Really useful for Integers Coverage Check (ICC) in the solution/genome.


## Fitness Function:

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


## Implementation of the Null Set
This idea allows an IND to mutate its genes avoiding to choose a list from problem, but choosing instead a void one. 
This strongly compensates the decision of using a fixed-length genome, which is useful for Recombination/Mating of INDs.

--------
## Offspring Generation
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
---------
# Experimental results

Some Notation used to facilitate comprehension:

    ET: Elapsed Time
    AVG X: Average x
    IND: Individual
    NG: Number of Generations
    GL: Genome Length
    POP_SIZE: Population Size
    OFF_SIZE: Offspring Size

The experimental results for the _Set Covering_ Algorithm are reported in the following tables.

For several runs we tested the algorithm with the following combinations of parameters: 


    N= 50, 500
    GL = 13,16,25
    NG = 500,1000


_NB: POP_SIZE and OFF_SIZE are always fixed to 400 and 200 respectively_

### For `N=50` for 20 runs each

    |N: 50 - GL: 13  - NG: 500  | N: 50 - GL: 16  - NG: 500  | N: 50 - GL: 25 - NG: 500  |
    |---------------------------|----------------------------|----------------------------|   
        MIN: 71   MAX:90            MIN: 71   MAX:89            MIN: 72   MAX:94
        AVG ET:  1.045              AVG ET:  1.215              AVG ET:  1.612
        AVG BLOAT:  158.6           AVG BLOAT:  159.4           AVG BLOAT:  166.3 
        AVG COST:  79.3             AVG COST:  79.7             AVG COST:  83.15


    |N: 50 - GL: 13  - NG: 1000  | N: 50 - GL: 16  - NG: 1000 | N: 50 - GL: 25  - NG: 1000 |
    |----------------------------|----------------------------|----------------------------|   
        MIN: 68   MAX:87            MIN: 73   MAX:86            MIN: 73   MAX:90
        AVG ET:  2.132              AVG ET:  2.462              AVG ET:  3.229
        AVG BLOAT:  157.8           AVG BLOAT:  161.0           AVG BLOAT:  165.0 
        AVG COST:  78.9             AVG COST:  80.5             AVG COST:  82.5
                                    
                                    |      
_Comments_:  
At first we can notice that a small GL and a big NG leads to better overall performance.
With bigger GLs we usually have an higher ET, AVG BLOAT and AVG COST, due to the fact each IND has more genes.


### For `N=500` for 10 runs each
Due to its dimension we only tested 10 runs for each combinations, for time reasons:
                                        
    |N: 500 - GL: 13  - NG: 500  | N: 500 - GL: 16  - NG: 500  | N: 500 - GL: 25  - NG: 500  |
    |---------------------------|----------------------------|----------------------------|   
        MIN: 1499   MAX:1647        MIN: 1576   MAX:1782        MIN: 1540   MAX:2182
        AVG ET:  8.0187             AVG ET:  9.704              AVG ET:  13.224
        AVG BLOAT:  314.7           AVG BLOAT:  338.4           AVG BLOAT:  332.28 
        AVG COST:  1573.3           AVG COST:  1692.0           AVG COST:  1661.4


    |N: 500 - GL: 13  - NG: 1000  | N: 500 - GL: 16  - NG: 1000 | N: 500 - GL: 25  - NG: 1000 |
    |----------------------------|----------------------------|----------------------------|   
        MIN: 1420   MAX:1589        MIN: 1422   MAX:1632         MIN: 1522   MAX:1678
        AVG ET:  15.396             AVG ET:  18.570              AVG ET:  26.487
        AVG BLOAT:  302.74          AVG BLOAT:  309.14           AVG BLOAT:  317.3
        AVG COST:  1513.7           AVG COST:  1545.7            AVG COST:  1586.5              
                                         
    _The code used to test the algorithm is at the bottom of the file in the Appendice_

 
[This are minimum found tuning properly the algorithm]

(Work In Progress)
| N | W(Cost) | Bloat | Population Size | Offspring size| Elapsed Time| GL| NG |
| --| ------- | -------- |------------- | ----------- |  ----------- | ---|----|
|5 | 5 | 100% | 200 |160 | 0.0086 s | 4|   10 |
| 10 | 10 | 100% | 200 | 160| 0.0483|  4   | 50  |
|20|24| 120% |200 | 160 |0.0859|  4  |  80   |
|50|69| 138% |20000 | 5600 |73.0 s| 13  |  900   | 
67 found a few times...
|100|176| 176% |miss|miss | miss s| miss  |  miss  |
|500| 1398 | 279.6% | 4000| 1000| miss circa 90s| 13  | 1000  |  
1391 found  a few times 
genome(1398)=[3, 1376, 1382, 157, 70, 1778, 1734, 1384, 1809, 624, 1809, 1775, 1809]
|1000| 3314 | 331.4% | 500| 100| 102.3s| 14 |  5000|
genome=[147, 1431, 728, 1628, 382, 3550, 3371, 3292, 3612, 3163, 2973, 3487, 3619, 3544]

# Conclusions

The experimental results show that the algorithm can find reasonable results by spending a reasonable amount of time. 

Tuning the various parameter is crucial for the efficiency and quality of the foundd solution. 

In this implementation we only test a single FF, and genes are indexes, which then need to be translated to check acceptability for each genome generated. The FF is not particulary efficient, so further work can be done there.

We can observe from experiments that this algorithm scales quite terribly with growing N, but the quality of the solution can be satisfying.
We do not try an implementation of a Tournament, but only an Elitarism with recombination and mutation between the top.

# Authors

This code has been developed after discussing it with [Marco Pratticò 294815](https://github.com/marcopra). However, our code is different.

# Appendice: Code for Tests

The code used to test the algorithm is a modification of the last cell:
```python
#@title Population Creation
from time import time

ET_array_store = []
BLOAT_Store = []
cost_store = []

NUM_RUN= 20

for i in range(0, NUM_RUN):
  #SETTINGS
  GENOME_LENGTH = 25
  DIM_POP = 400
  DIM_MAX_OFFSPRING= 200
  PERCENTAGE_SELECTED =75
  NUM_GEN = 1000
  PROB_MUT = 0.7 

  #Create an array of Individual istances, each already evaluate
  population = [random_new_individual() for _ in range(0, DIM_POP)]
  population.sort(key=sorting_key, reverse=True)

  #Plot variables init
  best_for_gen = [-100000]
  gens = range(0,NUM_GEN)
  extinted = False

  st  = time()

  for gen in range(0, NUM_GEN):

    offspring=generate_offspring_from(population,
                                        PERCENTAGE_SELECTED=PERCENTAGE_SELECTED, 
                                        PROB_MUT = PROB_MUT, 
                                        DIM_MAX_OFFSPRING=DIM_MAX_OFFSPRING)
    
    if len(offspring) == 0:
        print(f"Population extinted at gen: {gen-1} with best: {population[0].fitness_score}")
        extinted = True
        break

    population = offspring

    best_score = population[0].fitness
    best_for_gen.append(best_score)

  if not extinted:
      #import matplotlib.pyplot as plt

      #plt.plot(range(0,len(best_for_gen)-1), best_for_gen[1:])
      #plt.show()

      et  = time()

      elapsed_time = et - st
      best =  population[0]
      cost = -best.fitness[0]
      bloat = cost/N *100
      #print("Winner: \n", best)
      #print("Cost: ", cost)
      #print("Bloat= ", bloat, "%")
      #print(f"Elapsed time: {elapsed_time}s")

      #print("N: ", N)
      #print("GL: ", GENOME_LENGTH)
      #print("NG: ", NUM_GEN)

      ET_array_store.append(elapsed_time)
      BLOAT_Store.append(bloat)
      cost_store.append(cost)
print(f"MIN: {min(cost_store)}   MAX:{max(cost_store)}")
print("AVG ET: ", sum(ET_array_store)/len(ET_array_store))
print("AVG BLOAT: ", sum(BLOAT_Store)/len(BLOAT_Store))
print("AVG COST: ", sum(cost_store)/len(cost_store))
print("N: ", N)
print("GL: ", GENOME_LENGTH)
print("NG: ", NUM_GEN) 
```
