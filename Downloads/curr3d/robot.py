import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c

class ROBOT:
    def __init__(self,solutionID,links):
        self.myID = solutionID
        self.motors = {}
        self.links = links
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robot)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain" + str(self.myID) + ".nndf")
        os.system("rm brain" + str(self.myID) + ".nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        i = 0
        print(pyrosim.linkNamesToIndices)
        for linkName in pyrosim.linkNamesToIndices:
            if c.sensorNeuronsArray[i]:
                self.sensors[linkName] = SENSOR(linkName)
            i = i + 1

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

    def Think(self):
        self.nn.Update()



