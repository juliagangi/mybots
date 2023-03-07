from parallelHillClimber import PARALLEL_HILL_CLIMBER
import random
import constants as c
import matplotlib.pyplot as plt

best1 = []
for i in range(5):
    random.seed(i+1)
    phc = PARALLEL_HILL_CLIMBER(5)
    phc.Evolve('control')
    plt.plot(phc.fitnessArr, label=str(i+1), linewidth=1)
    best1.append(phc.Best_Parent())
plt.legend()
plt.xlabel('Generation')
plt.ylabel('Displacement')
plt.show()


best2 = []
for i in range(5):
    random.seed(i+1)
    phc = PARALLEL_HILL_CLIMBER(5)
    phc.Evolve('notcontrol')
    plt.plot(phc.fitnessArr, label=str(i+1), linewidth=1)
    best2.append(phc.Best_Parent())
plt.legend()
plt.xlabel('Generation')
plt.ylabel('Displacement')
plt.show()

input("Press Enter to Continue")
phc.Show_Best(best1,'control')
input("Press Enter to Continue")
phc.Show_Best(best2,'notcontrol')

