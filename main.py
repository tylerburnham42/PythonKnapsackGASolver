import random
import pprint
pp = pprint.PrettyPrinter(indent=4)

class Gene:
    """A Simple Class to Represent a Gene"""
    choices = {}
    def __init__(self):
        self.choices = {}
    def Get_Size(self):
        return sum([float(options[choice][0])*self.choices[choice] for choice in  self.choices.keys()])
    def Get_Cost(self):
        return sum([float(options[choice][1])*self.choices[choice] for choice in  self.choices.keys()])
    def __lt__(self, other):
        if(self.Get_Cost() == other.Get_Cost()):
            return (self.Get_Size()) < (other.Get_Size())
        else:
            return (self.Get_Cost() > other.Get_Cost())
    def __repr__(self):
        return("Size:" + str(self.Get_Size()) + "Cost:" + str(self.Get_Cost()) + ":" + str(self.choices))

print("Input the number of options for the knapsack (Integer)")
number_of_options = input()

#Create the dictionary of options and costs
options = {}

print("Input options in the form of:")
print("\tName Weight Cost")
#Populate the dictionary
for x in range(int(number_of_options)):
    line = input().strip().split()
    options[line[0]] = (float(line[1]),float(line[2]))

#Print options dictionary
#Options Format = {Name: (Weight, Cost)}
#print(options)

#Input Max sum of costs
print("Size of Knapsack (float)")
knapsack_max = float(input())

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
        if((options[choice][0]+gene.Get_Size()) > knapsack_max):
            break

        #Add the new choice or increment the count
        if choice in gene.choices.keys():
            gene.choices[choice] += 1
        else:
            gene.choices[choice] = 1

    #Add new Gene
    population.append(gene)

    

#Print Sorted starting Genes
population.sort()
pp.pprint(population)


