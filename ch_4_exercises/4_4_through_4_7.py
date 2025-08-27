#  Make a list of the numbers 1 through 1 million
numbers = list(range(1, 1001))   # Do 1 million and 1 because range is exclusive for the second value
print(f"min value: {min(numbers)} max value: {max(numbers)}")
print(f"Sum of the list \"numbers\" = {sum(numbers)}")

# Start at 1 and add every other number (which will be odd numbers in this case)
odd_numbers = list(range(1, 20, 2)) 
print(f"Odd numbers: {odd_numbers}")

# Use list comprehension to make a list of the first 10 cubes
cubbed_numbers = [num**3 for num in range(1, 11)]
    # Put what you want the for loop to do first, then set up the for loop. Put all of this 
    # inside of the brackets when constucting the list, and each number produced will be saved in it
print(f"Cubbed numbers 1-10: {cubbed_numbers}")