#lin/app.py
#print("Hello world!")
#print("Hello sun!")
#print("Hello sky!")

#print("Hello world!", end = " ")
#print("Hello sun!", end="!! ")
#print("Hello sky!", end="!!!\n")

#path="lib/app.py"
#def test_app_py_exists():
    #assert(path.exists("lib/app.py"))

    #print("Hello world!")

print("Hello world!")
print("Hello sun!")
print("Hello sky!")

print("Hello world!", end=" ")
print("Hello sun!", end="!! ")
print("Hello sky!", end="!!!\n")

path = "lib/app.py"

def test_app_py_exists():
    assert path.exists(path)

    print("Hello world!")


test_app_py_exists()
