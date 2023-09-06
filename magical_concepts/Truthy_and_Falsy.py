# truthy and false in python
# Example 1: Using bool() function to check if a value is truthy or falsy
print(bool(0))  # False
print(bool(1))  # True
print(bool(""))  # False
print(bool(" "))  # True

# Example 2: Using truthy and falsy values in an if statement
x = ""
if x:
    print("Truthy")
else:
    print("Falsy")


# Output: Falsy

# Example 3: Using truthy and falsy values with user-defined classes
class MyClass:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return bool(self.value)


obj1 = MyClass(0)
obj2 = MyClass(1)

print(bool(obj1))  # False
print(bool(obj2))  # True
