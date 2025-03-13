class Animal(): #super class or  parent class 

    def __init__(self, name, type): 
        self.name = name 
        self.type = type 
        
    def display(self): 
        print(f"{self.name} is a {self.type}")
    



class Dog(Animal): # sub class or child class inheriting the instances and the methods from the super class or Animal class in this case 

    def sound(self): 
        print(f"Woof")



class Cat(Animal): # sub class or child class 
    def sound(self):
        print("meow")

        





bigBoy = Dog("boxy", "pet")
smallBaby = Cat("tom", "wild")
bigBoy.display()
bigBoy.sound()
smallBaby.display()
smallBaby.sound()

