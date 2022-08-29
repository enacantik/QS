class Person():
    def __init__(self, name) :
        self.name = name
    def say_hay(self) :
        print("Hello, my name is", self.name)

p = Person("Hendi")
p.say_hay()



