class Jeanine:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def jeanineIntro(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


jean = Jeanine("Jeanine",16)
jean.jeanineIntro()