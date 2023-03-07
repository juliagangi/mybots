from parallelHillClimber import PARALLEL_HILL_CLIMBER
import random
import constants as c
import matplotlib.pyplot as plt
import numpy as np

colors = ['blue','orange','green','red','purple']
best1 = []
for i in range(5):
    random.seed(i+1)
    phc = PARALLEL_HILL_CLIMBER(5)
    phc.Evolve('control')
    plt.plot(phc.fitnessArr, label=str(i+1), color=colors[i], linewidth=1)
    x = np.arange(0,c.numberOfGenerations+1,1)
    ci = 1.96 * np.std(phc.fitnessArr)/np.sqrt(len(x))
    plt.fill_between(x,(phc.fitnessArr-ci), (phc.fitnessArr+ci), color=colors[i], alpha=0.1)
    best1.append(phc.Best_Parent())
plt.legend()
plt.xlabel('Generation')
plt.ylabel('Displacement')
plt.title('Evolution: Control')
plt.savefig('plot1')
plt.cla()

best2 = []
for i in range(5):
    random.seed(i+1)
    phc = PARALLEL_HILL_CLIMBER(9)
    phc.Evolve('control')
    plt.plot(phc.fitnessArr, label=str(i+1), color=colors[i], linewidth=1)
    x = np.arange(0,c.numberOfGenerations+1,1)
    ci = 1.96 * np.std(phc.fitnessArr)/np.sqrt(len(x))
    plt.fill_between(x,(phc.fitnessArr-ci), (phc.fitnessArr+ci), color=colors[i], alpha=0.1)
    best1.append(phc.Best_Parent())
plt.legend()
plt.xlabel('Generation')
plt.ylabel('Displacement')
plt.title('Evolution: Experiment #1')
plt.savefig('plot2')
plt.cla()

best3 = []
for i in range(5):
    random.seed(i+1)
    phc = PARALLEL_HILL_CLIMBER(5)
    phc.Evolve('notcontrol')
    plt.plot(phc.fitnessArr, label=str(i+1), color=colors[i], linewidth=1)
    x = np.arange(0,c.numberOfGenerations+1,1)
    ci = 1.96 * np.std(phc.fitnessArr)/np.sqrt(len(x))
    plt.fill_between(x,(phc.fitnessArr-ci), (phc.fitnessArr+ci), color=colors[i], alpha=0.1)
    best1.append(phc.Best_Parent())
plt.legend()
plt.xlabel('Generation')
plt.ylabel('Displacement')
plt.title('Evolution: Experiment #2')
plt.savefig('plot3')

input("Press Enter to Continue")
phc.Show_Best(best1,'control')
input("Press Enter to Continue")
phc.Show_Best(best2,'control')
input("Press Enter to Continue")
phc.Show_Best(best3,'notcontrol')