# Basic Form of a List

bikes = ['Trek', 'Redline', 'Cannondale', 'Specialized']
print(bikes)

# Access items in that list

print(bikes[1].title())

# Accessing the last item in that list

print(bikes[-1].title())

# Using Individual values from the list

message = f"My First bicycle was a {bikes[0].title()}."
print(message)

# Modify The List

bikes[0] = 'E-Bike'
print(bikes)

# Appending To End Of the list

bikes.append("Best Bike")
print(bikes)

# Empty List, Append

cars = []
cars.append("Hyundai")
cars.append("Toyota")
cars.append("Ferrari")
cars.append("Lambo")
print(cars)

# Inserting Items into a list

cars.insert(2, 'Audi')
print(cars)