import pybullet as p
import pybullet_data
import constants as c
from world import WORLD
from robot import ROBOT
import time

class SIMULATION:
    def __init__(self,directOrGUI,solutionID):
        if directOrGUI == "DIRECT":
            physicsClient = p.connect(p.DIRECT)
        else:
            physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.directOrGUI = directOrGUI
        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def Run(self):
        for i in range(c.numTimeSteps):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.ACT()
            if self.directOrGUI == "GUI":
                time.sleep(1/600)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()


