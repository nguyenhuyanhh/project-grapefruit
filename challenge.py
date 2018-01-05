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
        str_ = 'Fuel at stations: {}\nTruck at position {} with {} fuel'.format(
            self.values[:-2], self.values[-1], self.values[-2])
        return str_

    def __hash__(self):
        return hash(tuple(self.values))

    def move_right(self):
        """Move the truck right, by one unit."""
        values = self.values[:]
        if values[-2] > 0:
            values[-1] += 1
            values[-2] -= 1
        else:
            return None
        return Desert(values)

    def move_left(self):
        """Move the truck left, by one unit."""
        values = self.values[:]
        if values[-2] > 0 and values[-1] > 0:
            values[-1] -= 1
            values[-2] -= 1
        else:
            return None
        return Desert(values)

    def load_fuel_base(self):
        """Load the truck with the max fuel allowed at base."""
        values = self.values[:]
        if values[-1] == 0:
            values[-2] = MAX_FUEL
        else:
            return None
        return Desert(values)

    def load_fuel_1(self):
        """Load the truck with 1 unit of fuel at any other position."""
        values = self.values[:]
        cur_pos = values[-1] - 1
        if cur_pos >= 0 and values[-2] + 1 <= MAX_FUEL and MAX_FUEL >= values[cur_pos] >= 1:
            values[cur_pos] -= 1
            values[-2] += 1
        else:
            return None
        return Desert(values)

    def drop_fuel(self):
        """Drop the maximum amount of fuel from the truck."""
        values = self.values[:]
        if values[-1] > 0 and values[-2] > 0:
            cur_pos = values[-1] - 1
            max_allowed, values[-2] = values[-2], 0
            values[cur_pos] += max_allowed
        else:
            return None
        return Desert(values)

    def next_states(self):
        """Return the next states for the search problem."""
        result = OrderedDict()
        if self.load_fuel_base():
            result['F'] = self.load_fuel_base()
        if self.move_right():
            result['R'] = self.move_right()
        if self.drop_fuel():
            result['E'] = self.drop_fuel()
        if self.load_fuel_1():
            result['1'] = self.load_fuel_1()
        if self.move_left():
            result['L'] = self.move_left()
        return result, True if result else False


def bfs(target):
    """Use BFS to search for the goal state."""

    def _goal_state(state):
        return state.values[-1] == target

    # named tuple to keep track of search positions
    search_pos = namedtuple('search_pos', ['cur_state', 'prev_state', 'path'])

    # initialize the search problem
    init_value = [0 for i in range(target)] + [0, 0]
    pos = search_pos(Desert(init_value), None, '')
    queue, explored = deque([pos]), set()

    # search
    while queue:
        cur_pos = queue.popleft()
        cur_state = cur_pos.cur_state
        if _goal_state(cur_state):
            return cur_pos
        explored.add(cur_state)
        next_states, next_test = cur_state.next_states()
        if next_test:
            for key, next_state in next_states.items():
                cur_path = cur_pos.path
                if next_state != cur_state and next_state not in explored and \
                        next_state not in [x.cur_state for x in queue]:
                    queue.append(search_pos(
                        next_state, cur_state, cur_path + key))


def interactive(init_state, sequence):
    """Interactive mode, print out the state after applying a sequence of moves."""
    queue = deque(sequence)
    state = init_state
    while queue:
        move = queue.popleft()
        state = state.next_states()[0][move]
    return state


if __name__ == '__main__':
    if len(sys.argv) == 2:
        start = time()
        print('Path: {}'.format(bfs(int(sys.argv[1])).path))
        print('Time taken: {}'.format(time() - start))

    elif len(sys.argv) == 3:
        init_values = [0 for i in range(int(sys.argv[1]))] + [0, 0]
        print(interactive(Desert(init_values), sys.argv[2]))
