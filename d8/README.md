# Advent of Code 2022
## Day 8
https://adventofcode.com/2022/day/8


### Part 1
Task: How many trees are visible from outside the grid?

- Each tree is a single digit  
- A tree is the height of its size 0 = short 9 = tallest
- A tree can be seen if all the trees between it and the border on anyside are shorter than it  
- All the trees on the border can be seen  

Example Input:

---
```
30373
25512
65332
33549
35390
```
---


Split file on newlines, then split each line into a list. Wrote a convinence function to make looping through the 2 array vertically as easy as horizontally. Wrote a tallest_tree function that splits each row/column in half and checks each half for visability and returns early if the tree is visable. Counted the peremeter and added that to the count. Looped through every element of the 2d array skipping the edges and then checking left right up and down of the tree for visability using the tallest_tree function and adds to the counter if visable.


### Part 2
Task: What is the highest scenic score possible for any tree?

- Number of trees visable from any tree in any direction determines scenic score  
- Scenic score is found by multiplying number of visable trees in every direction
- Edge trees have 0 visable trees in that direction  
- Trees of same hight block the view  

Blah
