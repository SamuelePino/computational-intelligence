
# Peer Review 

## At First Sight: Presentation and Readability
The README file is quite raw. It reports only the obtained results, given some configurations.
This makes understanding both the code and the reasons for specific choices difficult for an external user.   
The `conclusion` could have specified what was the idea behind the `grouping`, and how it was meant to be implemented conceptually.

The code itself is neat and it is quite easy to understand how the code works (even considering that I know what was the problem, what approach you decide to use and how it works).
More comments would have made the analysis much easier.

---
## Algorithm Approach and Code Analysis
The approach seems to be only a Breadth Search (BS). 
You use combinations of the lists of integers (given by the problem), and then you check their validity as solutions. If you find an exact solution with N integers you stop the loop, otherwise you will keep looping until every combination has been checked.

### - <ins> Main Function: Solve <ins>

```python
def solve(self):
        for n in range(3, 6):       

            possible_solutions = combinations(range(self.size), n)
                
            for ps in possible_solutions:
                self.total_steps += 1
                number_of_elements = self.getNumberOfElements(ps)
                if number_of_elements < self.min_number_of_el and self.isSolution(ps):
                    self.min_number_of_el = number_of_elements
                    self.best_sol = ps
                    self.visited_nodes += 1
                    if self.min_number_of_el == self.N: 
                        return   #I found the best solution
```

The BS is good for small/medium state spaces because this algorithm can find the global optimum in a decent amount of steps (visited nodes).

In this problem though, you can notice that the growth of the state space dimension is linked to N through a Factorial function (even avoiding the *combinations*; it is an intrinsic property of the problem). The dimension can rapidly explode.

The BS implemented fails (as the others I suggested in the *Personal Suggestions*) when you set the number of possible integer numbers (N) to 50 or higher (as you stated in the *conclusions*). This lets us assume that the state space has become probably too big for this kind of approach.

BS works especially well when weights associated to each step are all equal.
In this particular case there are no equal weights (except considering sporadic coincidences) so this may not be the best algorithm to implement for this problem. 

---
## Doubts
I do not understand why in the `Solve` function, the for-loop starts with combinations of dimension 3. You can miss potential solutions made up of 1 or 2 lists containing all numbers.

---
## Personal Suggestion:
Maintaining your approach, my advice is to add some sort of Preprocessing (sorting, remove useless lists...) over the main list of lists and maybe implement a stronger form of pruning while checking each combination. 
Unfortunately, even implementing this optimization the BS probably will not work anyway considering N= 50 or higher.

Considering instead a different approach, an A-star or a Dijkstra could have been valid alternatives, in terms of both quality and computational performance. They can both find optimal solutions and the A-star algorithm can even exploit a-priori knowledge to make "better" decisions and converge even faster. 
They are both harder to implement though.


 