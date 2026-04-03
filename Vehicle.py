class Vehicle:
    def __init__(self,bodystyle):
        self.bodystyle=bodystyle

    def drive(self,speed):
        self.mode="driving"
        self.speed=speed

class Car(Vehicle):
    def __init__(self,engineType):
        super().__init__("Car")
        self.wheels=4
        self.doors=4
        self.engine=engineType

    def drive(self,speed):
        super().drive(speed)
        print("Driving my",self.engine,"Car at",self.speed)

class MotorCycle(Vehicle):
    def __init__(self,engineType,hasSideCar):
        super().__init__("MotorCycle")
        self.doors=0
        self.engine=engineType
        if(hasSideCar):
            self.wheels=3
        else:
            self.wheels=2

    def drive(self,speed):
        super().drive(speed)
        print("Driving my",self.engine,"Bike at",self.speed)
    
car1=Car("gas")
car2=Car("electric")
bike1=MotorCycle("gas",True)

print(bike1.wheels)
print(car1.engine)
print(car2.doors)


car1.drive(30)
car2.drive(40)
bike1.drive(50)