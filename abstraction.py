from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass
class BMW(Car):
    def mileage(self):
        print("i go 45 kmph")
class Audi(Car):
    def mileage(self):
        print("i go 50kmph")
# ob=BMW()
# ob.mileage()                   
     #or
BMW().mileage()     
