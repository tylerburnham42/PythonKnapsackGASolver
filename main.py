import random
import pprint
pp = pprint.PrettyPrinter(indent=4)

class Gene:
    """A Simple Class to Represent a Gene"""
    currentSize = 0
    choices = []
    def __init__(self):
        self.currentSize = 0
        self.choices = []
    def updateSize(self):
        self.currentSize = 0
        for choice in self.choices:
            self.currentSize += choice[1]
    def __repr__(self):
        return("Size: " + str(self.currentSize) + ":" + str(self.choices))

print("Input the number of options for the knapsack (Integer)")
number_of_options = input()

#Create the dictionary of options and costs
options = {}

print("Input options in the form of:")
print("\tName Cost")
#Populate the dictionary
for x in range(int(number_of_options)):
    line = input().strip().split()
    options[line[0]] = float(line[1])

#Print options dictionary
print(options)
print(options.keys())

#Input Max sum of costs
print("Size of Knapsack (float)")
knapsack_max = int(input())

#Create Constants
population_size = 10


#Create a population
population = []
for x in range(population_size):
    gene = Gene()
    while(True):
        #Get a rondom choice from the choices list
        choice = random.choice(list(options.keys()))
        
        #Break if adding a new choice will go over
        if((options[choice]+gene.currentSize) > knapsack_max):
            break

        #Add the new choice and update the size count
        gene.choices.append((choice,options[choice]))
        gene.updateSize()

    #Add new Gene
    population.append(gene)

    
#Print Starting Genes  
pp.pprint(population)


