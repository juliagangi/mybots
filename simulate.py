from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
parentID = sys.argv[3]
simulation = SIMULATION(directOrGUI,solutionID,parentID)
simulation.Run()
simulation.Get_Fitness()
