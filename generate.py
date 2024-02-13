import pyrosim.pyrosim as pyrosim

def create_world():
    pyrosim.Start_SDF('world.sdf')

    length, width, height = 1, 1, 1
    x,y,z = -2, -2, 0.5
    pyrosim.Send_Cube(name=f"Box", pos=[x,y,z] , size=[length,width,height])

    pyrosim.End()

def generate_body():
    pyrosim.Start_URDF("body.urdf")

    length, width, height = 1, 1, 1
    x,y,z = 0, 0, 1.5
    pyrosim.Send_Cube(name=f"Torso", pos=[x,y,z] , size=[length,width,height])
    pyrosim.Send_Cube(name=f"BackLeg", pos=[0.5, 0, -0.5] , size=[length,width,height])
    pyrosim.Send_Cube(name=f"FrontLeg", pos=[-0.5, 0, -0.5] , size=[length,width,height])

    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [x+0.5,y,z-0.5])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [x-0.5,y,z-0.5])
    
    pyrosim.End()

def generate_brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")

    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

    pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 0.7 )
    pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 0.5 )
    pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 3 , weight = 0.3 )
    pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = -0.3 )
    pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = 0.1 )
    pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = 0.9 )

    pyrosim.End()



create_world()
generate_brain()
generate_body()