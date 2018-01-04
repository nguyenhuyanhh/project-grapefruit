"""Solution to the challenge."""


class Desert():
    """Class to define a challenge state."""

    def __init__(self, n_target=10):
        # desert's state
        self.target = n_target
        self.desert_fuel = {k: 0 for k in range(1, n_target + 1)}

        # truck's state
        self.truck_fuel = 0
        self.truck_max_fuel = 3
        self.truck_pos = 0

    def __str__(self):
        _str = 'Fuel at positions: {}\nTruck is at position {} with {} fuel'.format(
            self.desert_fuel, self.truck_pos, self.truck_fuel)
        return _str

    def move_right(self):
        """Move the truck right, by one unit."""
        self.truck_pos += 1
        self.truck_fuel -= 1

    def move_left(self):
        """Move the truck left, by one unit."""
        self.truck_pos -= 1
        self.truck_fuel -= 1

    def load_fuel(self, n_fuel):
        """Load the truck with fuel, by n_fuel units, until max capacity."""
        self.truck_fuel = min(self.truck_max_fuel, self.truck_fuel + n_fuel)

    def drop_fuel(self, n_fuel):
        """Drop fuel from the truck, by n_fuel units, until 0."""
        self.truck_fuel = max(0, self.truck_fuel - n_fuel)


if __name__ == '__main__':
    pass
