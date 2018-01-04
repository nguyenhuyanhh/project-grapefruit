"""Solution to the challenge."""

MAX_FUEL = 3


class Desert:
    """Class to define the desert in the challenge."""

    def __init__(self, n_target):
        # desert's state
        self.target = n_target
        self.desert_fuel = {k: 0 for k in range(1, n_target + 1)}

        # truck's state
        self.truck_fuel = 0
        self.truck_pos = 0

    def __str__(self):
        _str = 'Fuel at positions: {}\nTruck is at position {} with {} fuel'.format(
            self.desert_fuel, self.truck_pos, self.truck_fuel)
        return _str

    def __eq__(self, other):
        return self.target == other.target and self.truck_pos == other.truck_pos

    def move_right(self):
        """Move the truck right, by one unit."""
        if self.truck_fuel > 0:
            self.truck_pos += 1
            self.truck_fuel -= 1
        return self

    def move_left(self):
        """Move the truck left, by one unit."""
        if self.truck_fuel > 0 and self.truck_pos > 0:
            self.truck_pos -= 1
            self.truck_fuel -= 1
        return self

    def load_fuel(self):
        """Load the truck with the maximum fuel allowed."""
        if self.truck_pos == 0:
            self.truck_fuel = MAX_FUEL
        else:
            cur_pos_fuel = self.desert_fuel[self.truck_pos]
            max_allowed = max(cur_pos_fuel, MAX_FUEL - self.truck_fuel)
            self.truck_fuel += max_allowed
            self.desert_fuel[self.truck_pos] -= max_allowed
        return self

    def drop_fuel(self):
        """Drop the maximum amount of fuel from the truck."""
        if self.truck_pos > 0 and self.truck_fuel > 0:
            max_allowed = self.truck_fuel
            self.truck_fuel = 0
            self.desert_fuel[self.truck_pos] += max_allowed
        return self


class State:
    """Class to hold a state for the search problem."""

    def __init__(self, init_desert):
        self.desert = init_desert

    def __str__(self):
        return str(self.desert)

    def __eq__(self, other):
        return self.desert == other.desert

    def _move_right(self):
        return State(self.desert.move_right())

    def _move_left(self):
        return State(self.desert.move_left())

    def _load_fuel(self):
        return State(self.desert.load_fuel())

    def _drop_fuel(self):
        return State(self.desert.drop_fuel())

    def next_states(self):
        """Return the next states for the search problem."""
        return [self._move_right(), self._move_left(), self._load_fuel(), self._drop_fuel()]


if __name__ == '__main__':
    pass
