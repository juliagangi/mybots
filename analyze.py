import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
print(backLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues, label='Back leg', linewidth=3)

frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
print(frontLegSensorValues)
matplotlib.pyplot.plot(frontLegSensorValues, label='Front leg', linewidth=2)

matplotlib.pyplot.legend()
matplotlib.pyplot.show()

