# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#  [Vehicle]-base class
class Vehicle:
    pass

#  [FlightVehicle] - child of vehicle
class FlightVehicle(Vehicle):
    pass

#  [Starship] - child of FlightVehicle
class Starship(FlightVehicle):
    pass

#  [Airplane] - child of FlightVehicle
class Airplane(FlightVehicle):
    pass

#  [GroundVehicle] - child of Vehicle  
class GroundVehicle(Vehicle):
    pass

#  [Car] - child of GroundVehicle
class Car(GroundVehicle):
    pass

#  [Motorcycle] - child of GroundVehicle
class Motorcycle(GroundVehicle):
    pass