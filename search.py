from parallelHillClimber import PARALLEL_HILL_CLIMBER
import random
import constants as c
import matplotlib.pyplot as plt
import numpy as np
import pickle


colors = ['blue','orange','green','cyan','purple']
arrs = []
best1 = []
for i in range(5):
    random.seed(i+1)
    phc = PARALLEL_HILL_CLIMBER(5,i+1)
    phc.Evolve('A',5)
    plt.plot(phc.fitnessArr, label=str(i+1), color=colors[i], linewidth=1)
    x = np.arange(0,c.numberOfGenerations+1,1)
    bestpar = phc.Best_Parent()
    best1.append(bestpar)
    file = open('pickles/pickle1_'+str(i+1), 'wb')
    pickle.dump(bestpar,file)
    arrs.append(phc.fitnessArr)
meanarr = []
for ind in range(c.numberOfGenerations+1):
    arra = [arrs[0][ind],arrs[1][ind],arrs[2][ind],arrs[3][ind],arrs[4][ind]]
    meanarr.append(np.mean(arra))
    ci = 1.96 * np.std(arra)/np.sqrt(5) 
    plt.fill_between(ind,(meanarr-ci), (meanarr+ci), color='red', alpha=0.1)
plt.plot(meanarr, label="Mean", color='red', linewidth=2)
plt.legend()
plt.xlabel('Generation')
plt.ylabel('Displacement')
plt.title('Evolution: Group A (Control)')
plt.savefig('diagrams/plot1')
plt.cla()


arrs = []
best2 = []
for i in range(5):
    random.seed(i+1)
    phc = PARALLEL_HILL_CLIMBER(9,i+1)
    phc.Evolve('B',1)
    plt.plot(phc.fitnessArr, label=str(i+1), color=colors[i], linewidth=1)
    x = np.arange(0,c.numberOfGenerations+1,1)
    bestpar = phc.Best_Parent()
    best2.append(bestpar)
    file = open('pickles/pickle2_'+str(i+1), 'wb')
    pickle.dump(bestpar,file)
    arrs.append(phc.fitnessArr)
meanarr = []
for ind in range(c.numberOfGenerations+1):
    arra = [arrs[0][ind],arrs[1][ind],arrs[2][ind],arrs[3][ind],arrs[4][ind]]
    meanarr.append(np.mean(arra))
    ci = 1.96 * np.std(arra)/np.sqrt(5) 
    plt.fill_between(ind,(meanarr-ci), (meanarr+ci), color='red', alpha=0.1)
plt.plot(meanarr, label="Mean", color='red', linewidth=2)
plt.legend()
plt.xlabel('Generation')
plt.ylabel('Displacement')
plt.title('Evolution: Group B')
plt.savefig('diagrams/plot2')
plt.cla()

best3 = []
arrs = []
for i in range(5):
    random.seed(i+1)
    phc = PARALLEL_HILL_CLIMBER(5,i+1)
    phc.Evolve('C',1)
    plt.plot(phc.fitnessArr, label=str(i+1), color=colors[i], linewidth=1)
    x = np.arange(0,c.numberOfGenerations+1,1)
    bestpar = phc.Best_Parent()
    best3.append(bestpar)
    file = open('pickles/pickle3_'+str(i+1), 'wb')
    pickle.dump(bestpar,file)
    arrs.append(phc.fitnessArr)
meanarr = []
for ind in range(c.numberOfGenerations+1):
    arra = [arrs[0][ind],arrs[1][ind],arrs[2][ind],arrs[3][ind],arrs[4][ind]]
    meanarr.append(np.mean(arra))
    ci = 1.96 * np.std(arra)/np.sqrt(5) 
    plt.fill_between(ind,(meanarr-ci), (meanarr+ci), color='red', alpha=0.1)
plt.plot(meanarr, label="Mean", color='red', linewidth=2)
plt.legend()
plt.xlabel('Generation')
plt.ylabel('Displacement')
plt.title('Evolution: Group C')
plt.savefig('diagrams/plot3')


input("Press Enter to Continue")
phc.Show_Best(best1,'A')
input("Press Enter to Continue")
phc.Show_Best(best2,'B')
input("Press Enter to Continue")
phc.Show_Best(best3,'C')