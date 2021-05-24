# # https://github.com/PdxCodeGuild/class_salmon/blob/main/1%20Python/labs/jackalope.md



population = [0, 0, ]  # target 1000
year = 0

def year_reproduce(population):

    reproductive_population = 0

    for individual in population:  # count the reproductive potential... 
        if 4 <= individual <= 8:
            reproductive_population += 1
    for i in population: # add one to each age.
        population[i] += 1
    
    # ... and add that # babies...
    for x in range (reproductive_population):
        population.append(0)

    return population

print(year_reproduce(population))

def die_at_age_10():
    for individual in population:
        if individual == 10:
            population.remove(10)
    print(population)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Mob Programming: Jackalope Simulator
# Version 1

# The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.

#     Jackalopes are reproductive from ages 4-8 and die at age 10.
#     Gestation is instantaneous. Each gestation produces two offspring.
#     Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do

# With these conditions in mind, we can represent our population as a list of ints.
# Version 2

# Now let's give the jackalopes distinct sexes and extend their gestation period to one year. We 
# can represent each jackalope with a dictionary, thus our population will be a list of dictionaries. 
# A jackalope will have the following properties:

#     name
#     age
#     sex
#     whether they're pregnant

# Jackalopes can only mate with those immediately around them. Every generation Jackalopes are 
# randomly shuffled.