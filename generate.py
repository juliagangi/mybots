import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

x = 3
for k in range(5):
    y = 3
    x = x - 1
    for j in range(5):
        length = 1
        width = 1
        height = 1
        base = 0
        z = .5
        y = y - 1
        for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
            length = length*.9
            width = width*.9
            height = height*.9
            base = base + height
            z = base + height/2


pyrosim.End()
