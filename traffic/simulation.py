from traffic.traffic import Street
from traffic.car import Car
import random

timesteps = 10

my_street = Street(100, 10)

for i in range(timesteps):

    my_street.update()
    

