# Store The locations in a list
locations = ['Greece', 'Iceland', 'America', 'mexico', 'England', 'portugal']

# Print the above, don't worry about neat

print(locations)

# Use the sorted function

print(sorted(locations))

# show that the list is still in the original order

print(locations)

# using sorted, put in reverse alphabetical

print(sorted(locations,reverse=True))

# show that the list is still in it's original order

print(locations)

# use the reverse() to change the order of your list

locations.reverse()
print(locations)
# and reverse it back
locations.reverse()
print(locations)

# using sort() put everything in alphabetical

locations.sort(reverse=False)
print(locations)

locations.sort(reverse=True)
print(locations)