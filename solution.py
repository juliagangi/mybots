import numpy
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import random
import time
import constants as c
from simulation import SIMULATION

class SOLUTION:
    def __init__(self,nextAvailableID):
        self.weights = 2*numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) - 1
        self.myID = nextAvailableID
        self.numLinks = random.randint(0,9)
        self.links = {}

    def Start_Simulation(self):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        #os.system("python3 simulate.py " + str(self.myID))
        simulation = SIMULATION(self.myID,self.links)
        simulation.Run()
        #os.system("python3 simulate.py " + str(self.myID) + " 2&>1 &")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        #pyrosim.Send_Cube(name="Box", pos=[-3,3,0.5], size=[1,1,1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
        for link in range(self.numLinks):
            xDim = numpy.random.rand()*2
            yDim = numpy.random.rand()*2
            zDim = numpy.random.rand()*2
            xPos = .5*xDim
            yPos = 0
            zPos = 1
            sensor = 0
            mycolor = "0 0 255 1"
            mycolorname = "Blue"
            if random.randint(0,1):
                sensor = 1
                mycolor = "0 128 0 1"
                mycolorname = "Green"
            linkName = "link"+str(link)
            self.links[linkName]=[xPos,xDim,sensor]       
            pyrosim.Send_Cube(name=linkName, pos=[xPos,yPos,zPos], size=[xDim,yDim,zDim], color=mycolor, colorname=mycolorname)
            if link > 0:
                pyrosim.Send_Joint(name = "link"+str(link-1)+"_"+linkName, parent= "link"+str(link-1), child = linkName, type = "revolute", position = [self.links["link"+str(link-1)][1],0,0], jointAxis = "1 0 0")
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        i = 0
        for link in self.links:
            if self.links[link][2]:
                pyrosim.Send_Sensor_Neuron(name = str(i), linkName = link)
                i = i + 1
        pyrosim.End()