# Advent of Code 2022
## Day 3
https://adventofcode.com/2022/day/3


### Part 1
Task: Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

- Uppercase A and lowercase a are different items  
- Rucksack is split exactly in half  
- a-z = 1-26, A-Z = 27-52  


Example Input:

---
```
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
```
---

Stole list generation from previous days, made a 2d list storing each rucksack as a list containing each strings for each pocket. Looped through first pocket checking for any matching letters in second pocket, and when found return the letter to a new list. Mapped the letters from the new_list to their priority with the map and a user defined return_prio function. Summed final list of priorities.



### Part 2
Task: Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?

- Groups of three lines are groups of elves  
- Elf group badges are represented by the common item shared between all three  

Instead of spliting the rucksacks in half, returned the full rucksack and split each grouping of three into a new list using list comprehension `[rucksack_list[i:i+3] for i in range(0, len(rucksack_list), 3)]`. Then looped through the first rucksack in each group checking for a an identical item in the other two rucksacks, and once found return that item and break the loop to prevent dupes. Then reused return_prio and sum to get new result.
