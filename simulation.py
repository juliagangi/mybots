import pybullet as p
import pybullet_data
import constants as c
from world import WORLD
from robot import ROBOT
import time


class SIMULATION:
    def __init__(self):
        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for i in range(100):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.ACT(i)
            time.sleep(1/20)

    def __del__(self):
        p.disconnect()



