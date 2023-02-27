import sys
import os
from simulation import SIMULATION
import solution

if sys.argv[1] == 'random':
    solution.SOLUTION(0).Start_Simulation('GUI')
elif sys.argv[1] == 'evolved':
    os.system("python3 search.py")
