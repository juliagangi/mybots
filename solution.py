import numpy
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import random
import constants as c
from simulation import SIMULATION

class SOLUTION:
    def __init__(self,nextAvailableID):
        self.links = {}
        self.joints = []
        self.myID = nextAvailableID
        self.length = random.randint(1,5)
        self.numMotorNeurons = 4*self.length
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

    def Start_Simulation(self):
        self.Create_World()
        self.Create_Body()
        self.weights = 2*numpy.random.rand(self.numMotorNeurons) - 1
        #self.weights = 2*numpy.random.rand(self.numSensorNeurons,self.numMotorNeurons) - 1
        self.Create_Brain()
        simulation = SIMULATION(self.myID)
        simulation.Run()

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    def Create_Body(self):
        if 1:
            pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
            overalllink = 0
            xDim = 1.5
            yDim = 1.5
            zDim = .8
            '''
            xDim = numpy.random.rand() + .5
            yDim = numpy.random.rand() + .5
            zDim = numpy.random.rand() + .5 
            '''
            xPos = 0
            yPos = 0
            zPos = c.height
            mycolor = "0 0 255 1"
            mycolorname = "Blue"
            if self.sensorNeuronsArray[0]:
                mycolor = "0 128 0 1"
                mycolorname = "Green"
            jointAxes = [random.randint(0,1), random.randint(0,1), random.randint(0,1)]  
            if sum(jointAxes) == 0:
                jointAxes[random.randint(0,2)] = 1
            axis = str(jointAxes[0]) + " " + str(jointAxes[1]) + " " + str(jointAxes[2])
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
                    prevlink = linkname - 1
                    zJoint = 0
                    zPos = 0
                    if link == 0:
                        zJoint = c.height
                        prevlink = 0
                    if dir_array[i] == '-x': 
                        #axis = "0 1 0"                   
                        xPos = -xDim*.5
                        xJoint = -self.links[prevlink][0]
                        if link == 0:
                            xJoint = -.5*self.links[0][0]
                        yPos = 0
                        yJoint = 0
                    if dir_array[i] == '+x':
                        #axis = "0 1 0"
                        xPos = xDim*.5
                        xJoint = self.links[prevlink][0]
                        if link == 0:
                            xJoint = .5*self.links[0][0]
                        yPos = 0
                        yJoint = 0
                    if dir_array[i] == '-y':
                        #axis = "1 0 0"
                        yPos = -yDim*.5
                        yJoint = -self.links[prevlink][1]
                        if link == 0:
                            yJoint = -.5*self.links[0][1]
                        xPos = 0
                        xJoint = 0
                    if dir_array[i] == '+y':
                        #axis = "1 0 0"
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
            '''
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
                    prevlink = linkname - 1
                    if dir_array[i] == '-x':
                        xJoint = 0
                        yJoint = 0
                        zJoint = -self.links[prevlink][2]
                        if j == 0:
                            xJoint = -.5*self.links[prevlink][0]
                            zJoint = 0
                    if dir_array[i] == '+x':
                        xJoint = 0
                        yJoint = 0
                        zJoint = -self.links[prevlink][2]
                        if j == 0:
                            xJoint = .5*self.links[prevlink][0]
                            zJoint = 0
                    if dir_array[i] == '-y':
                        xJoint = 0
                        yJoint = 0
                        zJoint = -self.links[prevlink][2]
                        if j == 0:
                            yJoint = -.5*self.links[prevlink][1]
                            zJoint = 0
                    if dir_array[i] == '+y':
                        xJoint = 0
                        yJoint = 0
                        zJoint = -self.links[prevlink][2]
                        if j == 0:
                            yJoint = .5*self.links[prevlink][1]
                            zJoint = 0
                    self.links[linkname] = [xDim,yDim,zDim]
                    jointName = str(prevlink)+"_"+str(linkname)
                    self.joints = self.joints + [jointName]
                    pyrosim.Send_Cube(name=str(linkname), pos=[xPos,yPos,zPos], size=[xDim,yDim,zDim], color=mycolor, colorname=mycolorname)
                    pyrosim.Send_Joint(name = jointName, parent= str(prevlink), child = str(linkname), type = "revolute", position = [xJoint,yJoint,zJoint], jointAxis = axis)
                    self.numMotorNeurons = self.numMotorNeurons + 1
                    self.synapseDict[self.numMotorNeurons - 1] = random.randint(0,self.numSensorNeurons-1)
                    linkname = linkname + 1
                    j = j + 1   
            '''
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        i = 0
        for link in self.links:
            if self.sensorNeuronsArray[link]:
                pyrosim.Send_Sensor_Neuron(name = i, linkName = str(link))
                i = i + 1
        for joint in self.joints:
            pyrosim.Send_Motor_Neuron(name = i, jointName = joint)
            i = i + 1
        '''
        for motor in range(self.numMotorNeurons):
            for sensor in range(self.numSensorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = sensor, targetNeuronName = motor+self.numSensorNeurons, weight = self.weights[sensor][motor])
        '''
        for motor in self.synapseDict:
            sensor = self.synapseDict[motor]
            pyrosim.Send_Synapse(sourceNeuronName = sensor, targetNeuronName = motor+self.numSensorNeurons, weight = self.weights[motor])
        
        pyrosim.End()