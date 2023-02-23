import numpy
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self,nextAvailableID):
        self.myID = nextAvailableID
        self.fitnessArray = []
        self.height = random.randint(1,10)
        self.numLinks = self.height
        self.links = []
        dirArray = ['-x','+x','-y','+y']
        for i in range(self.height):
            if random.randint(0,1):
                dir = dirArray[random.randint(0,3)]
                length = random.randint(1,5)
                self.links.append([dir,length])
                self.numLinks = self.numLinks + length
        self.dims = []
        self.sensors = []
        self.numSensorNeurons = 0
        for link in range(self.numLinks):
            if random.randint(0,4) > 1:
                self.sensors.append(1)
                self.numSensorNeurons = self.numSensorNeurons + 1
            else:
                self.sensors.append(0)
            if link < self.height:
                dims = [1,1,1]
            else:
                dims = [random.random()*.5+.5,random.random()*.5+.5,random.random()*.5+.5]
            self.dims.append(dims)
        self.numJoints = self.numLinks - 1
        self.weights = []
        self.axes = []
        for motor in range(self.numJoints):
            self.weights.append(2*random.random() - 1)
            jointAxes = [random.randint(0,1), random.randint(0,1), random.randint(0,1)]  
            if sum(jointAxes) == 0:
                jointAxes[random.randint(0,2)] = 1
            axis = str(jointAxes[0]) + " " + str(jointAxes[1]) + " " + str(jointAxes[2])
            self.axes.append(axis)        
        '''
        self.myID = nextAvailableID
        self.length = random.randint(1,5)
        self.numJoints = 4*self.length + 12
        self.numLinks = 4*self.length + 13
        self.numSensorNeurons = 0
        self.links = []
        self.sensors = []
        self.fitnessArray = []
        const = random.randint(0,self.numLinks-1)
        for link in range(self.numLinks):
            if link == const:
                self.sensors.append(1)
                self.numSensorNeurons = self.numSensorNeurons + 1                
            elif random.randint(0,4) > 1:
                self.sensors.append(1)
                self.numSensorNeurons = self.numSensorNeurons + 1
            else:
                self.sensors.append(0)
            self.links.append([random.random(), random.random(), random.random()])
        self.weights = []
        self.axes = []
        for motor in range(self.numJoints):
            self.weights.append(2*random.random() - 1)
            jointAxes = [random.randint(0,1), random.randint(0,1), random.randint(0,1)]  
            if sum(jointAxes) == 0:
                jointAxes[random.randint(0,2)] = 1
            axis = str(jointAxes[0]) + " " + str(jointAxes[1]) + " " + str(jointAxes[2])
            self.axes.append(axis)
        '''

    def Start_Simulation(self,directOrGUI):
        self.Create_World()
        self.Create_Body() 
        self.Create_Brain()
        #os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &")

    def Wait_For_Simulation_To_End(self,directOrGUI):
        while not os.path.exists("fitness/fitness" + str(self.myID) + ".txt"):
            time.sleep(0.3)
        fitnessFileName = "fitness/fitness" + str(self.myID) + ".txt"
        fitnessFile = open(fitnessFileName, "r")
        #try:
        self.fitness = float(fitnessFile.read())
        #except: 
        #    return
        fitnessFile.close()
        os.system("rm " + fitnessFileName)

    def Mutate(self):
        rand = random.randint(0,4)
        if rand == 0: # add sensor neuron
            new_sensor = random.randint(0,self.numLinks - 1)
            while self.sensors[new_sensor] == 1:
                new_sensor = random.randint(0,self.numLinks - 1)
            self.sensors[new_sensor] = 1
        if rand == 1: # remove sensor neuron
            curr_sensor = random.randint(0,self.numLinks - 1)
            while self.sensors[curr_sensor] == 0:
                curr_sensor = random.randint(0,self.numLinks - 1)
            self.sensors[curr_sensor] = 0
        if rand == 2: # change link dimension
            randlink = random.randint(0,self.numLinks - 1)
            randdir = random.randint(0,2)
            self.links[randlink][randdir] = 2*random.random() - 1
        if rand == 3: # change random joint axis
            motor = random.randint(0,self.numJoints - 1)
            jointAxes = [random.randint(0,1), random.randint(0,1), random.randint(0,1)]  
            if sum(jointAxes) == 0:
                jointAxes[random.randint(0,2)] = 1
            axis = str(jointAxes[0]) + " " + str(jointAxes[1]) + " " + str(jointAxes[2])
            self.axes[motor] = axis
        if rand == 4: # change random joint's weight
            motor = random.randint(0,self.numJoints - 1)
            self.weights[motor] = 2*random.random() - 1  

    def Set_ID(self,ID):
        self.myID = ID

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        #pyrosim.Send_Cube(name="Box", pos=[-3,3,0.5], size=[1,1,1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body/body" + str(self.myID) + ".urdf")
        self.joints = []
        linkname = 0
        for link in range(self.height):
            xPos = 0
            yPos = 0
            zPos = .5
            zJoint = .5
            if link == 1:
                zJoint = 1
            mycolor = "0 0 255 1"
            mycolorname = "Blue"
            if self.sensors[linkname]:
                mycolor = "0 128 0 1"
                mycolorname = "Green" 
            jointname = str(linkname-1)+"_"+str(linkname)
            self.joints.append(jointname)
            pyrosim.Send_Cube(name=str(linkname), pos=[xPos,yPos,zPos], size=self.dims[linkname], color=mycolor, colorname=mycolorname)
            if link != 0:
                pyrosim.Send_Joint(name = jointname, parent= str(linkname-1), child = str(linkname), type = "revolute", position = [0,0,zJoint], jointAxis = self.axes[linkname-1])
            linkname = linkname + 1
        for link1 in range(self.height):
            for link2 in range(self.links[link1][1]):
                dir = self.dims[link1][0]
                zJoint = 0
                zPos = 0
                if link2 == 0:
                    zJoint = c.height
                    prevlink = 0
                if dir == '-x': 
                    xPos = -self.dims[linkname][0]*.5
                    xJoint = -self.dims[prevlink][0]
                    yPos = 0
                    yJoint = 0                    
                    if link == 0:
                        xJoint = -.5*self.dims[0][0]
                if dir == '+x':
                    xPos = self.dims[linkname][0]*.5
                    xJoint = self.dims[prevlink][0]
                    yPos = 0
                    yJoint = 0                    
                    if link == 0:
                        xJoint = .5*self.links[0][0]
                if dir == '-y':
                    yPos = -self.dims[linkname][1]*.5
                    yJoint = -self.dims[prevlink][1]
                    xPos = 0
                    xJoint = 0                    
                    if link == 0:
                        yJoint = -.5*self.dims[0][1]
                if dir == '+y':
                    yPos = self.dims[linkname][1]*.5
                    yJoint = self.dims[prevlink][1]
                    xPos = 0
                    xJoint = 0                    
                    if link == 0:
                        yJoint = .5*self.dims[0][1]
                mycolor = "0 0 255 1"
                mycolorname = "Blue"
                if self.sensors[linkname]:
                    mycolor = "0 128 0 1"
                    mycolorname = "Green" 
                jointname = str(prevlink)+"_"+str(linkname)
                self.joints.append(jointname)
                pyrosim.Send_Cube(name=str(linkname), pos=[xPos,yPos,zPos], size=self.links[linkname], color=mycolor, colorname=mycolorname)
                pyrosim.Send_Joint(name = jointname, parent= str(prevlink), child = str(linkname), type = "revolute", position = [xJoint,yJoint,zJoint], jointAxis = self.axes[linkname-1])
                linkname = linkname + 1           
        '''
        self.joints = []
        xDim = 1.5
        yDim = 1.5
        zDim = .8
        xPos = 0
        yPos = 0
        zPos = c.height
        mycolor = "0 0 255 1"
        mycolorname = "Blue"
        if self.sensors[0]:
            mycolor = "0 128 0 1"
            mycolorname = "Green"
        self.links[0]=[xDim,yDim,zDim]     
        pyrosim.Send_Cube(name="0", pos=[xPos,yPos,zPos], size=[xDim,yDim,zDim], color=mycolor, colorname=mycolorname)
        dir_array = ['-x','+x','-y','+y']
        linkname = 1
        for i in range(len(dir_array)):
            for link in range(self.length):
                prevlink = linkname - 1
                zJoint = 0
                zPos = 0
                if link == 0:
                    zJoint = c.height
                    prevlink = 0
                if dir_array[i] == '-x': 
                    xPos = -self.links[linkname][0]*.5
                    xJoint = -self.links[prevlink][0]
                    yPos = 0
                    yJoint = 0                    
                    if link == 0:
                        xJoint = -.5*self.links[0][0]
                if dir_array[i] == '+x':
                    xPos = self.links[linkname][0]*.5
                    xJoint = self.links[prevlink][0]
                    yPos = 0
                    yJoint = 0                    
                    if link == 0:
                        xJoint = .5*self.links[0][0]
                if dir_array[i] == '-y':
                    yPos = -self.links[linkname][1]*.5
                    yJoint = -self.links[prevlink][1]
                    xPos = 0
                    xJoint = 0                    
                    if link == 0:
                        yJoint = -.5*self.links[0][1]
                if dir_array[i] == '+y':
                    yPos = self.links[linkname][1]*.5
                    yJoint = self.links[prevlink][1]
                    xPos = 0
                    xJoint = 0                    
                    if link == 0:
                        yJoint = .5*self.links[0][1]
                mycolor = "0 0 255 1"
                mycolorname = "Blue"
                if self.sensors[linkname]:
                    mycolor = "0 128 0 1"
                    mycolorname = "Green" 
                jointname = str(prevlink)+"_"+str(linkname)
                self.joints.append(jointname)
                pyrosim.Send_Cube(name=str(linkname), pos=[xPos,yPos,zPos], size=self.links[linkname], color=mycolor, colorname=mycolorname)
                pyrosim.Send_Joint(name = jointname, parent= str(prevlink), child = str(linkname), type = "revolute", position = [xJoint,yJoint,zJoint], jointAxis = self.axes[linkname-1])
                linkname = linkname + 1
            height = c.height - .5*self.links[0][2]
            remainder = height
            j = 0
            for j in range(3):
                xDim = self.links[linkname][0]
                yDim = self.links[linkname][1]
                zDim = height/3
                self.links[linkname][2] = height/3
                remainder = remainder - zDim
                xPos = 0
                yPos = 0
                zPos = -.5*zDim
                if self.sensors:
                    mycolor = "0 128 0 1"
                    mycolorname = "Green" 
                else:
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
                jointName = str(prevlink)+"_"+str(linkname)
                self.joints.append(jointName)
                pyrosim.Send_Cube(name=str(linkname), pos=[xPos,yPos,zPos], size=[xDim,yDim,zDim], color=mycolor, colorname=mycolorname)
                pyrosim.Send_Joint(name = jointName, parent= str(prevlink), child = str(linkname), type = "revolute", position = [xJoint,yJoint,zJoint], jointAxis = self.axes[linkname-1])
                linkname = linkname + 1
                j = j + 1   
        '''
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain/brain" + str(self.myID) + ".nndf")
        i = 0
        for i in range(len(self.sensors)):
            if self.sensors[i]:
                pyrosim.Send_Sensor_Neuron(name = i, linkName = str(i))
        j = 0
        i = i + 1
        for joint in self.joints:
            pyrosim.Send_Motor_Neuron(name = i, jointName = joint)
            split = joint.split('_')
            link0 = int(split[0])
            link1 = int(split[1])
            if self.sensors[link0]:
                pyrosim.Send_Synapse(sourceNeuronName = link0, targetNeuronName = i+self.numSensorNeurons, weight = self.weights[j])
            if self.sensors[link1]:
                pyrosim.Send_Synapse(sourceNeuronName = link1, targetNeuronName = i+self.numSensorNeurons, weight = self.weights[j])
            j = j + 1
            i = i + 1
        '''
        for motor in self.synapseDict:
            sensor = self.synapseDict[motor]
            pyrosim.Send_Synapse(sourceNeuronName = sensor, targetNeuronName = motor+self.numSensorNeurons, weight = self.weights[motor])
        '''
        pyrosim.End()