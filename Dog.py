class Dog:
    
    animal = "dog"

    def __init__(self, name, age, breed, angerlevel):
        self.name = name
        self.age = age
        self.breed = breed
        self.angerlevel = angerlevel


jacky = Dog("Jacky", 4, "Pug", 3)
moly = Dog("Moly", 6, "Beagle", 4)
maxx = Dog("Maxx", 5, "Labrador", 7)
coco = Dog("Coco", 3, "Shih Tzu", 1)

print(f"Jacky's name is {jacky.name}, he is {jacky.age} years old, he is a {jacky.breed}, and his anger level is {jacky.angerlevel}")
print(f"Moly's name is {moly.name}, she is {moly.age} years old, she is a {moly.breed}, and her anger level is {moly.angerlevel}")
print(f"Maxx's name is {maxx.name}, he is {maxx.age} years old, he is a {maxx.breed}, and his anger level is {maxx.angerlevel}")
print(f"Coco's name is {coco.name}, he is {coco.age} years old, he is a {coco.breed}, and his anger level is {coco.angerlevel}")
