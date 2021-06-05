from hashlib import new
import random

HOUSE = [1, 2, 3, 4, 5]
COLOR = ['red', 'green', 'white', 'yellow', 'blue']
NATIONALITY = ['brit', 'swede', 'dane', 'norwegian', 'german']
DRINK = ['tea', 'coffee', 'milk', 'beer', 'water']
SMOKE = ['pall mall', 'dunhill', 'bluemaster', 'prince', 'blend']
PET = ['dogs', 'birds', 'cats', 'horses', 'fish']

# PERSON = [HOUSE, COLOR, NATIONALITY, DRINK, SMOKE, PET]

PEOPLE_AMT = 5
TRAITS_AMT = 6

KNOWN_FACTS = [
    ['brit', 'red'],
    ['swede', 'dogs'],
    ['dane', 'tea'],
    ['green', 'coffee'],
    ['pall mall', 'birds'],
    ['yellow', 'dunhill'],
    ['milk', 3],
    ['norwegian', 1],
    ['bluemaster', 'beer'],
    ['german', 'prince'],
]

NEIGHBOURS = [
    ['green', 'white', 'left'], # green to the left of the white house
    ['blend', 'cats', 'next'],
    ['horses', 'dunhill', 'next'],
    ['norwegian', 'blue', 'next'],
    ['blend', 'water', 'next'],
]

SOLUTION = [
    [1, 'yellow', 'norwegian', 'water', 'dunhill', 'cats'],
    [2, 'blue', 'dane', 'tea', 'blend', 'horses'],
    [3, 'red', 'brit', 'milk', 'pall mall', 'birds'],    
    [4, 'green', 'german', 'coffee', 'prince', 'fish'],    
    [5, 'white', 'swede', 'beer', 'bluemaster', 'dogs']
] 

def check_neighbours(sectionA, sectionB, position):
    score = 0
    if position == 'left':
        if sectionA[0] == sectionB[0] - 1:
            score += 1 
            # print(houseA, 'is on the left of', houseB)                         

    elif position == 'next':
        if (sectionA[0] == sectionB[0] - 1 or
            sectionA[0] == sectionB[0] + 1):
            score += 1
            # print(houseA, 'is next to', houseB)                         

    return score

class DNA:
    def __init__(self):
        self.genes = []
        self.populate()
        self.fitness = 0
        self.points = 0
    
    def populate(self):
        """
        Creates a list object with the genes, to fill the solution.
        """

        traits1 = HOUSE[:]
        traits2 = COLOR[:]
        traits3 = NATIONALITY[:]
        traits4 = DRINK[:]
        traits5 = SMOKE[:]
        traits6 = PET[:]
        all_traits = [traits1, traits2, traits3, traits4, traits5, traits6]

        for trait in all_traits:
            random.shuffle(trait)
        
        for bunch in all_traits:
            for item in bunch:
                self.genes.append(item) 

    def show(self):
        print('Hints completed:', self.points, '\t \t Fitness', self.fitness)
        for i in range(len(self.genes)):
            print(self.genes[i],  end='\t\t\t')
            if i in [4, 9, 14, 19, 24, 29]:
                print()

    def calc_fitness(self):
        people = []
        for i in range(PEOPLE_AMT):
            people.append([])
        
        for i in range(PEOPLE_AMT):
            for j in range(TRAITS_AMT):
                people[i].append(self.genes[i+(PEOPLE_AMT*j)])

        hint_points = 0        
        for gene in people:           
            for hint in KNOWN_FACTS:
                if hint[0] in gene and hint[1] in gene:
                    hint_points += 1

            for hint in NEIGHBOURS:
                houseA, houseB, position = hint
                if houseA in gene:
                    for other in people:
                        if houseB in other:
                            hint_points += check_neighbours(gene, other, position)
        
        self.fitness = hint_points ** hint_points
        self.points = hint_points

    def crossover(self, other):
        new_genes = []
        """
        It selects a random section of the dna to interchange with other dna object.
        """
        mid = random.choice([0, 5, 10, 15, 20, 25])
        for i in range(len(self.genes)):
            if i < mid:
                new_genes.append(self.genes[i])
            else:
                new_genes.append(other.genes[i])

        return new_genes

    def mutate(self, ratio):
        """
        According to the given ratio applies a small change in some gene, 
        by exchanging values of different indexes of the same section
        """
        r = random.random()
        if r < ratio:
            start = random.choice([0, 5, 10, 15, 20, 25])
            end = start + 5
            section_copy = self.genes[start:end]
            # random.shuffle(section_copy)
            i1 = random.randint(0, 4)
            i2 = random.randint(0, 4)
            section_copy[i1], section_copy[i2] = section_copy[i2], section_copy[i1]        
            self.genes[start:end] = section_copy
