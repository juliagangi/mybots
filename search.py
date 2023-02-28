from parallelHillClimber import PARALLEL_HILL_CLIMBER
import os
import random
import constants as c
import matplotlib.pyplot as plt

parents = {}
for i in range(c.seeds):
    random.seed(i+1)
    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve()
    array = phc.parents[0].fitnessArray
    plt.plot(array, label=str(i+1), linewidth=1)
    parents[i] = phc.parents[0]
phc.Show_Best(parents)
plt.legend()
plt.xlabel('Generation')
plt.ylabel('Displacement')
plt.show()