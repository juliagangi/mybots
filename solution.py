import numpy
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import random
import constants as c
from simulation import SIMULATION

class SOLUTION:
    def __init__(self,nextAvailableID):
        self.myID = nextAvailableID
        self.numLinks = random.randint(2,12)
        print(self.numLinks)
        self.links = {}

    def Start_Simulation(self):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        simulation = SIMULATION(self.myID,self.links)
        simulation.Run()

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
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
            if link < self.numLinks-1:
                pyrosim.Send_Joint(name = linkName+"_link"+str(link+1), parent= linkName, child = "link"+str(link+1), type = "revolute", position = [xDim,0,0], jointAxis = "1 0 0")
            #if link > 0:
            #    pyrosim.Send_Joint(name = "link"+str(link-1)+"_"+linkName, parent= "link"+str(link-1), child = linkName, type = "revolute", position = [self.links["link"+str(link-1)][1],0,0], jointAxis = "1 0 0")
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        i = 0
        linkNum = 0
        sensors = []
        motors = []
        for link in self.links:
            if self.links[link][2]:
                pyrosim.Send_Sensor_Neuron(name = i, linkName = link)
                sensors = sensors + [i]
                i = i + 1
            if linkNum < self.numLinks - 1:
                pyrosim.Send_Motor_Neuron(name = i, jointName = link+"_link"+str(linkNum+1))
                motors = motors + [i]
                i = i + 1
            linkNum = linkNum + 1
        for sensor in range(len(sensors)):
            for motor in range(len(motors)):
                pyrosim.Send_Synapse(sourceNeuronName = sensor, targetNeuronName = motor, weight = 1)
        pyrosim.End()