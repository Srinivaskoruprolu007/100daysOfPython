class Person:
    """A class that represents a human being with a name and an age."""

    def __init__(self, name: str, age: int) -> None:
        """Initialize a new instance with a name and an age."""
        self._name = name  # use _ prefix to indicate private attribute
        self._age = age

    @property
    def name(self) -> str:
        """Return or set the name attribute."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        # check if value is a valid string
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError("Name must be a string")

    @property
    def age(self) -> int:
        """Return or set the age attribute."""
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        # check if value is a valid integer
        if isinstance(value, int):
            self._age = value
        else:
            raise TypeError("Age must be an integer")

    def __repr__(self) -> str:
        """Return a string representation of the instance."""
        return f"Person(name={self.name!r}, age={self.age!r})"

    def __gt__(self, other) -> bool:
        """Return True if self is older than other, False otherwise."""
        return self.age > other.age

    def __lt__(self, other) -> bool:
        """Return True if self is younger than other, False otherwise."""
        return self.age < other.age

    def __add__(self, other) -> str:
        """Return a new string that combines both names with a space."""
        return self.name + " " + other.name


human = Person('Srinivas', 23)
print(human)

human1 = Person('Ganesh', 22)
human2 = Person('Surya', 25)
print(human2 + human1)
print(human1 > human2)
