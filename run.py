import sys
import os
from simulation import SIMULATION
import solution
import pickle
import constants as c
from parallelHillClimber import PARALLEL_HILL_CLIMBER as phc

if sys.argv[1] == 'random':
    solution.SOLUTION(0,5).Start_Simulation('GUI','control')
elif sys.argv[1] == 'control':
    try:
        num = sys.argv[2]
        file = open('pickle1_'+str(num),'rb')
        par = pickle.load(file)
        par.Start_Simulation("GUI",'control')
    except:
        file = open('pickle1_1', 'rb')
        par1 = pickle.load(file)
        file = open('pickle1_2', 'rb')
        par2 = pickle.load(file)
        file = open('pickle1_3', 'rb')
        par3 = pickle.load(file)
        file = open('pickle1_4', 'rb')
        par4 = pickle.load(file)
        file = open('pickle1_5', 'rb')
        par5 = pickle.load(file)
        parents = [par1,par2,par3,par4,par5]
        p = phc(5)
        p.Show_Best(parents,'control')
elif sys.argv[1] == 'exp1':
    try:
        num = sys.argv[2]
        file = open('pickle2_'+str(num),'rb')
        par = pickle.load(file)
        par.Start_Simulation("GUI",'control')
    except:
        file = open('pickle2_1', 'rb')
        par1 = pickle.load(file)
        file = open('pickle2_2', 'rb')
        par2 = pickle.load(file)
        file = open('pickle2_3', 'rb')
        par3 = pickle.load(file)
        file = open('pickle2_4', 'rb')
        par4 = pickle.load(file)
        file = open('pickle2_5', 'rb')
        par5 = pickle.load(file)
        parents = [par1,par2,par3,par4,par5]
        p = phc(10)
        p.Show_Best(parents,'control')
elif sys.argv[1] == 'exp2':
    try:
        num = sys.argv[2]
        file = open('pickle3_'+str(num),'rb')
        par = pickle.load(file)
        par.Start_Simulation("GUI",'notcontrol')
    except:
        file = open('pickle3_1', 'rb')
        par1 = pickle.load(file)
        file = open('pickle3_2', 'rb')
        par2 = pickle.load(file)
        file = open('pickle3_3', 'rb')
        par3 = pickle.load(file)
        file = open('pickle3_4', 'rb')
        par4 = pickle.load(file)
        file = open('pickle3_5', 'rb')
        par5 = pickle.load(file)
        parents = [par1,par2,par3,par4,par5]
        p = phc(5)
        p.Show_Best(parents,'notcontrol')