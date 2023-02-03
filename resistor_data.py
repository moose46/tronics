__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'

from models import ProductType


# from main import ProductType


#
# Author: Robert W. Curtiss
# resistor_data.py was created on January 31 2023 @ 2:52 PM
# Project: pythonTronics
#


def load_resistors(session):
    resistors = []
    carbon_resistor = ProductType(name='Resistor Carbon')
    resistors.append(carbon_resistor)
    film_resistor = ProductType(name='Resistor Film')
    resistors.append(film_resistor)
    metal_oxide_resistor = ProductType(name='Resistor Metal Oxide')
    resistors.append(metal_oxide_resistor)
    metal_film_resistor = ProductType(name='Resistor Metal Film')
    resistors.append(metal_film_resistor)
    wire_wound = ProductType(name="Resistor Wire Wound")
    resistors.append(wire_wound)
    cement_wire_wound = ProductType(name="Resistor Cement Wire Wound")
    resistors.append(cement_wire_wound)
    session.add_all(resistors)
    session.commit()
