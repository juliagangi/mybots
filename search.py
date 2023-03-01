from parallelHillClimber import PARALLEL_HILL_CLIMBER
import os
import random
import constants as c
import matplotlib.pyplot as plt
import time

for i in range(5):
    random.seed(i+1)
    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve()
    plt.plot(phc.fitnessArr, label=str(i+1), linewidth=1)
    #phc.Show_Best()
    #time.sleep(5)
plt.legend()
plt.xlabel('Generation')
plt.ylabel('Displacement')
plt.show()
'''
for i in range(5):
    random.seed(i+6)
    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve()
    for parent in phc.parents:
        parent.
    plot_array.append()
phc.Show_Best() 
phc.Plot()
'''