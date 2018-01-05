"""Solution to the challenge."""

import sys
from collections import OrderedDict, deque, namedtuple
from time import time

MAX_FUEL = 3


class Desert:
    """Class to define the desert in the challenge."""

    def __init__(self, values):
        """Represent the desert as a list of n+2 values.

        values[:n]: fuel at each station
        values[-2]: fuel in truck
        values[-1]: truck position
        """
        self.values = values

    def __eq__(self, other):
        return self.values == other.values

    def __str__(self):
        _str = ','.join([str(i) for i in self.values])
        return _str

    def __hash__(self):
        return hash(str(self))

    def pretty_print(self):
        """Pretty-printed representation of the desert."""
        str_ = 'Fuel at stations: {}\nTruck at position {} with {} fuel'.format(
            self.values[:n_target], self.values[-1], self.values[-2])
        return str_

    def move_right(self):
        """Move the truck right, by one unit."""
        values = self.values[:]
        if values[-2] > 0:
            values[-1] += 1
            values[-2] -= 1
        return values

    def move_left(self):
        """Move the truck left, by one unit."""
        values = self.values[:]
        if values[-2] > 0 and values[-1] > 0:
            values[-1] -= 1
            values[-2] -= 1
        return values

    def load_fuel_base(self):
        """Load the truck with the max fuel allowed at base."""
        values = self.values[:]
        if values[-1] == 0:
            values[-2] = MAX_FUEL
        return values

    def load_fuel_1(self):
        """Load the truck with 1 unit of fuel at any other position."""
        values = self.values[:]
        cur_pos = values[-1] - 1
        if cur_pos >= 0 and values[-2] + 1 <= MAX_FUEL and values[cur_pos] >= 1:
            values[cur_pos] -= 1
            values[-2] += 1
        return values

    def load_fuel_2(self):
        """Load the truck with 2 units of fuel at any other position."""
        values = self.values[:]
        cur_pos = values[-1] - 1
        if cur_pos >= 0 and values[-2] + 2 <= MAX_FUEL and values[cur_pos] >= 2:
            values[cur_pos] -= 2
            values[-2] += 2
        return values

    def drop_fuel(self):
        """Drop the maximum amount of fuel from the truck."""
        values = self.values[:]
        if values[-1] > 0 and values[-2] > 0:
            cur_pos = values[-1] - 1
            max_allowed, values[-2] = values[-2], 0
            values[cur_pos] += max_allowed
        return values


class State:
    """Class to hold a state for the search problem."""

    def __init__(self, desert_values):
        self.desert = Desert(desert_values)

    def __eq__(self, other):
        return self.desert == other.desert

    def __str__(self):
        return str(self.desert)

    def __hash__(self):
        return hash(str(self))

    def pretty_print(self):
        """Pretty-printed representation of the state."""
        return self.desert.pretty_print()

    def move_right(self):
        """Move the truck right, by one unit."""
        result = self.desert.move_right()
        return State(result)

    def move_left(self):
        """Move the truck left, by one unit."""
        result = self.desert.move_left()
        return State(result)

    def load_fuel_base(self):
        """Load the truck with the maximum fuel allowed."""
        result = self.desert.load_fuel_base()
        return State(result)

    def load_fuel_1(self):
        """Load the truck with 1 unit of fuel at any other location."""
        result = self.desert.load_fuel_1()
        return State(result)

    def load_fuel_2(self):
        """Load the truck with 2 units of fuel at any other location."""
        result = self.desert.load_fuel_2()
        return State(result)

    def drop_fuel(self):
        """Drop the maximum amount of fuel from the truck."""
        result = self.desert.drop_fuel()
        return State(result)

    def next_states(self):
        """Return the next states for the search problem."""
        result = OrderedDict([('F', self.load_fuel_base()),
                              ('R', self.move_right()),
                              ('E', self.drop_fuel()),
                              ('1', self.load_fuel_1()),
                              ('L', self.move_left())])
        return result


def bfs(n_target):
    """Use BFS to search for the goal state."""

    def _goal_state(state):
        return str(state).split(',')[-1] == str(n_target)

    # named tuple to keep track of search positions
    search_pos = namedtuple('search_pos', ['cur_state', 'prev_state', 'path'])

    # initialize the search problem
    init_value = [0 for i in range(n_target)] + [0, 0]
    pos = search_pos(State(init_value), None, '')
    queue = deque([pos])
    explored = set()

    # search
    while queue:
        cur_pos = queue.popleft()
        cur_state = cur_pos.cur_state
        if _goal_state(cur_state):
            return cur_pos
        explored.add(cur_state)
        for key, next_state in cur_state.next_states().items():
            cur_path = cur_pos.path
            if next_state not in explored and next_state not in [x.cur_state for x in queue]:
                queue.append(search_pos(
                    next_state, cur_state, cur_path + key))


def interactive(init_state, sequence):
    """Interactive mode."""
    queue = deque(sequence)
    state = init_state

    while(queue):
        move = queue.popleft()
        state = state.next_states()[move]

    return state


if __name__ == '__main__':
    if len(sys.argv) == 2:
        n_target = int(sys.argv[1])
        start = time()
        res = bfs(n_target)
        print('Path: {}'.format(res.path))
        print('Time taken: {}'.format(time() - start))

    elif len(sys.argv) == 3:
        n_target = int(sys.argv[1])
        seq = sys.argv[2]
        init_values = [0 for i in range(n_target)] + [0, 0]
        print(interactive(State(init_values), seq).pretty_print())
