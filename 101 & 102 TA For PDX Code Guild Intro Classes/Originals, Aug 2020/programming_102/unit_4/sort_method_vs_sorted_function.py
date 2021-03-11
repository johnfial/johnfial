numbers = [5,2,8]

# .sort() doesn't return a sorted list
sorted_numbers = numbers.sort()
# print(sorted_numbers) # None

# .sort() operates directly on the list
numbers.sort()
# print(numbers)

# numbers = numbers.append(7) # append doesn't return anything either
# print(numbers) # None

numbers_sorted = sorted(numbers) # sorted() DOES return a sorted list
# print(numbers_sorted)
