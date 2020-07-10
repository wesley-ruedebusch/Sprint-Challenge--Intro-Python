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

# Vehicle - base
class Vehicle:
    pass

# Flight vehicle - child of vehicle
class FlightVehicle(Vehicle):
    pass

# Stareship child of the flight vehicle
class Starship(FlightVehicle):
    pass

# Airplane child of FlightVehicle
class Airplane(FlightVehicle):
    pass

# GroundVehicle child of vehicle
class GroundVehicle(Vehicle):
    pass

# Car child of GroundVehicle
class Car(GroundVehicle):
    pass

# Motorcycle child of GroundVehicle
class Motorcycle(GroundVehicle):
    pass