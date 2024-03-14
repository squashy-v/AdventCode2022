# Advent of Code 2022
## Day 9
https://adventofcode.com/2022/day/9


### Part 1
Task: How many positions does the tail of the rope visit at least once?

- Rope is made of up 2 parts H (head) and T (tail)  
- H and T must always be touching  
- Diagonally and overlapping count as touching  
- If head moves 2 in any direction tail also moves in same direction to touch  
- If head and tail are in different rows and columns tail moves one diagonally  

Initial State:
---
```
......
......
......
......
H.....    (H covers T)
```
---

Example Input:
---
```
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
```
---


First implementation was extraordinarily messy, I had a ropebridge class with a head and tail of numpy array and a state of a zeroed out numpy ndarray. Had a move head function (simple) only moved one space at a time, this would call an update tail function (basically a wrapper) checks if the tail needs to move and early returns if not, otherwise calls move tail and then update state. Move tail was just a big elif chain to move the tail in the cardinal directions using this formula `self.tail[x] += (diff[x] // 2)` and in the diagonals using this formula `self.tail[x] += (diff[x] // 2); self.tail[y] += diff[y]`. The update state function just indexed into the state array based on tail coords and set value to 1. The main problem with was I used a fixed size ndarray for the state. In the example problem the initial state is a 6x5 array and never changes, in the full problem set, there is no set dimentions, and the movements take place on an infinately growing plane. My solution was to just make a 1000x1000 initial state and put the starting points at (500, 500), which works for the full set, but is not a generic solution.


### Part 2
Task: How many positions does the tail of the rope visit at least once?

- Now the rope is 9 knots long

Blah
