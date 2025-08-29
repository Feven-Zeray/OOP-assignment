# ==========================================
# Assignment 1: Design Your Own Class
# ==========================================

# Superhero class example with inheritance and encapsulation
class Superhero:
    def _init_(self, name, superpower, health):
        self.name = name
        self.superpower = superpower
        self.__health = health  # private attribute

    def show_info(self):
        print(f"Hero: {self.name}")
        print(f"Superpower: {self.superpower}")
        print(f"Health: {self.__health}")

    def take_damage(self, damage):
        self.__health -= damage
        print(f"{self.name} took {damage} damage!")

    def get_health(self):
        return self.__health

class FlyingHero(Superhero):
    def _init_(self, name, superpower, health, flight_speed):
        super()._init_(name, superpower, health)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} km/h!")

# Objects for Assignment 1
hero1 = Superhero("Iron Fist", "Martial Arts", 100)
hero2 = FlyingHero("Skybolt", "Lightning", 120, 300)

hero1.show_info()
hero1.take_damage(20)
print(f"{hero1.name}'s Health: {hero1.get_health()}")

print("\n---Flying Hero---")
hero2.show_info()
hero2.fly()
hero2.take_damage(50)
print(f"{hero2.name}'s Health: {hero2.get_health()}")

# ==========================================
# Activity 2: Polymorphism Challenge
# ==========================================

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car is driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Plane is flying ✈")

class Boat(Vehicle):
    def move(self):
        print("Boat is sailing ⛴")

# Polymorphism demonstration
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()