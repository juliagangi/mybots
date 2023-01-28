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
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robot)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain" + str(self.myID) + ".nndf")
        os.system("rm brain" + str(self.myID) + ".nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
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
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        basePosition = basePositionAndOrientation[0]
        zPosition = basePosition[2]
        sensor1Vals = self.sensors["BackLowerLeg"].values
        sensor2Vals = self.sensors["FrontLowerLeg"].values
        sensor3Vals = self.sensors["LeftLowerLeg"].values
        sensor4Vals = self.sensors["RightLowerLeg"].values
        summedVals = sensor1Vals + sensor2Vals + sensor3Vals + sensor4Vals
        fitnessArray = []
        currStretch = 0
        for i in range(len(summedVals)):
            if summedVals[i] == -4:
                currStretch = currStretch + 1
            if summedVals[i] != -4:
                if currStretch != 0:
                    fitnessArray.append(currStretch) 
                currStretch = 0
        longestStretch = 0
        for i in range(len(fitnessArray)):
            curr = fitnessArray[i]
            if curr > longestStretch:
                longestStretch = curr
        fitnessFile = open("tmp" + str(self.myID) + ".txt", "w")
        os.system("mv tmp" + str(self.myID) + ".txt" " fitness" + str(self.myID) + ".txt")
        fitnessFile.write(str(longestStretch+zPosition))
        fitnessFile.close()

    def Think(self):
        self.nn.Update()



