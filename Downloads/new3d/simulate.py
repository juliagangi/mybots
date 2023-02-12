import random
from solution import SOLUTION

numSims = random.randint(1,9)
print(numSims)
for i in range(numSims):
        solution = SOLUTION(i)
        solution.Start_Simulation()