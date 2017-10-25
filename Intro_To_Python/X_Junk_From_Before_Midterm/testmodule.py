# testmodule.py
print('The test module has started')

print("__name__ is", __name__)

if __name__ == "__main__":
# called from itself
    print("I am the main program.")
else:
# (Called from the Shell)
    print("Another module is importing me.")


