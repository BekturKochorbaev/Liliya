class Computer:
    def __init__(self, ram, storage, cpu, price):
        self.ram = ram
        self.storage = storage
        self.cpu = cpu
        self.price = price

    def show(self):
        return f'{self.ram}, {self.storage}, {self.cpu}, {self.price}'

computer1 = Computer(8, 512, 'Intel', 45000)
print(computer1.show())  # 8, 512, 'Intel', 45000

class Laptop:
    def __init__(self, ram, storage, cpu, price, size):
        self.ram = ram
        self.storage = storage
        self.cpu = cpu
        self.price = price
        self.size = size
    def show(self):
        return f'{self.ram}, {self.storage}, {self.cpu}, {self.price}, {self.size}'

laptop1 = Laptop(8, 512, 'Ryzen', 45000, 17)
print(laptop1.show())  # 8, 512, 'Ryzen', 45000, 17

