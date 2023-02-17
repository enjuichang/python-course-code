import random 
from car import Car

class Street():
    def __init__(self, length):
        self.length = length
        # self.speed_limit = speed_limit
        self.street = [False for i in range(length)]

       
    
    def initialize_cars(self, speed):
        # initialize cars on the street
        # random.randint(0, self.length)
        self.street[0] = Car(speed=speed)

    def update(self):
        # Update the street
        new_setup = self.street

        for car in reversed(self.street):
            if car: # car = Car(1)
                if new_setup[car.position+car.speed] == False:
                    new_setup[car.position+car.speed] = car
                    new_setup[car.position] = False
                    car.position += car.speed
            else:
                pass

        self.street = new_setup


    def add_car(self, car):
        self.street[0] = Car(speed=1)

    def remove_car(self, car):
        self.street.remove(car)

    def _print(self):
        traffic_str = "".join([" * " if car else " - " for car in self.street])
        print("Our street: " + "| " + traffic_str + " |")

if __name__ == "__main__":
    street = Street(length=10)
    street.initialize_cars(speed=1)
    for i in range(5):
        street.update()
        print("---- iter " + str(i) + " ----")
        street._print()

