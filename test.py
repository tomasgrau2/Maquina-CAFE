from platform import machine
import unittest
from main import CoffeMachine, NoCoinException, NoElementsException, NoSugarException

class CoffeM(unittest.TestCase):

    def test_initial(self):
        machine = CoffeMachine()
        self.assertEqual(machine.coins, 0)

    def test_insercoin(self):
        machine = CoffeMachine()
        machine.insert_coin()
        self.assertEqual(machine.coins, 1)

    def test_add_coffe(self):
        machine = CoffeMachine()
        machine.fill_machine_cafe()
        self.assertEqual(machine.coffee,30)

    def test_add_sugar(self):
        machine = CoffeMachine()
        machine.fill_machine_azucar()
        self.assertEqual(machine.sugar,15)

    def test_add_milk(self):
        machine = CoffeMachine()
        machine.fill_machine_milk()
        self.assertEqual(machine.milk,20)

    def test_no_coins(self):
        machine = CoffeMachine()
        with self.assertRaises(NoCoinException):
            machine.get_coffee()

    def test_get_coffe(self):
        machine = CoffeMachine()
        machine.insert_coin()
        machine.fill_machine_azucar()
        machine.fill_machine_cafe()
        machine.get_coffee()
        self.assertEqual(machine.coffee,0)
        self.assertEqual(machine.sugar,10)
        self.assertEqual(machine.coins,0)
    



if __name__ == '__main__':
    unittest.main()
        