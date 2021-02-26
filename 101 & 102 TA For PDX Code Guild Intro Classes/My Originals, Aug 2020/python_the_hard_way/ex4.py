
cars = 100
space_in_a_car = 4

# This is the number of drivers
drivers = 30
passengers = 90

#This is the number of cars which are not driven, or sitting idly today, because we do not have enough drivers.
cars_not_driven = cars - drivers
cars_driven = drivers

carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "passengers to carpool today.")
print("We need to put", average_passengers_per_car, "in each car.")
