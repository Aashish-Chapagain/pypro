class Animal(): #grand parent 
    def __init__(self,name):
       self.name = name 

    def eat(self): 
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")



class Herbivore(Animal): 
    
    def feed(self):
     print(f"{self.name}  eats plant.")
    
class Carnivore(Animal):
   
   def prey(self):
      print(f"{self.name}  eats flesh.")     
    
class Omnivores(Herbivore, Carnivore):  #multiple inheritance
   
   def allrounder(self): 
      print(f"So {self.name} is all rounder.")



print("\n")

lion = Carnivore("lion")
lion.sleep()
lion.eat()
lion.prey()

print("\n")

men = Omnivores("Human")
men.eat()
men.sleep()
men.feed()
men.prey() 
men.allrounder()