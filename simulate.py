import random
from solution import SOLUTION
import os
import constants as c

os.system("rm body*.urdf")
numSims = random.randint(1,9)
print(numSims)
for i in range(numSims):
        solution = SOLUTION(i)
        solution.Start_Simulation()