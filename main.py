from logging import raiseExceptions
from operator import contains

class NoCoinException(Exception):
    pass

class NoElementsException(Exception):
    pass

class NoSugarException(Exception):
    pass


class CoffeMachine:
    def __init__(self):
        self.coins = 0
        self.sugar = 0
        self.coffee = 0
        self.milk = 0
        
    def insert_coin(self):
        self.coins += 1

    def fill_machine_cafe(self,):
        self.coffee += 30

    def fill_machine_azucar(self):
        self.sugar += 15

    def fill_machine_milk(self):
        self.milk += 20

    def get_coffee(self):
        if self.coins == 0:
            raise NoCoinException()
        self.coffee -= 30
        self.sugar -= 5
        self.coins -= 1
        return True







            
        
    

    


    