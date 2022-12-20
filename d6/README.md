# Advent of Code 2022
## Day 6
https://adventofcode.com/2022/day/6


### Part 1
Task: How many characters need to be processed before the first start-of-packet marker is detected?


Example Input:

```
---
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
---
```

Grab the entire string from the input file and loop through its index, adding the first 3 characters in the string to a list. On every iteration after i = 3 check the current 4 characters for dupes using the list.count() method and then returning the index + 1 because i is being increased after the dupelicate check.



### Part 2

Just increased the size of the list containing recent characters to 13.