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


firstname = "The Apprentice"
lastname = "AI"

# This is known as a f-string, which you can use to print out multiple variables

print(f"My Name is {firstname} + {lastname}")


# Escape Sequences

"""
1. \n: The newline character represents a line break. It is used to create a new line within a string. When the string is printed or displayed, the text following the newline character will appear on a new line.
2. \t: The tab character represents a horizontal tab. It is used to insert a tab space within a string. This can be helpful for formatting output, such as creating indented or column-aligned text.

\\: Backslash (to insert a literal backslash in the string)
\": Double quote (to insert a literal double quote within a string enclosed by double quotes)
\': Single quote (to insert a literal single quote within a string enclosed by single quotes)

"""

text = "Hello, World!\nWelcome to Python!"
print(text)

print("Languages: \n\tPython\n\tC\n\tJavascript")


"""
The choice between rstrip, lstrip, and strip depends on your specific requirements. If you only need to remove whitespace from one side of the string (either the beginning or the end), you would use lstrip() or rstrip(). If you want to remove whitespace from both sides, you would use strip().
"""


"""
lstrip(): This method removes whitespace only from the beginning (left side) of a string. You might use lstrip() when you want to remove only the leading whitespace, but keep the trailing whitespace intact.
"""
text = "   Hello, World!   "
result = text.lstrip()
print(result)

"""
rstrip(): This method removes whitespace only from the end (right side) of a string. You might use rstrip() when you want to remove only the trailing whitespace, but keep the leading whitespace intact.
"""

text = "   Hello, World!   "
result = text.rstrip()
print(result)

"""
strip(): This method removes whitespace from both the beginning and the end of a string. If you want to get rid of all leading and trailing whitespace, strip() is the appropriate choice.
"""

text = "   Hello, World!   "
result = text.strip()
print(result)
