#Input will always read in a string but we can convert the values to int float boolean etc
#and we can also print out the type of the variable
birth_year = input('Birth year: \n')
age = 2023 - int(birth_year)
print(type(birth_year))
print(type(age))
print(age)