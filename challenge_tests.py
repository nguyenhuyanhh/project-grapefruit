"""Testing for challenge.py."""

from unittest import TestCase, main

from challenge import Desert, State


class TestDesert(TestCase):
    """Test cases for class Desert."""

    def setUp(self):
        self.desert = Desert(n_target=5)

    def test_definition(self):
        """Test the definition of the instance."""
        self.assertEqual(self.desert.desert_fuel, {
            1: 0, 2: 0, 3: 0, 4: 0, 5: 0})

    def test_load_fuel_initial(self):
        """Test initial load fuel."""
        result = self.desert.load_fuel()
        self.assertEqual(result.truck_pos, 0)
        self.assertEqual(result.truck_fuel, 3)

    def test_drop_fuel_initial(self):
        """Test initial drop fuel."""
        result = self.desert.drop_fuel()
        self.assertEqual(result.truck_pos, 0)
        self.assertEqual(result.truck_fuel, 0)

    def test_move_right_initial(self):
        """Test initial move right."""
        result = self.desert.move_right()
        self.assertEqual(result.truck_pos, 0)
        self.assertEqual(result.truck_fuel, 0)

    def test_move_left_initial(self):
        """Test initial move left."""
        result = self.desert.move_right()
        self.assertEqual(result.truck_pos, 0)
        self.assertEqual(result.truck_fuel, 0)

    def test_move_right_3(self):
        """Test move 3 right."""
        result = self.desert.load_fuel()
        for _ in range(3):
            result = result.move_right()
        self.assertEqual(result.truck_pos, 3)
        self.assertEqual(result.truck_fuel, 0)

    def test_drop_at_pos_1(self):
        """Test dropping fuel at position 1."""
        result = self.desert.load_fuel().move_right().drop_fuel()
        self.assertEqual(result.truck_pos, 1)
        self.assertEqual(result.truck_fuel, 0)
        self.assertEqual(result.desert_fuel[1], 2)


class TestState(TestCase):
    """Test cases for class State."""

    def setUp(self):
        self.desert = Desert(5)
        self.state = State(self.desert)

    def test_next_states_initial(self):
        """Test the next states after the initial state."""
        right, left, load, drop = self.state.next_states()
        self.assertEqual(right.desert, self.desert)
        self.assertEqual(left.desert, self.desert)
        self.assertEqual(load.desert.truck_fuel, 3)
        self.assertEqual(drop.desert, self.desert)


if __name__ == '__main__':
    main()
