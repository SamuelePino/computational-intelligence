
import random
from itertools import combinations 

def problem(N:int, seed:int=None) -> list:
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]

def check_solution(N:int, solution:list[list]) -> bool:

    # A table where the index represents the corresponding number, and the content is a bool
    check_table: list= list(False for i in range(0,N))

    #print("check table init:")
    #print(check_table)

    # flag to trigger the first if and leave the loop if a solution has been found
    solution_found  = False

    # for each list of the proposed solution
    for my_list in solution:

        if solution_found:
            break

        # check for each value we need to search (numbers in 0-N) if it is in this list
        for n in range(0,N):

            # check: if the checkTable is all True, the solution works
            # we can exit through a 'break'
            if all(check_table):
                solution_found = True
                break
            #print(f"current n: {n}\ncurrent my_list: {my_list}")

            # Otherwise we check if the n-th number is in this list
            if n in my_list:

                check_table[n] = True

    return   all(check_table)

def solve(N:int, problem:list[list]) -> list[list]:

    s = []
    dim = 0
    solution_found = False
    iterations = 0

    for n in range(0, len(problem)):  

        if solution_found:
            break  

        dim = dim+1
        combs = list(combinations(problem, dim))
        for comb in combs:
            iterations += 1
            if check_solution(N, solution=comb):
                #print(f"check: {check_solution(N, solution=comb)}")
                #print(comb)
                solution_found = True
                s = comb
                break
        #print(f"For DIM: {dim} we've got: {comb}")

    #print(s)
    #print(f"check: {check_solution(N, solution=s)}")
    if check_solution(N, solution=s):
        print(f"Found solution in {iterations} steps: {s}")
        
    else:
        print("No solution found")
    return s

# Is the range in which we generate integers => (0, N)
N = 10  

p = problem(N, seed=42)
print(f"problem:\n {p}\n")
p.sort(key= lambda x: len(x))
print(f"sorted problem:\n {p}")

s: list[list] = []
s = solve(N,problem=p)

#print(s)
"""
test_solution = [[0, 3], [1,1], [0,2] ]
res = check_solution(N, solution= test_solution)

print(f"TEST Result is:  {res}")
"""