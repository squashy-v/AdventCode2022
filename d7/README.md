# Advent of Code 2022
## Day 7
https://adventofcode.com/2022/day/7


### Part 1
Task: Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

-Filesystem mirrors linux filesytem with / being the root
-cd = change directory
-ls = list stuff
-Directories do not have any inherient size


Example Input:

---
```
---
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
```
---

Made a file class to store file names, and their sizes. Made a directory class to store file objects, and recursively calculate their size based on the size of their inner objects.

### Part 2
