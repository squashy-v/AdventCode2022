# Advent of Code 2022
## Day 4
https://adventofcode.com/2022/day/4


### Part 1
Task: In how many assignment pairs does one range fully contain the other?

- Assignment pairs are two ranges  
- A range is fully contained if both the lower bound is less, and the upper bound is greater  


Example Input: 

---
```
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
```
---


After some dirty looping through the list of data eventually created a 2d list that contains a list of each pairing of elf's assignments and the pairings in format `[[2,4],[6,8]]`. Defined a function to check if a list contained another and wrote a for loop to count how many time the function returned true, and had to pass each pair in twice, to compensate for the fact that the second assignment can contain the first as well.



### Part 2
Task: In how many assignment pairs do the ranges overlap?

- Now any overlap should return true  

Now just checking if the bounds of the first assignment surrounds the lowerbound of the second assignement, or checking if the bounds of the first assignment surround the upperbound of the second assignment returns true, and once again checks both assignments on each other.
