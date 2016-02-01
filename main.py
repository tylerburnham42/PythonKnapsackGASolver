import random
import pprint
import copy
pp = pprint.PrettyPrinter(indent=4)

class Gene:
    """A Simple Class to Represent a Gene"""
    global dimensions
    choices = []
    size = 0 
    cost = 0
    def __init__(self, choices):
        self.Update_Choices(choices)
    def Update_Choices(self,choices):
        self.choices = choices
        self.size = self.Update_Size()
        self.cost = self.Update_Cost()
    def Add_Choice(self,choice):
        self.choices.append(choice)
        self.size = self.Update_Size()
        self.cost = self.Update_Cost()
    def Update_Size(self):
        return sum([float(options[choice][0]) for choice in  self.choices])
    def Update_Cost(self):
        return sum([float(options[choice][1]) for choice in  self.choices])  
    def Get_Size(self):
        return self.size
    def Get_Cost(self):
        return self.cost  
    def __lt__(self, other):
        if(dimensions == 2):
            if(self.Get_Size() == other.Get_Size()):
                return (self.cost) < (other.cost)
            else:
                return (self.size > other.size)
        else:
            return (self.size) > (other.size)
    def __repr__(self):
        if(dimensions == 2):
            return("Weight:" + str(self.size) + "Cost:" + str(self.cost) + ":" + str(self.choices))
        else:
            return("Weight:" + str(self.size) + ":" + str(self.choices))
            
    def Gene_Fill(self, options, knapsack_max):
        self.choices = []
        while(True):
            #Get a random choice from the choices list
            choice = random.choice(list(options.keys()))
            
            #Break if adding a new choice will go over
            if((options[choice][0]+self.size) > knapsack_max):
                break

            #Add to size
            self.size += float(options[choice][0])           
            
            #Add Choice
            self.choices.append(choice)
            
        #Update current cost
        self.cost = self.Update_Cost()
       
#Input the file name        
print("Input the file name")
file_name = input()
print(file_name)

#Open the file
file = open(file_name, 'r')
print("Fire0")
# Input the number of options for the knapsack (Integer)"
number_of_options = file.readline()


dimensions = 0
while(dimensions == 0):
    # "1 or 2 dimensional Problem?"
    print("Fire0")
    dimensions = int(file.readline())

#Create the dictionary of options and costs
options = {}

print("Fire")
#Populate the dictionary
#"Input options in the form of: Name Weight Cost"
for x in range(int(number_of_options)):
    line = file.readline().strip().split()
    if(dimensions == 2):
        options[line[0]] = (float(line[1]),float(line[2]))
    else:
        options[line[0]] = (float(line[1]), 0)

#Print options dictionary
#Options Format = {Name: (Weight, Cost)}
#print(options)

#Input Max sum of costs
print("Size of Knapsack (float)")
knapsack_max = float(file.readline())

#---Create Constants---
#Number of genes created for each generation
population_size = 20

#Number of selections made
generations = 10000

#%Chance of Mutation mutation/mutation_max
mutation = 10
crossover = 30
mutation_max = 100
#-----------------------

#Create a population
population = []
for x in range(population_size):
    gene = Gene([])
    gene.Gene_Fill(options, knapsack_max)
    #Add new Gene
    population.append(gene)

#Print Sorted starting Genes
population.sort()
pp.pprint(population)

average_weight = []
average_cost = []
max_weight = []
max_cost = []

print("---------------")
for generation in range(1,generations+1):
    #Get Pairents
    one = population[0]
    two = population[1]
    #Clear List
    population.clear()
    #Keep Best Parent
    population.append(one)
    while(len(population) < population_size):
        #Cross over 
        crossoverA = copy.deepcopy(one.choices)
        crossoverB = copy.deepcopy(gene.choices)[::-1]
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
        print("Generation:" + str(generation))
        print("Max Weight:" + str(population[0].Get_Size()))
        print("Max Cost:" + str(population[0].Get_Cost()))
    
    average_weight.append(sum([x.Get_Size() for x in population])/len(population))
    average_cost.append(sum([x.Get_Cost() for x in population])/len(population))
    
    max_weight.append(population[0].Get_Size())
    max_cost.append(population[0].Get_Cost())
    
pp.pprint(population)
    

    
