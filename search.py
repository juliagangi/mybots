from parallelHillClimber import PARALLEL_HILL_CLIMBER
import random
import constants as c
import matplotlib.pyplot as plt
import numpy as np

best1 = []
for i in range(5):
    random.seed(i+1)
    phc = PARALLEL_HILL_CLIMBER(5)
    phc.Evolve('control')
    plt.plot(phc.fitnessArr, label=str(i+1), linewidth=1)
    best1.append(phc.Best_Parent())
ci = 0.1 * np.std(best1) / np.mean(best1)
plt.legend()
plt.xlabel('Generation')
plt.ylabel('Displacement')
plt.fill_between((best1-ci), (best1+ci))#, alpha=0.5)
plt.savefig('plot1')

exit()
best2 = []
for i in range(5):
    random.seed(i+1)
    phc = PARALLEL_HILL_CLIMBER(9)
    phc.Evolve('control')
    plt.plot(phc.fitnessArr, label=str(i+1), linewidth=1)
    best2.append(phc.Best_Parent())
ci = 0.1 * np.std(best2) / np.mean(best2)
plt.legend()
plt.xlabel('Generation')
plt.ylabel('Displacement')
plt.fill_between((best2-ci), (best2+ci))#, alpha=0.5)
plt.savefig('plot2')

best3 = []
for i in range(5):
    random.seed(i+1)
    phc = PARALLEL_HILL_CLIMBER(5)
    phc.Evolve('notcontrol')
    plt.plot(phc.fitnessArr, label=str(i+1), linewidth=1)
    best3.append(phc.Best_Parent())
ci = 0.1 * np.std(best3) / np.mean(best3)
plt.legend()
plt.xlabel('Generation')
plt.ylabel('Displacement')
plt.fill_between((best3-ci), (best3+ci))#, alpha=0.5)
plt.savefig('plot3')

input("Press Enter to Continue")
phc.Show_Best(best1,'control')
input("Press Enter to Continue")
phc.Show_Best(best2,'control')
input("Press Enter to Continue")
phc.Show_Best(best3,'notcontrol')