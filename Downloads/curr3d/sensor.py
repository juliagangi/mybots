import numpy
import pyrosim.pyrosim as pyrosim
import constants as c

class SENSOR:
    def __init__(self,linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.numTimeSteps)

    def Get_Value(self,t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Set_Value(self,t,val):
        self.values[t] = val

    def Save_Values(self):
        numpy.save("data/SensorValues", self.values, allow_pickle=True, fix_imports=True)
