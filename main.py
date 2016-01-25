import random
import pprint
import copy
pp = pprint.PrettyPrinter(indent=4)

class Gene:
    """A Simple Class to Represent a Gene"""
    global demsions
    choices = []
    def __init__(self):
        self.choices = []
    def __init__(self, choices):
        self.choices = choices
    def Get_Size(self):
        return sum([float(options[choice][0]) for choice in  self.choices])
    def Get_Cost(self):
        return sum([float(options[choice][1]) for choice in  self.choices])  
    def __lt__(self, other):
        if(dimensions == 2):
            if(self.Get_Size() == other.Get_Size()):
                return (self.Get_Cost()) < (other.Get_Cost())
            else:
                return (self.Get_Size() > other.Get_Size())
        else:
            return (self.Get_Size()) > (other.Get_Size())
    def __repr__(self):
        #if(dimensions == 2):
        return("Weight:" + str(self.Get_Size()) + "Cost:" + str(self.Get_Cost()) + ":" + str(self.choices))
        #else:
            #return("Weight:" + str(self.Get_Size()) + str(self.choices))

print("Input the number of options for the knapsack (Integer)")
number_of_options = input()


dimensions = 0
while(dimensions == 0):
    print("1 or 2 dimensional Problem?")
    dimensions = int(input())


#Create the dictionary of options and costs
options = {}

print("Input options in the form of:")
print("\tName Weight Cost")
#Populate the dictionary
for x in range(int(number_of_options)):
    line = input().strip().split()
    if(dimensions == 2):
        options[line[0]] = (float(line[1]),float(line[2]))
    else:
        options[line[0]] = (float(line[1]), 0)

#Print options dictionary
#Options Format = {Name: (Weight, Cost)}
#print(options)

#Input Max sum of costs
print("Size of Knapsack (float)")
knapsack_max = float(input())

#Create Constants
population_size = 10
generations = 10000
mutation = 10
mutation_max = 50

#Create a population
population = []
for x in range(population_size):
    gene = Gene([])
    while(True):
        #Get a rondom choice from the choices list
        choice = random.choice(list(options.keys()))
        
        #Break if adding a new choice will go over
        if((options[choice][0]+gene.Get_Size()) > knapsack_max):
            break

        #Add the new choice or increment the count
        gene.choices.append(choice)


    #Add new Gene
    population.append(gene)

    

#Print Sorted starting Genes
population.sort()
pp.pprint(population)

print("---------------")
for generation in range(1,generations+1):
    if(generation%1000 ==0):
        print("Generation:" + str(generation))
    #Get Pairents
    one = population[0]
    two = population[1]
    #print(one)
    #print(two)
    #Clear List
    population.clear()
    #Keep Best Parent
    population.append(one)
    while(len(population) < population_size):
        crossoverA = copy.deepcopy(one.choices)
        crossoverB = copy.deepcopy(two.choices)[::-1]
        #print(crossover)
        #print(one)
        #print(two)
        maxlength = min([len(crossoverA), len(crossoverB)])
        limits = sorted([random.randint(0, maxlength) for k in range(2)])
        crossoverA[limits[0]:limits[1]] = crossoverB[limits[0]:limits[1]]
        while(random.randint(0, mutation_max) <= mutation):
            #If it is 0 length add an element
            if(len(crossoverA) <= 0):
                crossoverA.append(random.choice(list(options.keys())))
                continue
            
            selection = random.randint(0, 4)
            #print("Mutation! " + str(selection))
            if(selection == 0):
                #Addition
                crossoverA.insert(random.randint(0, len(crossoverA)-1), random.choice(list(options.keys())))
            if(selection == 1):
                #Subtraction
                crossoverA.pop(random.randint(0, len(crossoverA)-1))
            if(selection == 2):
                #Substution
                crossoverA[random.randint(0, len(crossoverA)-1)] = random.choice(list(options.keys()))
            if(selection == 3):
                #Swap
                if(len(crossoverA)>=2):
                    rand = random.randint(0, len(crossoverA)-2)
                    temp_list = crossoverA[rand:rand+1]
                    crossoverA[rand:rand+1] = temp_list[::-1]
            if(selection == 4):
                #Invert Entire List
                crossoverA = crossoverA[::-1]

        #If the gene is too heavy skip the gene       
        new_gene = Gene(crossoverA)
        if(new_gene.Get_Size() > knapsack_max):
            continue
        #Add the gene to the current population
        population.append(Gene(crossoverA))

    population.sort()
    if(generation%1000 ==0):
        pp.pprint(population)
        #print("-------------------")
    

    

    
