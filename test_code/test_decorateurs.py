def name(func):
    def inner(*args, **kwargs):
        print(f"Running this method : {func.__name__}")
        return func(*args, **kwargs)

    return inner


class CoffeeMachine:
    water_level = 100

    @name
    def _start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("plus d'eau")
            return False

    @name
    def __boil_water(self):
        return "ebullition..."

    @name
    def make_coffee(self):
        if self._start_machine():
            self.water_level -= 20
            print(self.__boil_water())
            print("Le Café est prêt!")


machine: CoffeeMachine = CoffeeMachine()
for i in range(0, 5):
    machine.make_coffee()

machine.make_coffee() 
machine._start_machine()
machine._CoffeeMachine__boil_water()
"""
print(f"Faire un caffe: Public {machine.make_coffee()}")
print(f"demarrer Machine: Protected {machine._start_machine()}")
print(f"Faire un caffe: Private {machine._CoffeeMachine__boil_water()}")
"""
