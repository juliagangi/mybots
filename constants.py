import numpy
import random

amplitude = numpy.pi/8
frequency = 10
offset = 0
numTimeSteps = 10000
numberOfGenerations = 2
populationSize = 1
height = 2
length = random.randint(height+2,7)
numMotorNeurons = height-1 + 4*length
sensorNeuronsArray = []
numSensorNeurons = 0
for i in range(numMotorNeurons+1):
    if random.randint(0,4) > 1:
        sensorNeuronsArray = sensorNeuronsArray + [1]
        numSensorNeurons = numSensorNeurons + 1
    else:
        sensorNeuronsArray = sensorNeuronsArray + [0]
motorJointRange = .3
