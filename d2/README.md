# Advent of Code 2022
## Day 2
https://adventofcode.com/2022/day/2


### Part 1
Task: What would your total score be if everything goes exactly according to your strategy guide?

- First column, A = rock, B = paper, C = scisors  
- Second column, X = rock, Y = paper, Z = scisors  
- 1pt for rock, 2 for paper, 3 for scisors  
- 0pt for loss, 3 for tie, 6 for win  

Example Input:

---
```
A Y
B X
C Z
```
---


Tweaked the list generation from day 1 to generate a list of rounds. Wrote a determine_round function with a bunch of if statments to return the values 0 3 or 6 based on win loss or tie. Wrote a determine_score function to call the determine_round function and then add the value of 1 2 or 3 based on what was played that round. Mapped stratagy accross determine_score function `map(determine_score, stratagy)` and summed the list to find total score.



## Part 2
Task: Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

- Second column, X = lose, Y = draw, Z = win  

Wrote new function brute force map each old symbol to the new one based on new instructions. Passed new list into old functions to solve.

On both part 1 & 2 ran into a problem where in conditionals a bracket got missed and caused the index to always return 0 and evaluate. `round[0 == "X"` instead of `round[0] == "X"`.
