from population import Population
from dna import SOLUTION
import os


def main():

    REFRESH_RATE = 1
    POP_SIZE = 500
    MUTATION_RATE = 0.75

    population = Population(POP_SIZE)
    population.calc_fitness()
    population.show()
     
    cycle = 0
    while not population.solved:
        cycle+= 1

        population.selection(MUTATION_RATE)
        population.calc_fitness()         

        if cycle % REFRESH_RATE == 0:
            os.system('CLS')
            print('GENERATIONS', cycle)
            population.show()
            print()
            print("**************** ACTUAL SOLUTION ****************")
            for r in SOLUTION:    
                print(r)

if __name__ == '__main__':
    main()