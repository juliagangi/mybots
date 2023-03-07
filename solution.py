import numpy
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self,nextAvailableID):
        #random.seed(nextAvailableID+1)
        self.myID = nextAvailableID
        self.fitnessArray = []
        self.dirs = [['-x',0],['+x',0],['-y',0],['+y',0]]
        dirarray = [0,1,2,3]
        self.numLinks = 1 
        self.numHiddenNeurons = 2        
        numarms = random.randint(1,4)
        for arm in range(numarms):
            i = random.randint(0,len(dirarray)-1)
            index = dirarray[i]
            numlinks = random.randint(1,5)
            self.dirs[index][1] = numlinks
            dirarray.remove(index)
            self.numLinks = self.numLinks + numlinks
        self.dims = []
        self.sensors = []
        self.numSensorNeurons = 0
        self.sweights = []
        for link in range(self.numLinks):
            for hneuron in range(self.numHiddenNeurons):
                self.sweights.append(random.random()*2-1)
            if random.randint(0,4) > 1:
                self.sensors.append(1)
                self.numSensorNeurons = self.numSensorNeurons + 1
            else:
                self.sensors.append(0)
            dims = [random.random(),random.random(),random.random()]
            if link == 0:
                dims=[.7,.7,.7]
            self.dims.append(dims)
        if self.numSensorNeurons == 0:
            self.numSensorNeurons = 1
            self.sensors[random.randint(0,len(self.sensors)-1)] = 1
        self.numJoints = self.numLinks - 1
        self.mweights = []
        self.axes = []       
        self.weights = []
        for motor in range(self.numJoints):
            self.weights.append(random.random()*2-1)
            for hneuron in range(self.numHiddenNeurons):
                self.mweights.append(random.random()*2-1)
            jointAxes = [random.randint(0,1), random.randint(0,1), random.randint(0,1)]  
            if sum(jointAxes) == 0:
                jointAxes[random.randint(0,2)] = 1
            axis = str(jointAxes[0]) + " " + str(jointAxes[1]) + " " + str(jointAxes[2])
            self.axes.append(axis)
 
    def Start_Simulation(self,directOrGUI,flag):
        self.Create_World()
        self.Create_Body() 
        self.Create_Brain(flag)
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")
        #os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &")

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness/fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        while True:
            f = open(fitnessFileName,"r")
            content = f.read()
            if content != "":
                self.fitness = float(content)
                f.close()
                break
            else:
                f.close()
        os.system("rm " + fitnessFileName)

    def Mutate(self,flag):
        rand = random.randint(0,6)
        if self.numLinks < 3:
            rand = random.randint(0,5)
        if flag == 'control':
            if rand == 0: # add sensor neuron
                print("here0")
                i = 0
                new_sensor = random.randint(0,self.numLinks - 1)
                while self.sensors[new_sensor] == 1:
                    new_sensor = random.randint(0,self.numLinks - 1)
                    i = i + 1
                    if i == 5:
                        break
                self.sensors[new_sensor] = 1
            if rand == 1: # remove sensor neuron
                print("here1")
                if self.numSensorNeurons == 1:
                    return
                i = 0
                curr_sensor = random.randint(0,self.numLinks - 1)
                while self.sensors[curr_sensor] == 0:
                    i = i + 1
                    if i == 5:
                        break
                    curr_sensor = random.randint(0,self.numLinks - 1)
                self.sensors[curr_sensor] = 0
            if rand == 2: # change link dimension
                print("here2")
                randlink = random.randint(1,self.numLinks - 1)
                randdim = random.randint(0,2)
                self.dims[randlink][randdim] = random.random()
            if rand == 3: # add link
                print("here3")
                randlink = random.randint(1,self.numLinks - 1)
                self.dims.insert(randlink,[random.random(),random.random(),random.random()])
                dir = random.randint(0,3)
                self.dirs[dir][1] = self.dirs[dir][1]+1
                if random.randint(0,4) > 1:
                    self.sensors.insert(randlink,1)
                    self.numSensorNeurons = self.numSensorNeurons + 1
                else:
                    self.sensors.insert(randlink,0)
                jointAxes = [random.randint(0,1), random.randint(0,1), random.randint(0,1)]  
                if sum(jointAxes) == 0:
                    jointAxes[random.randint(0,2)] = 1
                axis = str(jointAxes[0]) + " " + str(jointAxes[1]) + " " + str(jointAxes[2])
                self.axes.insert(randlink-1, axis)
                self.weights.insert(randlink-1,2*random.random()-1)
                self.numLinks = self.numLinks + 1
                self.numJoints = self.numJoints + 1             
            if rand == 4: # change random joint's weight
                motor = random.randint(0,self.numJoints - 1)
                self.weights[motor] = 2*random.random() - 1          
            if rand == 5: # change random joint axis
                motor = random.randint(0,self.numJoints - 1)
                jointAxes = [random.randint(0,1), random.randint(0,1), random.randint(0,1)]  
                if sum(jointAxes) == 0:
                    jointAxes[random.randint(0,2)] = 1
                axis = str(jointAxes[0]) + " " + str(jointAxes[1]) + " " + str(jointAxes[2])
                self.axes[motor] = axis
            if rand == 6: # remove link
                print("here6")
                randlink = random.randint(1,self.numLinks - 1)
                del self.dims[randlink]
                dir = random.randint(0,3)
                currnum = self.dirs[dir][1]
                i = 0
                while currnum == 0:
                    dir = random.randint(0,3)
                    currnum = self.dirs[dir][1]
                    i = i + 1
                self.dirs[dir][1] = self.dirs[dir][1]-1              
                if self.sensors[randlink]:
                    self.numSensorNeurons = self.numSensorNeurons - 1
                del self.sensors[randlink]
                del self.axes[randlink-1]
                del self.weights[randlink-1]
                self.numLinks = self.numLinks - 1
                self.numJoints = self.numJoints - 1 
        else:
            if self.numLinks < 3:
                rand = random.randint(0,5)
            if rand == 0: # add sensor neuron
                i = 0
                new_sensor = random.randint(0,self.numLinks - 1)
                while self.sensors[new_sensor] == 1:
                    new_sensor = random.randint(0,self.numLinks - 1)
                    i = i + 1
                    if i == 5:
                        break
                self.sensors[new_sensor] = 1
            if rand == 1: # remove sensor neuron
                if self.numSensorNeurons == 1:
                    return
                i = 0
                curr_sensor = random.randint(0,self.numLinks - 1)
                while self.sensors[curr_sensor] == 0:
                    i = i + 1
                    if i == 5:
                        break
                    curr_sensor = random.randint(0,self.numLinks - 1)
                self.sensors[curr_sensor] = 0
            if rand == 2: # change link dimension
                randlink = random.randint(1,self.numLinks - 1)
                randdim = random.randint(0,2)
                self.dims[randlink][randdim] = random.random()
            if rand == 3: # add link
                randlink = random.randint(1,self.numLinks - 1)
                self.dims.insert(randlink,[random.random(),random.random(),random.random()])
                dir = random.randint(0,3)
                self.dirs[dir][1] = self.dirs[dir][1]+1
                if random.randint(0,4) > 1:
                    self.sensors.insert(randlink,1)
                    self.numSensorNeurons = self.numSensorNeurons + 1
                else:
                    self.sensors.insert(randlink,0)
                jointAxes = [random.randint(0,1), random.randint(0,1), random.randint(0,1)]  
                if sum(jointAxes) == 0:
                    jointAxes[random.randint(0,2)] = 1
                axis = str(jointAxes[0]) + " " + str(jointAxes[1]) + " " + str(jointAxes[2])
                self.axes.insert(randlink-1, axis)
                for neuron in range(self.numHiddenNeurons):
                    self.sweights.insert(randlink+neuron,2*random.random()-1)
                    self.mweights.insert(randlink-1+neuron,2*random.random()-1)
                self.numLinks = self.numLinks + 1
                self.numJoints = self.numJoints + 1             
            if rand == 4: # change random joint's weight
                if random.randint(0,1):
                    motor = random.randint(0,self.numJoints - 1)
                    for neuron in range(self.numHiddenNeurons):
                        self.mweights[motor+neuron] = 2*random.random() - 1    
                else:
                    sensor = random.randint(0,self.numSensorNeurons - 1)
                    for neuron in range(self.numHiddenNeurons):
                        self.sweights[sensor+neuron] = 2*random.random() - 1        
            if rand == 5: # change random joint axis
                motor = random.randint(0,self.numJoints - 1)
                jointAxes = [random.randint(0,1), random.randint(0,1), random.randint(0,1)]  
                if sum(jointAxes) == 0:
                    jointAxes[random.randint(0,2)] = 1
                axis = str(jointAxes[0]) + " " + str(jointAxes[1]) + " " + str(jointAxes[2])
                self.axes[motor] = axis
            if rand == 6: # remove link
                randlink = random.randint(1,self.numLinks - 1)
                del self.dims[randlink]
                dir = random.randint(0,3)
                currnum = self.dirs[dir][1]
                i = 0
                while currnum == 0:
                    dir = random.randint(0,3)
                    currnum = self.dirs[dir][1]
                    i = i + 1
                self.dirs[dir][1] = self.dirs[dir][1]-1              
                if self.sensors[randlink]:
                    self.numSensorNeurons = self.numSensorNeurons - 1
                del self.sensors[randlink]
                del self.axes[randlink-1]
                for neuron in range(self.numHiddenNeurons):
                    del self.mweights[randlink-1+neuron]
                    del self.sweights[randlink+neuron]
                self.numLinks = self.numLinks - 1
                self.numJoints = self.numJoints - 1 

 
    def Set_ID(self,ID):
        self.myID = ID

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body/body" + str(self.myID) + ".urdf")
        self.joints = []
        linkname = 0
        zDim = self.dims[linkname][2]
        mycolor = "0 0 255 1"
        mycolorname = "Blue"
        if self.sensors[linkname]:
            mycolor = "0 128 0 1"
            mycolorname = "Green" 
        pyrosim.Send_Cube(name=str(linkname), pos=[0,0,.5*zDim], size=self.dims[0], color=mycolor, colorname=mycolorname)
        linkname = linkname + 1
        for dir in self.dirs:
            direction = dir[0]
            len = dir[1]
            for item in range(len):
                mycolor = "0 0 255 1"
                mycolorname = "Blue"
                if self.sensors[linkname]:
                        mycolor = "0 128 0 1"
                        mycolorname = "Green" 
                prevlink = linkname - 1
                if item == 0:
                    prevlink = 0
                if direction == '-x':
                    xPos = -.5*self.dims[linkname][0]
                    yPos = 0
                    zPos = .5*self.dims[linkname][2]
                    yJoint = 0
                    xJoint = -self.dims[prevlink][0]
                    zJoint = self.dims[prevlink][2]
                    if item == 0:
                        xJoint = -.5*self.dims[0][0]
                        zJoint = self.dims[0][2]
                if direction == '+x':
                    xPos = .5*self.dims[linkname][0]
                    yPos = 0
                    zPos = .5*self.dims[linkname][2]
                    yJoint = 0
                    xJoint = self.dims[prevlink][0]
                    zJoint = self.dims[prevlink][2]
                    if item == 0:
                        xJoint = .5*self.dims[0][0]
                        zJoint = self.dims[0][2]
                if direction == '-y':
                    xPos = 0
                    yPos = -.5*self.dims[linkname][1]
                    zPos = .5*self.dims[linkname][2]
                    xJoint = 0
                    yJoint = -self.dims[prevlink][1]
                    zJoint = self.dims[prevlink][2]
                    if item == 0:
                        yJoint = -.5*self.dims[0][0]
                        zJoint = self.dims[0][2]
                if direction == '+y':
                    xPos = 0
                    yPos = .5*self.dims[linkname][1]
                    zPos = .5*self.dims[linkname][2]
                    xJoint = 0
                    yJoint = self.dims[prevlink][1]
                    zJoint = self.dims[prevlink][2]
                    if item == 0:
                        yJoint = .5*self.dims[0][0]
                        zJoint = self.dims[0][2]
                jointname = str(prevlink)+"_"+str(linkname)
                pyrosim.Send_Cube(name= str(linkname), pos=[xPos,yPos,zPos], size=self.dims[linkname], color=mycolor, colorname=mycolorname)
                pyrosim.Send_Joint(name = jointname, parent=str(prevlink), child = str(linkname), type = "revolute", position = [xJoint,yJoint,zJoint], jointAxis = self.axes[linkname-1])
                self.joints.append(jointname)
                linkname = linkname + 1
        pyrosim.End()

    def Create_Brain(self,flag):
        pyrosim.Start_NeuralNetwork("brain/brain" + str(self.myID) + ".nndf")
        i = 0
        for i in range(len(self.sensors)):
            if self.sensors[i]:
                pyrosim.Send_Sensor_Neuron(name = i, linkName = str(i))
        j = 0
        i = i + 1
        if flag == 'control':
            for joint in self.joints:
                pyrosim.Send_Motor_Neuron(name = i, jointName = joint)
                split = joint.split('_')
                link0 = int(split[0])
                link1 = int(split[1])
                if self.sensors[link0]:
                    pyrosim.Send_Synapse(sourceNeuronName = link0, targetNeuronName = i, weight = self.weights[j])
                if self.sensors[link1]:
                    pyrosim.Send_Synapse(sourceNeuronName = link1, targetNeuronName = i, weight = self.weights[j])
                j = j + 1
                i = i + 1
        else:
            hidden = i
            for neuron in range(self.numHiddenNeurons):
                pyrosim.Send_Hidden_Neuron(name = i)
                i = i + 1
            for sensor in range(len(self.sensors)):
                if self.sensors[sensor]:
                    for neuron in range(self.numHiddenNeurons):
                        pyrosim.Send_Synapse(sourceNeuronName = sensor, targetNeuronName = hidden+neuron, weight = self.sweights[sensor+neuron])
            for joint in range(len(self.joints)):
                pyrosim.Send_Motor_Neuron(name = i, jointName = self.joints[joint])
                for neuron in range(self.numHiddenNeurons):
                    pyrosim.Send_Synapse(sourceNeuronName = hidden+neuron, targetNeuronName = i, weight = self.mweights[joint+neuron])
                i = i + 1
        pyrosim.End()