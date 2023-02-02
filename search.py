from solution import SOLUTION
import random

solution=SOLUTION(0)
solution.Start_Simulation()
exit()
numSims = random.randint(0,9)
for i in range(numSims):
    solution = SOLUTION(i)
    solution.Start_Simulation()