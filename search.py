import os

from hillclimber import HillClimber

hc = HillClimber(n_generations=20)

hc.evolve()
hc.parent.evaluate(0)