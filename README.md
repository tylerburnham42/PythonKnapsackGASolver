# Python Knapsack Genetic Alogorithm Solver
This is a simple python script to solve knapsack problems with a genetic algorithm.

This is currently setup to solve change making problems but can be easily adapted by changing the fitness function. The program uses standard inputs.

|Inputs|
|------|
|The (N) first input is the number of items |
|The seccond is if the program is in one or two dimensional mode. |
|The next (N) inputs are the options in the form of "Name weight cost" |
|The last is the max weight for the knapsack.  |

A test case is based off the XKCD comic https://xkcd.com/287/   
**Input**
```
6
2
MixedFruit 2.15 1
FrenchFries 2.75 1
SideSalad 3.35 1
HotWings 3.55 1
MozzarellaSticks 4.20 1
SamplerPlate 5.80 1
15.05
```

**Output**
```
Generation:20000
Weight:15.05 Cost:4.0 ['HotWings', 'SamplerPlate', 'MixedFruit', 'HotWings']
```
