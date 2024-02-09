import pybullet as p

class World:
    def __init__(self):
        # Set plane
        self.plane_id = p.loadURDF('plane.urdf')
        self.world_id = p.loadSDF('world.sdf')
        # self.robot_id = p.loadURDF('body.urdf')