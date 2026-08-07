class Person:
    def get_name(self):
        return "Mr.X"


p1= Person()
def greet(person):
    return(f" Hello { person.get_name()}")

print(greet(p1))

# Mocking is the testing technique using fake objects from mock not the objects we create. 
