import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import matplotlib.pylab as plt


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

amplitudeF = numpy.pi/14
frequencyF = 30
phaseOffsetF = 0
motorVectorF = numpy.linspace(0,2*numpy.pi,1000)
targetAnglesF = numpy.zeros(1000)

amplitudeB = numpy.pi/10
frequencyB = 30
phaseOffsetB = -numpy.pi/6
motorVectorB = numpy.linspace(0,2*numpy.pi,1000)
targetAnglesB = numpy.zeros(1000)

for i in range(1000):
    targetAnglesF[i] = amplitudeF * numpy.sin(frequencyF * motorVectorF[i] + phaseOffsetF)
    targetAnglesB[i] = amplitudeB * numpy.sin(frequencyB * motorVectorB[i] + phaseOffsetB)

numpy.save("back",targetAnglesB)
numpy.save("front",targetAnglesF)

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = b'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,targetPosition = targetAnglesB[i],maxForce = 500)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = b'Torso_FrontLeg',
            controlMode = p.POSITION_CONTROL,targetPosition = targetAnglesF[i],maxForce = 500)
    time.sleep(1/480)
p.disconnect()

numpy.save("data/backLegSensorValues", backLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save("data/frontLegSensorValues", frontLegSensorValues, allow_pickle=True, fix_imports=True)
