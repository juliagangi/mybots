import sys
import os
from simulation import SIMULATION
import solution
import pickle
import constants as c

if sys.argv[1] == 'random':
    solution.SOLUTION(0).Start_Simulation('GUI')
elif sys.argv[1] == 'exp1':
    try:
        num = sys.argv[2]
        parent = pickle.load('pickle2_'+str(num))
        id = parent.nextAvailableID
    except:
        par1 = pickle.load('pickle2_0','rb')
        par2 = pickle.load('pickle2_1','rb')
        par3 = pickle.load('pickle2_2','rb')
        par4 = pickle.load('pickle2_3','rb')
        par5 = pickle.load('pickle2_4','rb')
        parents = [par1,par2,par3,par4,par5]
        maxfitness = 1000
        maxpar = None
        for par in parents:
            currfitness = par.fitnessArray[c.numberOfGenerations]
            if currfitness > maxfitness:
                maxpar = par
        id = maxpar.nextAvailableID
    os.system("python3 simulate.py GUI " + str(id))
elif sys.argv[1] == 'exp2':
    try:
        num = sys.argv[2]
        parent = pickle.load('pickle3_'+str(num))
        id = parent.nextAvailableID
    except:
        par1 = pickle.load('pickle3_0','rb')
        par2 = pickle.load('pickle3_1','rb')
        par3 = pickle.load('pickle3_2','rb')
        par4 = pickle.load('pickle3_3','rb')
        par5 = pickle.load('pickle3_4','rb')
        parents = [par1,par2,par3,par4,par5]
        maxfitness = 1000
        maxpar = None
        for par in parents:
            currfitness = par.fitnessArray[c.numberOfGenerations]
            if currfitness > maxfitness:
                maxpar = par
        id = maxpar.nextAvailableID
    os.system("python3 simulate.py GUI " + str(id))