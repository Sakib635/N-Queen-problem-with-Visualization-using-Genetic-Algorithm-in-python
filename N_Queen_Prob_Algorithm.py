import numpy as np
import random

#TASK-1 (calculates the fitness score of each of the individuals in the population)
def fitness(individual,num):
   Attacking_pair = 0
   Horizontal_attack = (num - len(np.unique(individual)))
   Attacking_pair += Horizontal_attack
   for n in range(num):
      for m in range(num):
         if ( n > m):
            i = abs(n-m)
            j = abs(individual[n] - individual[m])
            if(i == j):
               Attacking_pair += 1
   non_attacking_pairs=Goal_Fitness - Attacking_pair
   return non_attacking_pairs


#TASK-2 (returns one individual randomly )
def select_random(population):
    return random.choice(population)


#TASK-3 (Append first half of x with second half of y to create the child)
def crossover(x, y):
    return x[0:int(number_of_Queen/2)] + y[int(number_of_Queen/2):number_of_Queen]


#TASK-4 (mutates a random gene into another random gene)
def mutate(child):
    index = random.randint(0, len(child)-1)
    value = random.randint(1, len(child))
    child[index] = value
    return child


#TASK-5 (Genetic_Algorithm)
def Genetic_Algorithm(population, n, mutation_threshold ):
    updated_population = []   
    for i in range(len(population)):
        x = select_random(population)
        y = select_random(population)
        child = crossover(x, y)
        if random.random() < mutation_threshold:
            child = mutate(child)
        updated_population.append(child)
        if fitness(child,number_of_Queen) == Goal_Fitness:
             break
    return updated_population


#TASK-6 (N-Queen-Problem)
print("Welcome")
number_of_Queen=int(input("Tell the KING, how many Queens he has..."))
print()
print('Game Starts....')

Goal_Fitness=int((number_of_Queen*(number_of_Queen-1))/2)
start_population = 200
mutation_threshold = 0.3
population =[[random.randint(1,number_of_Queen) for i in range(number_of_Queen)] for i in range(start_population)]
num_of_iteration=0
Generation=1

print()

print("Queens are fighting to get safe positions, please wait.......")
while not Goal_Fitness in [fitness(individual,number_of_Queen) for individual in population]:
   if num_of_iteration<50000:
        population = Genetic_Algorithm(population, number_of_Queen, mutation_threshold)
        Generation += 1
        num_of_iteration += 1
   else:
       print("In Every position Queens Fight\nSo, No Queen is placed") 
       print()
       break

winner=[]

for individuals in population:
    if fitness(individuals,number_of_Queen) == Goal_Fitness:
        print("Reached Goal Fitness is->",fitness(individuals,number_of_Queen))
        print("After {} Generations Queens got their safe positions...".format(Generation-1))
        print()
        print("Safe Positions: ")
        print(individuals)
        winner=individuals
        print()


#Table Drawing
if len(winner)==number_of_Queen:
    print("###",number_of_Queen,"Queens Playing Table###")
    table = []
    for x in range(number_of_Queen):
        table.append(["[_]"] * number_of_Queen)
    for i in range(number_of_Queen):
        table[number_of_Queen-winner[i]][i]="[Q]"
    for breadth in table:
        print (" ".join(breadth))
    print()
print("--Game Over--")
