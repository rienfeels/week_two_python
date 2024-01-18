class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(f'{self.year} {self.make} {self.model}')

# Create a Vehicle object
car = Vehicle('Nissan', 'Leaf', 2015)

# Access individual attributes
print(car.make, car.model, car.year)

# Use the print_info method
car.print_info()
