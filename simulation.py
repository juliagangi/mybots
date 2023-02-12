import pybullet as p
import pybullet_data
import constants as c
from world import WORLD
from robot import ROBOT
import time


class SIMULATION:
    def __init__(self,solutionID,links):
        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def Run(self):
        for i in range(c.numTimeSteps):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.ACT()
            time.sleep(1/600)

    def __del__(self):
        p.disconnect()



