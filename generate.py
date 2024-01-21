import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF('boxes.sdf')

for i in range(5):
    for j in range(5):
        length, width, height = 1, 1, 1
        x,y,z = i, j, 0.5
        for k in range(10):
            length *= 0.9
            width *= 0.9
            height *= 0.9            
            z += 1
            pyrosim.Send_Cube(name=f"Box", pos=[x,y,z] , size=[length,width,height])

pyrosim.End()