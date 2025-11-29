class sahil:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet (self):
        print("My name is : " + self.name)

obj = sahil("sahil yadav", 18)
obj.greet()
print(obj.age)
