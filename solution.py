import numpy
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self,nextAvailableID):
        self.weights = 2*numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) - 1
        self.links = {}
        self.joints = []
        self.myID = nextAvailableID

    def Start_Simulation(self,directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        #os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &")

    def Wait_For_Simulation_To_End(self,directOrGUI):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.3)
        print("here")
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        fitnessFile = open(fitnessFileName, "r")
        self.fitness = float(fitnessFile.read())
        print(self.fitness)
        fitnessFile.close()
        os.system("rm " + fitnessFileName)

    def Mutate(self):
        row = random.randint(0,c.numSensorNeurons-1)
        col = random.randint(0,c.numMotorNeurons-1)
        self.weights[row,col] = 2*random.random() - 1

    def Set_ID(self,ID):
        self.myID = ID

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-3,3,0.5], size=[1,1,1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        height = c.height
        length = c.length
        overalllink = 0
        for link in range(height):
            xDim = numpy.random.rand()+1
            yDim = numpy.random.rand()+1
            zDim = numpy.random.rand()+1
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
                xDim = numpy.random.rand()+1
                yDim = numpy.random.rand()+1
                zDim = numpy.random.rand()+1
                prevlink = linkname - 1
                if dir_array[i] == '-x':
                    axis = "0 -1 0"
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
                    axis = "-1 0 0"
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
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])
        pyrosim.End()
        '''
        for sensor in range(len(sensors)):
            for motor in range(len(motors)):
                pyrosim.Send_Synapse(sourceNeuronName = sensors[sensor], targetNeuronName = motors[motor], weight = self.weights[sensor][motor])
        pyrosim.End()
        '''
