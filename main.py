organisms_start = int(input("Enter Starting Organisms: "))
population_increase = input("Enter Average Daily Increase: ")
increase_formatting = float(population_increase.strip('%'))
increase_percentage = float(increase_formatting / 100)
days_to_multiply = int(input("Enter Number of Days To Multiply: "))
starting_day = 1
# population for each day is equal to previous days population + previous days population * increase percentage
print("Approximate Day\t Population")
while starting_day < (days_to_multiply + 1):
    print(starting_day, '\t\t\t\t', organisms_start)
    starting_day = starting_day + 1
    organisms_start = organisms_start + (organisms_start * increase_percentage)
