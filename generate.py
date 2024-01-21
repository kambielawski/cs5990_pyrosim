import pyrosim.pyrosim as pyrosim

def create_world():
    pyrosim.Start_SDF('world.sdf')

    length, width, height = 1, 1, 1
    x,y,z = -2, -2, 0.5
    pyrosim.Send_Cube(name=f"Box", pos=[x,y,z] , size=[length,width,height])

    pyrosim.End()

def create_robot():
    pyrosim.Start_URDF("body.urdf")

    length, width, height = 1, 1, 1
    x,y,z = 0, 0, 1.5
    pyrosim.Send_Cube(name=f"Torso", pos=[x,y,z] , size=[length,width,height])
    pyrosim.Send_Cube(name=f"BackLeg", pos=[0.5, 0, -0.5] , size=[length,width,height])
    pyrosim.Send_Cube(name=f"FrontLeg", pos=[-0.5, 0, -0.5] , size=[length,width,height])

    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [x+0.5,y,z-0.5])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [x-0.5,y,z-0.5])
    
    pyrosim.End()

create_world()
create_robot()