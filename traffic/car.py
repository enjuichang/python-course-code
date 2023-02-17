class Car():
    def __init__(self, speed=0, position=0):
        self.speed = speed
        self.position = position

    def accelerate(self, delta=1):
        self.speed += delta

    def decelerate(self, delta=1):
        self.speed -= delta

    def _print(self):
        print("Car is at position {} and moving at speed {}".format(self.position, self.speed))


if __name__ == "__main__":
    c = Car()
    c._print()
    c.accelerate(2)
    c._print()
    c.decelerate(5)
    c._print()