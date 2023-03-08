from parallelHillClimber import PARALLEL_HILL_CLIMBER
import random
import constants as c
import matplotlib.pyplot as plt
import numpy as np
import pickle


colors = ['blue','orange','green','cyan','purple']
'''
arrs = []
best1 = []
for i in range(5):
    random.seed(i+1)
    phc = PARALLEL_HILL_CLIMBER(5)
    phc.Evolve('control')
    plt.plot(phc.fitnessArr, label=str(i+1), color=colors[i], linewidth=1)
    x = np.arange(0,c.numberOfGenerations+1,1)
    bestpar = phc.Best_Parent()
    best1.append(bestpar)
    file = open('pickle1_'+str(i), 'wb')
    pickle.dump(bestpar,file)
    arrs.append(phc.fitnessArr)
meanarr = []
for ind in range(c.numberOfGenerations+1):
    arra = [arrs[0][ind],arrs[1][ind],arrs[2][ind],arrs[3][ind],arrs[4][ind]]
    print(arra)
    print(np.mean(arra))
    meanarr.append(np.mean(arra))
    ci = 1.96 * np.std(arra)/np.sqrt(5) 
plt.plot(meanarr, label="Mean", color='red', linewidth=2)
plt.fill_between(x,(meanarr-ci), (meanarr+ci), color='red', alpha=0.1)
plt.legend()
plt.xlabel('Generation')
plt.ylabel('Displacement')
plt.title('Evolution: Control')
plt.savefig('plot1')
plt.cla()


arrs = []
best2 = []
for i in range(5):
    random.seed(i+1)
    phc = PARALLEL_HILL_CLIMBER(9)
    phc.Evolve('control')
    plt.plot(phc.fitnessArr, label=str(i+1), color=colors[i], linewidth=1)
    x = np.arange(0,c.numberOfGenerations+1,1)
    bestpar = phc.Best_Parent()
    best2.append(bestpar)
    file = open('pickle2_'+str(i), 'wb')
    pickle.dump(bestpar,file)
    arrs.append(phc.fitnessArr)
meanarr = []
for ind in range(c.numberOfGenerations+1):
    arra = [arrs[0][ind],arrs[1][ind],arrs[2][ind],arrs[3][ind],arrs[4][ind]]
    meanarr.append(np.mean(arra))
    ci = 1.96 * np.std(arra)/np.sqrt(5) 
plt.plot(meanarr, label="Mean", color='red', linewidth=2)
plt.fill_between(x,(meanarr-ci), (meanarr+ci), color='red', alpha=0.1)
plt.legend()
plt.xlabel('Generation')
plt.ylabel('Displacement')
plt.title('Evolution: Experiment #1')
plt.savefig('plot2')
plt.cla()
'''
best3 = []
arrs = []
for i in range(5):
    random.seed(i+1)
    phc = PARALLEL_HILL_CLIMBER(5)
    phc.Evolve('notcontrol')
    plt.plot(phc.fitnessArr, label=str(i+1), color=colors[i], linewidth=1)
    x = np.arange(0,c.numberOfGenerations+1,1)
    bestpar = phc.Best_Parent()
    best3.append(bestpar)
    file = open('pickle3_'+str(i), 'wb')
    pickle.dump(bestpar,file)
    arrs.append(phc.fitnessArr)
meanarr = []
for ind in range(c.numberOfGenerations+1):
    arra = [arrs[0][ind],arrs[1][ind],arrs[2][ind],arrs[3][ind],arrs[4][ind]]
    meanarr.append(np.mean(arra))
    ci = 1.96 * np.std(arra)/np.sqrt(5) 
plt.plot(meanarr, label="Mean", color='red', linewidth=2)
plt.fill_between(x,(meanarr-ci), (meanarr+ci), color='red', alpha=0.1)
plt.legend()
plt.xlabel('Generation')
plt.ylabel('Displacement')
plt.title('Evolution: Experiment #2')
plt.savefig('plot3')

'''
input("Press Enter to Continue")
phc.Show_Best(best1,'control')
input("Press Enter to Continue")
phc.Show_Best(best2,'control')
'''
input("Press Enter to Continue")
phc.Show_Best(best3,'notcontrol')