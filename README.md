# project-grapefruit

This is a technical challenge for Graymatics.

## Challenge Statement

A truck has to travel across a desert from the base camp at position 0 (left) to the target camp at position n (right). The intermediate positions 1, 2, and 3 are desert camps, and have at the beginning of the process no fuel. The truck is able to take 3 units of fuel with it. Each move 1 field to the right (towards the target camp) or 1 field to the left (towards the base camp) uses up 1 unit of fuel. If not all fuel is used up in a move, and the move has not reached the target camp, the remaining fuel is dropped at the current position for later use.

There is an arbitrary amount of fuel at the base camp (of which the truck can take at most 3 units), and when the truck has reached position n (target camp), the puzzle is completed. However, when the truck is at one of the positions 1, 2, 3, it can take only as much fuel with it as there is present at the given position.

## Assumptions

1. At any position, there should only be a maximum of 3 units of fuel. This assumption removes a lot of potential moves and allows meaningful running times at higher n

## Running the Challenge

To run the challenge script:

```
$ python3 challenge.py [n_target]
```

To simulate a run using a sequence of moves (L for left, R for right, F for load at base camp, 1 for load 1 fuel at any other station, E for drop at any other station):

```
$ python3 challenge.py [n_target] [sequence of moves]
```

Examples:

```
$ python3 challenge.py 3
Path: FRRR
Time taken: 0.0006921291351318359

$ python3 challenge.py 4 FRE1LF
Fuel at stations: [1, 0, 0, 0]
Truck at position 0 with 3 fuel
```
