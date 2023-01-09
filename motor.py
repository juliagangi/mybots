import pybullet as p
import numpy
import constants as c
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        if self.jointName == b'Torso_BackLeg':
            self.frequency = c.frequency
        else:
            self.frequency = c.frequency / 2
        self.offset = c.offset
        self.motors = {}
        motorVector = numpy.linspace(0,2*numpy.pi,100)
        self.motorValues = numpy.zeros(100)
        for i in range(100):
            self.motorValues[i] = self.amplitude * numpy.sin(self.frequency * motorVector[i] + self.offset)

    def Set_Value(self,robot,t):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robot,jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,targetPosition = MOTOR(self.jointName).motorValues[t],maxForce = 500)

    def Save_Values(self):
        numpy.save("data/MotorValues", self.motorValues, allow_pickle=True, fix_imports=True)
