# ćwiczenia

class House:
    color: str
    window_count: int

    def __init__(self, color: str, window_count: int) -> None:
        self.color = color
        self.window_count = window_count

    def get_color(self) -> str:
        return f'elewacja budynku jest koloru: {self.color}'

    def add_windows(self, amount: int) -> None:
        self.window_count += amount

    def __private_method(self) -> None:
        print('ebe')


house1 = House('blue', 10)
house2 = House('orange', 8)

print(f'Dom nr 1 ma {house1.window_count} okien.')
print(f'Dom nr 2 ma {house2.window_count} okien.')

house2.add_windows(5)

print(f'Dom nr 1 ma {house1.window_count} okien.')
print(f'Dom nr 2 ma {house2.window_count} okien.')

print(house1.get_color())
print(house2.get_color())

house1.color = 'black'

print(house1.get_color())
print(house2.get_color())

# 1)

