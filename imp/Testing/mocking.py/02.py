from unittest.mock import Mock

def greet(person):
    return f" Hello {person.get_name()}"

p1= Mock() #object from Mock , this should return what we need using return_value

p1.get_name.return_value = "Ram"

print(greet(p1))