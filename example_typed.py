from rigidpython import typed

@typed
def foo(i: int) -> str:
    return str(i)


r = foo(2)
print(r)
r = foo("hi")
print(r)