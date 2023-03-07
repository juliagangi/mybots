from solution import SOLUTION
import constants as c
import copy
import os
import numpy
import matplotlib.pyplot as plt

class PARALLEL_HILL_CLIMBER:
    def __init__(self,upperlimit):
        os.system("rm brain/brain*.nndf")
        os.system("rm fitness/fitness*.txt")
        os.system("rm body/body*.urdf")
        self.parents = {}
        self.nextAvailableID = 0
        self.fitnessArr = []
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID,upperlimit)
            self.nextAvailableID = self.nextAvailableID + 1

    def Evolve(self,flag):
        self.Evaluate(self.parents,flag)
        self.Get_Best()
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(flag)

    def Evolve_For_One_Generation(self,flag):
        self.Spawn()
        self.Mutate(flag)
        self.Evaluate(self.children,flag)
        self.Print()
        self.Select()  
        self.Update_Fitness()    

    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            newChild = copy.deepcopy(self.parents[parent])
            newChild.Set_ID(self.nextAvailableID)
            self.children[parent] = newChild
            self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self,flag):
        for child in self.children:
            self.children[child].Mutate(flag)

    def Evaluate(self,solutions,flag):
        for parent in solutions:
            solutions[parent].Start_Simulation("DIRECT",flag)
        for parent in solutions:
            solutions[parent].Wait_For_Simulation_To_End()

    def Select(self):
        for parent in self.parents:
            if self.children[parent].fitness > self.parents[parent].fitness:
                self.parents[parent] = self.children[parent]

    def Plot(self):
        for parent in self.parents:
            array = self.parents[parent].fitnessArray
            plt.plot(array, label=str(parent+1), linewidth=1)
        plt.legend()
        plt.xlabel('Generation')
        plt.ylabel('Displacement')
        plt.show()

    def Show_Best(self,parents,flag):
        bestFitness = -1000
        bestParent = None
        for parent in parents:
            currFitness = parent.fitness
            if currFitness > bestFitness:
                bestFitness = currFitness
                bestParent = parent
        bestParent.Start_Simulation("GUI",flag)

    def Update_Fitness(self):
        bestFitness = -1000
        for parent in self.parents:
            currParent = self.parents[parent]
            currFitness = currParent.fitness
            if currFitness > bestFitness:
                bestFitness = currFitness
        self.fitnessArr.append(bestFitness)

    def Best_Parent(self):
        bestFitness = -1000
        bestParent = None
        for parent in self.parents:
            currParent = self.parents[parent]
            currFitness = currParent.fitness
            if currFitness > bestFitness:
                bestFitness = currFitness
                bestParent = currParent 
        return bestParent

    def Print(self):
        print("\n")
        for parent in self.parents:
            print("\n", self.parents[parent].fitness, " | ", self.children[parent].fitness)
        print("\n")




