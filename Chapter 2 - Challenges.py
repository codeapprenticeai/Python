# 1.  Personal Message - Use A Variable to print a person's name

# Code Apprentice's Attempt

name = "Toby"
print(f"Hi {name}, would you like to learn some python today?")

# ChatGPT Attempt (GPT3.5)

person_name = "Alice"

print("Hello, " + person_name + "!")

# ChatGPT Attempt (GPT4)

person_name = "Alice"
print(person_name)















# 2. Name Cases - print multiple names using uppercase,lowercase,titlecase

# Code Apprentice's Attempt

name = "Fred"
print(name.lower()) # Lower Case
print(name.upper()) # Upper Case
print(name.title()) # Title Case

# ChatGPT Attempt (GPT3.5) - Weird it using lists, for doing this task, but this is what it's done (All valid ways of doing this)

names = ["john", "jane", "alex"]

# Print names in uppercase
print("Uppercase names:")
for name in names:
    print(name.upper())

print()

# Print names in lowercase
print("Lowercase names:")
for name in names:
    print(name.lower())

print()

# Print names in titlecase
print("Titlecase names:")
for name in names:
    print(name.title())


# ChatGPT Attempt (GPT 4)

name1 = "Alice"
name2 = "Bob"
name3 = "charlie"

# Printing names in uppercase
print(name1.upper())
print(name2.upper())
print(name3.upper())

# Printing names in lowercase
print(name1.lower())
print(name2.lower())
print(name3.lower())

# Printing names in title case
print(name1.title())
print(name2.title())
print(name3.title())





#3 Famous Quotes - find a quote and print that quote using quotation marks

# Code Apprentice Attempt

quote = 'Albert Einstein once said "A person who never made a mistake never tried anything new."'
print(quote)


# ChatGPT (3.5 Attempt)

quote = "A person who never made a mistake never tried anything new. - Albert Einstein"
print(f'"{quote}"')


# ChatGPT (4 Attempt)
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')












# 4 Stripping Names - use a variable to represent a person's name, include some whitespace at the start and end and use the strip function to fix this and use a combination of \t \n

# Code Apprentice Attempt

firstname = "   Alex      "
print(firstname)

print(f"{firstname.lstrip()} \tThis is my left strip\n")
print(f"{firstname.rstrip()} \tThis is my right strip\n")
print(f"{firstname.strip()} \tThis is my full strip\n")


# ChatGPT (3.5 Attempt)

name = "\t  John Doe\n"

# Strip whitespace, tabs, and newline characters from the name
name_stripped = name.strip()

# Print the stripped name
print(f"Stripped name: '{name_stripped}'")


# ChatGPT (4 Attempt)

name_with_whitespace = "\t\n John Doe \n\t"
stripped_name = name_with_whitespace.strip()

print(f"Original name: '{name_with_whitespace}'")
print(f"Stripped name: '{stripped_name}'")
