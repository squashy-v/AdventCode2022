# Advent of Code 2022
## Day 6
https://adventofcode.com/2022/day/6


### Part 1
Task: How many characters need to be processed before the first start-of-packet marker is detected?

- start-of-packet marker is 4 non-repeating characters in a row  


Example Input:

---
```
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
```
---

Grab the entire string from the input file and loop through its index, adding the first 3 characters in the string to a list. On every iteration after i = 3 check the current 4 characters for dupes using the list.count() method and then returning the index + 1 because i is the first character of the packet.



### Part 2
Task: How many characters need to be processed before the first start-of-message marker is detected?

- Now looking for 13 non-repeating characters in a row  

Just increased the size of the list containing recent characters to 13.
