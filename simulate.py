from simulation import Simulation
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Run simulation')
parser.add_argument('sim_type', type=str, default='GUI', help='Type of simulation to run (GUI or HEADLESS)')
args = parser.parse_args()

# Create simulation object
simulation = Simulation(args.sim_type)

simulation.run()
