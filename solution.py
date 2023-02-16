import numpy
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self,nextAvailableID):
        self.links = {}
        self.joints = []
        self.myID = nextAvailableID
        self.length = random.randint(c.height+2,7)
        self.numMotorNeurons = c.height-1 + 4*self.length
        self.weights = 2*numpy.random.rand(self.numMotorNeurons) - 1
        self.sensorNeuronsArray = []
        self.numSensorNeurons = 0
        for i in range(self.numMotorNeurons+1):
            if random.randint(0,4) > 1:
                self.sensorNeuronsArray.append(1)
                self.numSensorNeurons = self.numSensorNeurons + 1
            else:
                self.sensorNeuronsArray.append(0)
        self.synapseDict = {}
        for motor in range(self.numMotorNeurons):
            sensor = random.randint(0,self.numSensorNeurons-1)
            self.synapseDict[motor] = sensor

    def Start_Simulation(self,directOrGUI,parentID,parentOrChild):
        self.Create_World()
        self.Create_Body(parentID,parentOrChild)      
        self.Create_Brain()
        #os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &")

    def Wait_For_Simulation_To_End(self,directOrGUI):
        while not os.path.exists("fitness/fitness" + str(self.myID) + ".txt"):
            time.sleep(0.3)
        fitnessFileName = "fitness/fitness" + str(self.myID) + ".txt"
        fitnessFile = open(fitnessFileName, "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()
        os.system("rm " + fitnessFileName)

    def Mutate(self):
        rand = random.randint(0,3)
        if rand == 0: # add random sensor
            new_sensor = random.randint(0,len(self.links) - 1)
            while self.sensorNeuronsArray[new_sensor] == 1:
                new_sensor = random.randint(0,len(self.links) - 1)
            self.sensorNeuronsArray[new_sensor] = 1
        if rand == 1: # add random synapse
            motor = random.randint(0,self.numMotorNeurons - 1)
            sensor = random.randint(0,len(self.links) - 1)
            self.synapseDict[motor] = sensor
        if rand == 2: # remove random synapse
            pass
        if rand == 3: # change random synapse
            motor = random.randint(0,self.numMotorNeurons-1)
            self.weights[motor] = 2*random.random() - 1        
        #if rand == 4: # change size of cube? add cube?
        #    file = URDF.load("body" + str(self.myID) + ".urdf")

    def Set_ID(self,ID):
        self.myID = ID

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        #pyrosim.Send_Cube(name="Box", pos=[-3,3,0.5], size=[1,1,1])
        pyrosim.End()

    def Create_Body(self,parentID,parentOrChild):
        if parentOrChild == 'child': # don't want to create new file w random 
            pyrosim.Start_URDF("body/body" + str(self.myID) + ".urdf")
            os.system("rm body/body" + str(self.myID) + ".urdf")
            os.system("cp " + "body/body" + str(parentID) + ".urdf" + " " + "body/body" + str(self.myID) + ".urdf")
        else:
            pyrosim.Start_URDF("body/body" + str(self.myID) + ".urdf")
            overalllink = 0
            for link in range(c.height):
                xDim = numpy.random.rand() + .5
                yDim = numpy.random.rand() + .5
                zDim = numpy.random.rand() + .5
                xPos = 0
                yPos = 0
                zPos = .5*zDim
                mycolor = "0 0 255 1"
                mycolorname = "Blue"
                if self.sensorNeuronsArray[link]:
                    mycolor = "0 128 0 1"
                    mycolorname = "Green"
                jointAxes = [random.randint(0,1), random.randint(0,1), random.randint(0,1)]  
                if sum(jointAxes) == 0:
                    jointAxes[random.randint(0,2)] = 1
                axis = str(jointAxes[0]) + " " + str(jointAxes[1]) + " " + str(jointAxes[2])
                self.links[link]=[xDim,yDim,zDim]       
                pyrosim.Send_Cube(name=str(link), pos=[xPos,yPos,zPos], size=[xDim,yDim,zDim], color=mycolor, colorname=mycolorname)
                if link > 0:
                    pyrosim.Send_Joint(name = str(link-1)+"_"+str(link), parent= str(link-1), child = str(link), type = "revolute", position = [0,0,self.links[link-1][2]], jointAxis = axis)
                    self.joints = self.joints + [str(link-1)+"_"+str(link)]
            dir_array = ['-x','+x','-y','+y']
            linkname = c.height
            toplinkdims = self.links[c.height-1]
            for i in range(len(dir_array)):
                for link in range(self.length):
                    xDim = numpy.random.rand() + .5
                    yDim = numpy.random.rand() + .5
                    zDim = numpy.random.rand() + .5
                    jointAxes = [random.randint(0,1), random.randint(0,1), random.randint(0,1)]  
                    if sum(jointAxes) == 0:
                        jointAxes[random.randint(0,2)] = 1
                    axis = str(jointAxes[0]) + " " + str(jointAxes[1]) + " " + str(jointAxes[2])
                    prevlink = linkname - 1
                    if dir_array[i] == '-x': 
                        #axis = "0 1 0"                   
                        xPos = -xDim*.5
                        xJoint = -self.links[linkname-1][0]
                        if link == 0:
                            xJoint = -.5*toplinkdims[0]
                            prevlink = c.height-1
                        yPos = 0
                        yJoint = 0
                    if dir_array[i] == '+x':
                        #axis = "0 1 0"
                        xPos = xDim*.5
                        xJoint = self.links[linkname-1][0]
                        if link == 0:
                            xJoint = .5*toplinkdims[0]
                            prevlink = c.height-1
                        yPos = 0
                        yJoint = 0
                    if dir_array[i] == '-y':
                        #axis = "1 0 0"
                        yPos = -yDim*.5
                        yJoint = -self.links[linkname-1][1]
                        if link == 0:
                            yJoint = -.5*toplinkdims[1]
                            prevlink = c.height-1
                        xPos = 0
                        xJoint = 0
                    if dir_array[i] == '+y':
                        #axis = "1 0 0"
                        yPos = yDim*.5
                        yJoint = self.links[linkname-1][1]
                        if link == 0:
                            yJoint = .5*toplinkdims[1]
                            prevlink = c.height-1
                        xPos = 0
                        xJoint = 0
                    zPos = .5*zDim
                    mycolor = "0 0 255 1"
                    mycolorname = "Blue"
                    if self.sensorNeuronsArray[overalllink]:
                        mycolor = "0 128 0 1"
                        mycolorname = "Green" 
                    overalllink = overalllink + 1
                    self.links[linkname] = [xDim,yDim,zDim]
                    jointname = str(prevlink)+"_"+str(linkname)
                    self.joints = self.joints + [jointname]
                    #if link == self.link-1:
                    #    lower_dims.append([linkname,xPos,])
                    pyrosim.Send_Cube(name=str(linkname), pos=[xPos,yPos,zPos], size=[xDim,yDim,zDim], color=mycolor, colorname=mycolorname)
                    pyrosim.Send_Joint(name = jointname, parent= str(prevlink), child = str(linkname), type = "revolute", position = [xJoint,yJoint,0], jointAxis = axis)
                    linkname = linkname + 1
                height = self.links[0][2] + self.links[1][2]
                remainder = height
                j = 0
                last = False
                while remainder > 0:
                    xDim = numpy.random.rand() + .5
                    yDim = numpy.random.rand() + .5
                    zDim = numpy.random.rand()*remainder
                    if j > 1:
                        zDim = remainder
                        last = True
                    remainder = remainder - zDim
                    xPos = 0
                    yPos = 0
                    zPos = -.5*zDim
                    jointAxes = [random.randint(0,1), random.randint(0,1), random.randint(0,1)]  
                    if sum(jointAxes) == 0:
                        jointAxes[random.randint(0,2)] = 1
                    axis = str(jointAxes[0]) + " " + str(jointAxes[1]) + " " + str(jointAxes[2])
                    if random.randint(0,1):
                        self.sensorNeuronsArray.append(1)
                        mycolor = "0 128 0 1"
                        mycolorname = "Green" 
                        self.numSensorNeurons = self.numSensorNeurons + 1
                    else:
                        self.sensorNeuronsArray.append(0)
                        mycolor = "0 0 255 1"
                        mycolorname = "Blue"
                    #overalllink = overalllink + 1
                    prevlink = linkname - 1
                    if dir_array[i] == '-x':
                        xJoint = 0
                        yJoint = 0
                        zJoint = -zDim
                        if j == 0:
                            xJoint = -.5*self.links[prevlink][0]
                            zJoint = 0
                    if dir_array[i] == '+x':
                        xJoint = 0
                        yJoint = 0
                        zJoint = -zDim
                        if j == 0:
                            xJoint = .5*self.links[prevlink][0]
                            zJoint = 0
                    if dir_array[i] == '-y':
                        xJoint = 0
                        yJoint = 0
                        zJoint = -zDim
                        if j == 0:
                            yJoint = -.5*self.links[prevlink][1]
                            zJoint = 0
                    if dir_array[i] == '+y':
                        xJoint = 0
                        yJoint = 0
                        zJoint = -zDim
                        if j == 0:
                            yJoint = .5*self.links[prevlink][1]
                            zJoint = 0
                    self.links[linkname] = [xDim,yDim,zDim]
                    jointName = str(prevlink)+"_"+str(linkname)
                    self.joints = self.joints + [jointName]
                    pyrosim.Send_Cube(name=str(linkname), pos=[xPos,yPos,zPos], size=[xDim,yDim,zDim], color=mycolor, colorname=mycolorname)
                    if not last:
                        pyrosim.Send_Joint(name = jointname, parent= str(prevlink), child = str(linkname), type = "revolute", position = [xJoint,yJoint,zJoint], jointAxis = axis)
                        self.numMotorNeurons = self.numMotorNeurons + 1
                    linkname = linkname + 1
                    j = j + 1          
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain/brain" + str(self.myID) + ".nndf")
        i = 0
        for link in self.links:
            if self.sensorNeuronsArray[link]:
                pyrosim.Send_Sensor_Neuron(name = i, linkName = str(link))
                i = i + 1
        for joint in self.joints:
            pyrosim.Send_Motor_Neuron(name = i, jointName = joint)
            i = i + 1
        for motor in self.synapseDict:
            sensor = self.synapseDict[motor]
            pyrosim.Send_Synapse(sourceNeuronName = sensor, targetNeuronName = motor+self.numSensorNeurons, weight = self.weights[motor])
        pyrosim.End()