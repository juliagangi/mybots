import sys
import os
from simulation import SIMULATION
import solution
import pickle
import constants as c

if sys.argv[1] == 'random':
    solution.SOLUTION(0,5).Start_Simulation('GUI','control')
elif sys.argv[1] == 'exp1':
    try:
        num = sys.argv[2]
        parent = pickle.load('pickle2_'+str(num))
        id = parent.myID
    except:
        file = open('pickle2_0', 'rb')
        par1 = pickle.load(file)
        file = open('pickle2_1', 'rb')
        par2 = pickle.load(file)
        file = open('pickle2_2', 'rb')
        par3 = pickle.load(file)
        file = open('pickle2_3', 'rb')
        par4 = pickle.load(file)
        file = open('pickle2_4', 'rb')
        par5 = pickle.load(file)
        parents = [par1,par2,par3,par4,par5]
        maxfitness = -1000
        maxpar = None
        for par in parents:
            currfitness = par.fitnessArray[c.numberOfGenerations-1]
            if currfitness > maxfitness:
                maxpar = par
        id = maxpar.myID
    maxpar.Start_Simulation("GUI",'control')
    #os.system("python3 simulate.py GUI " + str(id))
elif sys.argv[1] == 'exp2':
    try:
        num = sys.argv[2]
        parent = pickle.load('pickle3_'+str(num))
        id = parent.myID
    except:
        file = open('pickle3_0', 'rb')
        par1 = pickle.load(file)
        file = open('pickle3_1', 'rb')
        par2 = pickle.load(file)
        file = open('pickle3_2', 'rb')
        par3 = pickle.load(file)
        file = open('pickle3_3', 'rb')
        par4 = pickle.load(file)
        file = open('pickle3_4', 'rb')
        par5 = pickle.load(file)
        parents = [par1,par2,par3,par4,par5]
        maxfitness = -1000
        maxpar = None
        for par in parents:
            currfitness = par.fitnessArray[c.numberOfGenerations-1]
            if currfitness > maxfitness:
                maxpar = par
        id = maxpar.myID
    maxpar.Start_Simulation("GUI",'notcontrol')
    #os.system("python3 simulate.py GUI " + str(id))