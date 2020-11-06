import random

#Hiding the hash

class Foo():
    def __hash__(self):
        return random.randint(1,1000)

f = Foo()

for i in range(10):
    print(hash(f))

dictionary = {f : 1}

print(f in dictionary) #False, it is hidden due to random hashing

for i in range(1000):
    if hash(f) == i:
        print("You can't fool me, the hash is: {}".format(i))
    else:
        pass

print(dictionary.keys()) #Here's the object lol