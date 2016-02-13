from rigidpython import caseclass

@caseclass
def Cat(name: str, age: int):
    pass

mycat = Cat("terry", 4)
print(mycat)
print(mycat.name)
badcat = Cat(4, 4)
print(badcat)

