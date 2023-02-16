from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain/brain*.nndf")
        os.system("rm fitness/fitness*.txt")
        os.system("rm body/body*.urdf")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Evolve(self):
        self.Evaluate(self.parents,"parent")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children,"child")
        self.Print()
        self.Select()        

    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            newChild = copy.deepcopy(self.parents[parent])
            newChild.Set_ID(self.nextAvailableID)
            self.children[parent] = newChild
            self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Evaluate(self,solutions,parentOrChild):
        for parent in solutions:
            solutions[parent].Start_Simulation("DIRECT",self.parents[parent].myID,parentOrChild)
        for parent in solutions:
            solutions[parent].Wait_For_Simulation_To_End("DIRECT")

    def Select(self):
        for parent in self.parents:
            if self.children[parent].fitness > self.parents[parent].fitness:
                self.parents[parent] = self.children[parent]

    def Show_Best(self):
        bestFitness = -1000
        bestParent = None
        for parent in self.parents:
            currParent = self.parents[parent]
            currFitness = currParent.fitness
            if currFitness > bestFitness:
                bestFitness = currFitness
                bestParent = currParent
        bestParent.Start_Simulation("GUI",bestParent.myID,"final")

    def Print(self):
        print("\n")
        for parent in self.parents:
            print("\n", self.parents[parent].fitness, " | ", self.children[parent].fitness)
        print("\n")




