import random
from dna import DNA

class Population():
    def __init__(self, size):
        self.size = size
        self.solutions = []
        self.populate()
        self.mating_pool = []
        self.max_fit = 0
        self.fit_avg = 0
        self.best = None
        self.first = random.choice(self.solutions)
        self.solved = False

    def populate(self):
        for i in range(self.size):
            self.solutions.append(DNA())

    def show(self):
        """
        Shows in the terminal the first solution, as well as five random solutions
        """

        print('************ FIRST **************')   
        self.first.show()
        print()

        print('POPULATION SIZE:', self.size)
        print('AVERAGE FITNESS:', self.fit_avg)
        print()

        print('************ RANDOM SOLUTIONS **************')   
        random.choice(self.solutions).show()
        print()

        for i in range(5):
            sol = random.choice(self.solutions)
            print('Hints completed:', sol.points, '\t \t Fitness', sol.fitness)
        print()

        print('************ BEST SOLUTION SO FAR**************')
        self.best.show()

    def calc_fitness(self):
        HINTS_TOTAL = 15

        self.max_fit = 0
        self.best = None
        self.fit_avg = 0

        for solution in self.solutions:
            solution.calc_fitness()
            
            if solution.fitness > self.max_fit:
                self.max_fit = solution.fitness
                self.best = solution
            
            if solution.points == HINTS_TOTAL:
                self.solved = True


        for solution in self.solutions: 
            solution.fitness /= self.max_fit  
            self.fit_avg += solution.fitness
        
        self.fit_avg /= len(self.solutions)
            
        
        self.mating_pool = []
        for solution in self.solutions:
            for i in range(int(solution.fitness*100)):
                self.mating_pool.append(solution)

    def selection(self, mutation_rate):
        new_solutions = []

        for i in range(self.size):
            parentA = random.choice(self.mating_pool)
            parentB = random.choice(self.mating_pool)  
            child = DNA()          
            genes = parentA.crossover(parentB)
            child.genes = genes
            child.mutate(mutation_rate)
            child.calc_fitness()
            new_solutions.append(child)

        self.solutions = new_solutions