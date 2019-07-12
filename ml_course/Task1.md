# Task1

Here is an ecological simulation of wolf and rabbit populations. Rabbits eat grass. Wolves eat rabbits. There is plenty of grass, so
wolves are the only obstacle to the rabbit population increase. The wolf population increases with the population of rabbits. 

The day by-day changes in the rabbit population R and the wolf population W can be expressed by the following formulae:

R(tomorrow) = (1 + a).R(today) - c.R(today).W(today)
W(tomorrow) = (1 - b).W(today) + c.d.R(today).W(today)

a = 0.01 = fractional increase in rabbit population without threat from
wolves ( 0.01 means 1 % increase)
b = 0.005 = fractional decrease in wolf population without rabbit to eat
c = 0.00001 = likelihood that a wolf will encounter and eat a rabbit
d = 0.01 = fractional increase in wolf population attributed to a devoured rabbit.

Assume that initially there are 10,000 rabbits and 1000 wolves. Write a program to calculate populations of rabbits and wolves over a
1000-day period. Have the program print the populations every 25 days. See what happens when you start with 500 wolves instead
of 1000. Try starting with 2000 wolves too.

Solution for the problem is [WolvesandRabbit.ipynb](https://github.com/Pranav-Khurana/TIL/blob/master/ml_course/ipynbfiles/WolvesandRabbit.ipynb) 
