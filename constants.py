import numpy
import random


amplitude = numpy.pi/8
frequency = 10
offset = 0
numTimeSteps = 1000
numberOfGenerations = 2
populationSize = 1
height = numpy.random.randint(2,4)
length = numpy.random.randint(height,8)
numMotorNeurons = height-1 + 4*length
sensorNeuronsArray = []
numSensorNeurons = 0
for i in range(numMotorNeurons+1):
    if random.randint(0,1):
        sensorNeuronsArray = sensorNeuronsArray + [1]
        numSensorNeurons = numSensorNeurons + 1
    else:
        sensorNeuronsArray = sensorNeuronsArray + [0]
print("generated array")
print(sensorNeuronsArray)
motorJointRange = .2
