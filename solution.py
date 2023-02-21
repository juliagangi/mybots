import numpy
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import random
import time
import constants as c
#from parallelHillClimber import PARALLEL_HILL_CLIMBER as phc

class SOLUTION:
    def __init__(self,nextAvailableID):
        self.links = {}
        self.joints = []
        self.myID = nextAvailableID
        self.length = random.randint(1,5)
        self.numMotorNeurons = 4*self.length
        self.sensorNeuronsArray = []
        self.numSensorNeurons = 0
        const = random.randint(0,self.numMotorNeurons)
        for i in range(self.numMotorNeurons+1):
            if i == const:
                self.sensorNeuronsArray.append(1)
                self.numSensorNeurons = self.numSensorNeurons + 1                
            elif random.randint(0,4) > 1:
                self.sensorNeuronsArray.append(1)
                self.numSensorNeurons = self.numSensorNeurons + 1
            else:
                self.sensorNeuronsArray.append(0)
        self.synapseDict = {}
        self.jointDict = {}
        for motor in range(self.numMotorNeurons):
            sensor = random.randint(0,self.numSensorNeurons-1)
            self.synapseDict[motor] = sensor

    def Start_Simulation(self,directOrGUI,isfinal):
        self.Create_World()
        self.Create_Body(isfinal) 
        #self.weights = 2*numpy.random.rand(self.numSensorNeurons,self.numMotorNeurons) - 1
        self.weights = 2*numpy.random.rand(self.numMotorNeurons) - 1
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")
        #os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &")

    def Wait_For_Simulation_To_End(self,directOrGUI):
        while not os.path.exists("fitness/fitness" + str(self.myID) + ".txt"):
            time.sleep(0.3)
        fitnessFileName = "fitness/fitness" + str(self.myID) + ".txt"
        fitnessFile = open(fitnessFileName, "r")
        try:
            self.fitness = float(fitnessFile.read())
        except: 
            return
        fitnessFile.close()
        os.system("rm " + fitnessFileName)

    def Mutate(self,parentID):
        pyrosim.Start_URDF("body/body" + str(self.myID) + ".urdf")
        os.system("rm body/body" + str(self.myID) + ".urdf")
        os.system("cp " + "body/body" + str(parentID) + ".urdf" + " " + "body/body" + str(self.myID) + ".urdf")
        rand = random.randint(0,3)
        if rand == 0: # add sensor neuron to random link
            new_sensor = random.randint(0,len(self.links) - 1)
            while self.sensorNeuronsArray[new_sensor] == 1:
                new_sensor = random.randint(0,len(self.links) - 1)
            self.sensorNeuronsArray[new_sensor] = 1
        if rand == 1: # change sensor neuron that motor neuron affects
            motor = random.randint(0,self.numMotorNeurons - 1)  
            sensor = random.randint(0,len(self.links) - 1)
            self.synapseDict[motor] = sensor
        if rand == 2: # change random joint axis
            motor = random.randint(0,self.numMotorNeurons-1)
            jointAxes = [random.randint(0,1), random.randint(0,1), random.randint(0,1)]  
            if sum(jointAxes) == 0:
                jointAxes[random.randint(0,2)] = 1
            axis = str(jointAxes[0]) + " " + str(jointAxes[1]) + " " + str(jointAxes[2])
            self.jointDict[motor] = axis
        if rand == 3: # change random synapse's weight
            motor = random.randint(0,self.numMotorNeurons-1)
            #sensor = random.randint(0,self.numSensorNeurons-1)
            self.weights[motor] = 2*random.random() - 1        
        #if rand == 4: # change size of cube? add cube?
        #    file = URDF.load("body" + str(self.myID) + ".urdf")

    def Set_ID(self,ID):
        self.myID = ID

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        #pyrosim.Send_Cube(name="Box", pos=[-3,3,0.5], size=[1,1,1])
        pyrosim.End()

    def Create_Body(self,isfinal):
        if isfinal:
            return
        else:
            pyrosim.Start_URDF("body/body" + str(self.myID) + ".urdf")
            overalllink = 0
            xDim = 1.5
            yDim = 1.5
            zDim = .8
            xPos = 0
            yPos = 0
            zPos = c.height
            mycolor = "0 0 255 1"
            mycolorname = "Blue"
            if self.sensorNeuronsArray[0]:
                mycolor = "0 128 0 1"
                mycolorname = "Green"
            self.links[0]=[xDim,yDim,zDim]     
            pyrosim.Send_Cube(name="0", pos=[xPos,yPos,zPos], size=[xDim,yDim,zDim], color=mycolor, colorname=mycolorname)
            dir_array = ['-x','+x','-y','+y']
            linkname = 1
            for i in range(len(dir_array)):
                for link in range(self.length):
                    xDim = numpy.random.rand() 
                    yDim = numpy.random.rand() 
                    zDim = numpy.random.rand() 
                    jointAxes = [random.randint(0,1), random.randint(0,1), random.randint(0,1)]  
                    if sum(jointAxes) == 0:
                        jointAxes[random.randint(0,2)] = 1
                    axis = str(jointAxes[0]) + " " + str(jointAxes[1]) + " " + str(jointAxes[2])
                    self.jointDict[linkname - 1] = axis
                    prevlink = linkname - 1
                    zJoint = 0
                    zPos = 0
                    if link == 0:
                        zJoint = c.height
                        prevlink = 0
                    if dir_array[i] == '-x': 
                        xPos = -xDim*.5
                        xJoint = -self.links[prevlink][0]
                        if link == 0:
                            xJoint = -.5*self.links[0][0]
                        yPos = 0
                        yJoint = 0
                    if dir_array[i] == '+x':
                        xPos = xDim*.5
                        xJoint = self.links[prevlink][0]
                        if link == 0:
                            xJoint = .5*self.links[0][0]
                        yPos = 0
                        yJoint = 0
                    if dir_array[i] == '-y':
                        yPos = -yDim*.5
                        yJoint = -self.links[prevlink][1]
                        if link == 0:
                            yJoint = -.5*self.links[0][1]
                        xPos = 0
                        xJoint = 0
                    if dir_array[i] == '+y':
                        yPos = yDim*.5
                        yJoint = self.links[prevlink][1]
                        if link == 0:
                            yJoint = .5*self.links[0][1]
                        xPos = 0
                        xJoint = 0
                    mycolor = "0 0 255 1"
                    mycolorname = "Blue"
                    if self.sensorNeuronsArray[overalllink]:
                        mycolor = "0 128 0 1"
                        mycolorname = "Green" 
                    overalllink = overalllink + 1
                    self.links[linkname] = [xDim,yDim,zDim]
                    jointname = str(prevlink)+"_"+str(linkname)
                    self.joints = self.joints + [jointname]
                    pyrosim.Send_Cube(name=str(linkname), pos=[xPos,yPos,zPos], size=[xDim,yDim,zDim], color=mycolor, colorname=mycolorname)
                    pyrosim.Send_Joint(name = jointname, parent= str(prevlink), child = str(linkname), type = "revolute", position = [xJoint,yJoint,zJoint], jointAxis = axis)
                    linkname = linkname + 1
                height = c.height - .5*self.links[0][2]
                remainder = height
                j = 0
                while remainder > 0:
                    xDim = numpy.random.rand()
                    yDim = numpy.random.rand()
                    zDim = numpy.random.rand()*remainder
                    if j > 1:
                        zDim = remainder
                    remainder = remainder - zDim
                    xPos = 0
                    yPos = 0
                    zPos = -.5*zDim
                    jointAxes = [random.randint(0,1), random.randint(0,1), random.randint(0,1)]  
                    if sum(jointAxes) == 0:
                        jointAxes[random.randint(0,2)] = 1
                    axis = str(jointAxes[0]) + " " + str(jointAxes[1]) + " " + str(jointAxes[2])
                    self.jointDict[linkname-1] = axis
                    if random.randint(0,1):
                        self.sensorNeuronsArray.append(1)
                        mycolor = "0 128 0 1"
                        mycolorname = "Green" 
                        self.numSensorNeurons = self.numSensorNeurons + 1
                    else:
                        self.sensorNeuronsArray.append(0)
                        mycolor = "0 0 255 1"
                        mycolorname = "Blue"
                    prevlink = linkname - 1
                    if dir_array[i] == '-x':
                        xJoint = 0
                        yJoint = 0
                        zJoint = -self.links[prevlink][2]
                        if j == 0:
                            xJoint = -.5*self.links[prevlink][0]
                            zJoint = -.5*self.links[prevlink][2]
                    if dir_array[i] == '+x':
                        xJoint = 0
                        yJoint = 0
                        zJoint = -self.links[prevlink][2]
                        if j == 0:
                            xJoint = .5*self.links[prevlink][0]
                            zJoint = -.5*self.links[prevlink][2]
                    if dir_array[i] == '-y':
                        xJoint = 0
                        yJoint = 0
                        zJoint = -self.links[prevlink][2]
                        if j == 0:
                            yJoint = -.5*self.links[prevlink][1]
                            zJoint = -.5*self.links[prevlink][2]
                    if dir_array[i] == '+y':
                        xJoint = 0
                        yJoint = 0
                        zJoint = -self.links[prevlink][2]
                        if j == 0:
                            yJoint = .5*self.links[prevlink][1]
                            zJoint = -.5*self.links[prevlink][2]
                    self.links[linkname] = [xDim,yDim,zDim]
                    jointName = str(prevlink)+"_"+str(linkname)
                    self.joints = self.joints + [jointName]
                    pyrosim.Send_Cube(name=str(linkname), pos=[xPos,yPos,zPos], size=[xDim,yDim,zDim], color=mycolor, colorname=mycolorname)
                    pyrosim.Send_Joint(name = jointName, parent= str(prevlink), child = str(linkname), type = "revolute", position = [xJoint,yJoint,zJoint], jointAxis = axis)
                    self.numMotorNeurons = self.numMotorNeurons + 1
                    self.synapseDict[self.numMotorNeurons - 1] = random.randint(0,self.numSensorNeurons-1)
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