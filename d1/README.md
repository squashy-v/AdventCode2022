# Advent of Code 2022
## Day 1
https://adventofcode.com/2022/day/1


### Part 1
Task: Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

- Each line is a snack that an elf is holding
- New lines indicate a new elf is writing


Example Input:

---
```
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
```
---


Opened and split raw input on each double newline `.split("\n\n")` to seperate each elf's input, and then split each elf's input on newlines to make a 2d list containing the calorie counts of each elf.

Used list comprehension for each list of calories to turn it from a list of str to int and then summed each list and compared against a running variable storing highest count.



### Part 2
Task: Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?


Using the same list and list comprehension added the sum of each new list, sorted the new list from greatest to smallest. Used slices to return a sublist first 3 entries and summed those to get answer.