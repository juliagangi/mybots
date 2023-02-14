import numpy
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import random
import constants as c
from simulation import SIMULATION

class SOLUTION:
    def __init__(self,nextAvailableID):
        self.weights = 2*numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) - 1
        self.myID = nextAvailableID
        self.numLinks = random.randint(2,12)
        print(self.numLinks)
        self.links = {}
        self.joints = []

    def Start_Simulation(self):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        simulation = SIMULATION(self.myID)
        simulation.Run()

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        height = c.height
        length = c.length
        overalllink = 0
        for link in range(height):
            xDim = numpy.random.rand()
            yDim = numpy.random.rand()
            zDim = numpy.random.rand()
            xPos = 0
            yPos = 0
            zPos = .5*zDim
            sensor = 0
            mycolor = "0 0 255 1"
            mycolorname = "Blue"
            if random.randint(0,1):
                sensor = 1
                mycolor = "0 128 0 1"
                mycolorname = "Green"            
            self.links[link]=[sensor,xDim,yDim,zDim]       
            pyrosim.Send_Cube(name=str(link), pos=[xPos,yPos,zPos], size=[xDim,yDim,zDim], color=mycolor, colorname=mycolorname)
            if link > 0:
                pyrosim.Send_Joint(name = str(link-1)+"_"+str(link), parent= str(link-1), child = str(link), type = "revolute", position = [0,0,self.links[link-1][3]], jointAxis = "1 1 1")
                self.joints = self.joints + [str(link-1)+"_"+str(link)]
        dir_array = ['-x','+x','-y','+y']
        linkname = height
        toplinkdims = self.links[height-1][1:4]
        for i in range(len(dir_array)):
            for link in range(length):
                xDim = numpy.random.rand()
                yDim = numpy.random.rand()
                zDim = numpy.random.rand()
                prevlink = linkname - 1
                if dir_array[i] == '-x':
                    axis = "0 1 0"
                    xPos = -xDim*.5
                    xJoint = -self.links[linkname-1][1]
                    if link == 0:
                        xJoint = -.5*toplinkdims[0]
                        prevlink = height-1
                    yPos = 0
                    yJoint = 0
                if dir_array[i] == '+x':
                    axis = "0 1 0"
                    xPos = xDim*.5
                    xJoint = self.links[linkname-1][1]
                    if link == 0:
                        xJoint = .5*toplinkdims[0]
                        prevlink = height-1
                    yPos = 0
                    yJoint = 0
                if dir_array[i] == '-y':
                    axis = "1 0 0"
                    yPos = -yDim*.5
                    yJoint = -self.links[linkname-1][2]
                    if link == 0:
                        yJoint = -.5*toplinkdims[1]
                        prevlink = height-1
                    xPos = 0
                    xJoint = 0
                if dir_array[i] == '+y':
                    axis = "1 0 0"
                    yPos = yDim*.5
                    yJoint = self.links[linkname-1][2]
                    if link == 0:
                        yJoint = .5*toplinkdims[1]
                        prevlink = height-1
                    xPos = 0
                    xJoint = 0
                zPos = .5*zDim
                sensor = 0
                mycolor = "0 0 255 1"
                mycolorname = "Blue"
                if c.sensorNeuronsArray[overalllink]:
                    sensor = 1
                    mycolor = "0 128 0 1"
                    mycolorname = "Green" 
                overalllink = overalllink + 1
                self.links[linkname] = [sensor,xDim,yDim,zDim]
                jointname = str(prevlink)+"_"+str(linkname)
                self.joints = self.joints + [jointname]
                pyrosim.Send_Cube(name=str(linkname), pos=[xPos,yPos,zPos], size=[xDim,yDim,zDim], color=mycolor, colorname=mycolorname)
                pyrosim.Send_Joint(name = jointname, parent= str(prevlink), child = str(linkname), type = "revolute", position = [xJoint,yJoint,0], jointAxis = axis)
                linkname = linkname + 1
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        i = 0
        for link in self.links:
            if self.links[link][0]:
                pyrosim.Send_Sensor_Neuron(name = i, linkName = str(link))
                i = i + 1
        for joint in self.joints:
            pyrosim.Send_Motor_Neuron(name = i, jointName = joint)
            i = i + 1
        for motor in range(c.numMotorNeurons):
            sensor = numpy.random.randint(0,c.numSensorNeurons)
            pyrosim.Send_Synapse(sourceNeuronName = sensor, targetNeuronName = motor+c.numSensorNeurons, weight = numpy.random.rand()*2 - 1)
        pyrosim.End()
