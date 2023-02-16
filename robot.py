import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c
import numpy

class ROBOT:
    def __init__(self,solutionID):
        self.myID = solutionID
        self.motors = {}
        self.robot = p.loadURDF("body/body" + str(self.myID) + ".urdf")
        pyrosim.Prepare_To_Simulate(self.robot)
        self.nn = NEURAL_NETWORK("brain/brain" + str(self.myID) + ".nndf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system("rm brain/brain" + str(self.myID) + ".nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        neurons = self.nn.Get_Sensor_Neurons()
        for neuron in neurons:
            linkName = neuron.Get_Link_Name()
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self,t):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def ACT(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)*c.motorJointRange
                self.motors[jointName].Set_Value(self.robot,desiredAngle)
                
    def Get_Fitness(self):
        # if fitness file doesn't exist, write position to it
        # if fitness file does exist, read from it
        # write back displacement to it
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        yPosition = basePosition[1]
        zPosition = basePosition[2]
        zDisp = zPosition - c.height
        dist = numpy.sqrt(xPosition*xPosition + yPosition*yPosition)
        fitnessFile = open("tmp" + str(self.myID) + ".txt", "w")
        os.system("mv tmp" + str(self.myID) + ".txt" " fitness/fitness" + str(self.myID) + ".txt")
        fitnessFile.write(str(dist - zDisp))
        fitnessFile.close()

    def Think(self):
        self.nn.Update()



