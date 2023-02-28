from parallelHillClimber import PARALLEL_HILL_CLIMBER
import os
import random
import constants as c
import matplotlib.pyplot as plt

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
phc.Plot()