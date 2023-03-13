import sys
import os
from simulation import SIMULATION
import solution
import pickle
import constants as c
from parallelHillClimber import PARALLEL_HILL_CLIMBER as phc

file = open('pickle_A_0','rb')
par = pickle.load(file)
par.Start_Simulation("GUI",'A')
exit()
file = open('pickle_B_0','rb')
par = pickle.load(file)
par.Start_Simulation("GUI",'B')


file = open('pickle_C_0','rb')
par = pickle.load(file)
par.Start_Simulation("GUI",'C')


if sys.argv[1] == 'random':
    solution.SOLUTION(0,5).Start_Simulation('GUI','control')
elif sys.argv[1] == 'A':
    try:
        num = sys.argv[2]
        file = open('pickle1_'+str(num),'rb')
        par = pickle.load(file)
        par.Start_Simulation("GUI",'A')
    except:
        file = open('pickle1_5', 'rb')
        par5 = pickle.load(file)
        par5.Start_Simulation("GUI",'A')
elif sys.argv[1] == 'B':
    try:
        num = sys.argv[2]
        file = open('pickle2_'+str(num),'rb')
        par = pickle.load(file)
        par.Start_Simulation("GUI",'B')
    except:
        file = open('pickle2_1', 'rb')
        par1 = pickle.load(file)
        par1.Start_Simulation("GUI",'B')
elif sys.argv[1] == 'C':
    try:
        num = sys.argv[2]
        file = open('pickle3_'+str(num),'rb')
        par = pickle.load(file)
        par.Start_Simulation("GUI",'C')
    except:
        file = open('pickle3_1', 'rb')
        par1 = pickle.load(file)
        par1.Start_Simulation("GUI",'C')