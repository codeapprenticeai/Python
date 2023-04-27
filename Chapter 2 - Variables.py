"""
- Key Notes Regarding Variables -

1. Choose descriptive names: Variable names should be descriptive and convey the purpose or meaning of the data they store. For example, use 'age' or 'height' instead of generic names like 'x' or 'a'.

2. Follow naming conventions: In Python, it's common to use lowercase letters for variable names and separate words with underscores. This is known as the "snake_case" naming convention. For instance, use 'first_name' instead of 'firstName' or 'firstname'.

3. Begin with a letter or underscore: Variable names must start with a letter (a-z, A-Z) or an underscore (_). However, starting with an underscore is often used to indicate private or internal variables, so it's best to begin with a letter in most cases.

4. Avoid reserved words: Do not use Python's reserved words (keywords) as variable names, such as 'if', 'else', 'while', 'def', etc. These words have special meanings in Python, and using them as variable names will lead to errors.

5. Case sensitivity: Python variables are case-sensitive. This means that 'name', 'Name', and 'NAME' are considered distinct variables. Be consistent with your casing to avoid confusion.

6. No special characters: Variable names can only contain letters (a-z, A-Z), digits (0-9), and underscores (_). Special characters and spaces are not allowed.

7. Dynamic typing: Python is a dynamically-typed language, which means you don't need to declare the variable type explicitly. The type is inferred based on the value assigned to the variable. You can also change the type of a variable by assigning a new value of a different type.

8. Variable scope: Be aware of the variable's scope, which refers to the region of the code where the variable is accessible. Variables defined within a function have a local scope, while variables defined outside functions have a global scope. Accessing a variable outside its scope will result in an error.

"""

# Basic Variable Practice
message = "Hello Python World!"
print(message)

# Combining Variables

message = "Hello Python World Crash Course!"
print(message)

# Strings

print("this is a string")
print('This is also a string')
