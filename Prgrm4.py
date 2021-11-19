#multi level
class Animal:
    def run(self):
        print("Animals run")
class Dog(Animal):
    def bark(self):
        print("dog barks")
class Puppy(Dog):
    def drink(self):
        print("puppy drinks milk")
p= Puppy()
p.drink()
p.bark()
p.run()


#mutiple inheritance
class ArithmeticOperation1:
    def Addition(self,i,j):
        return i+j
class ArithmeticOperation2:
    def Multiple(self,i,j):
        return i*j
class Derived(ArithmeticOperation1,ArithmeticOperation2):
    def Subtract(self,i,j):
        return i-j
d=Derived()
print(d.Addition(20,10))
print(d.Multiple(20,10))
print(d.Subtract(20,10))
