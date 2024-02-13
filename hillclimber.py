import copy
from solution import Solution

class HillClimber:
    def __init__(self, n_generations=100):
        self.n_generations = n_generations
        self.parent = Solution()
        self.parent.evaluate(0)

    def evolve(self):
        for i in range(self.n_generations):
            self.evolve_one_generation(i)
            print(f'Generation {i}')

    def evolve_one_generation(self, gen):
        self.spawn()
        self.mutate()
        self.child.evaluate(gen+1)
        self.select()

    def spawn(self):
        self.child = copy.deepcopy(self.parent)

    def mutate(self):
        self.child.mutate()

    def select(self):
        print(self.parent.fitness, self.child.fitness)
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child
