class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"{self.name} {self.age}")

p = person("john", 25)

print(p)