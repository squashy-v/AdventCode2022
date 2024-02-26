# Advent of Code 2022
## Day 5
https://adventofcode.com/2022/day/5


### Part 1
Task: After the rearrangement procedure completes, what crate ends up on top of each stack?

-Each column is a stack of crates
-Each instruction moves one crate at a time from the old stack to the new one


Example Input:

---
Original Configuration:
```
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
```
Instruction input:
```
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
```
---

Original Configuration
```
[N]     [Q]         [N]            
[R]     [F] [Q]     [G] [M]        
[J]     [Z] [T]     [R] [H] [J]    
[T] [H] [G] [R]     [B] [N] [T]    
[Z] [J] [J] [G] [F] [Z] [S] [M]    
[B] [N] [N] [N] [Q] [W] [L] [Q] [S]
[D] [S] [R] [V] [T] [C] [C] [N] [G]
[F] [R] [C] [F] [L] [Q] [F] [D] [P]
 1   2   3   4   5   6   7   8   9
 ```

 Finally decided that the boiler plate OOP was worth and and made a class for manipulating the crate configuration. Instead of using a 2d array, decided to throw together a quick class (CrateStack) for FILO string storage, that also keeps track of its own length. Also made a class (CrateConfig) for storing a set number of CrateStacks with methods to abstract the CrateStacks methods for easy looping in a for loop.



 ### Part 2
Task: After the rearrangement procedure completes, what crate ends up on top of each stack?

-Now multiple cranes can be moved at once

 Even though the crates aren't always moved in FILO anymore, making a new move_crates function that moves each group of crates in FIFO (just stored them in an array and move out of that array in reverse order), but still treats each new instruction as FILO like the old code does. Allows for moving groups of crates within an instruction to be FIFO, but the instructions over all to be FILO.
