# Advent of Code 2022
## Day 7
https://adventofcode.com/2022/day/7


### Part 1
Task: Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

- Filesystem mirrors linux filesytem with / being the root  
- cd = change directory  
- ls = list stuff  
- Directories do not have any inherient size  


Example Input:

---
```
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

Read from file, generating list of commands, and removed each ls command. Made a directory class that returns all its properties, can add children items, calculate its own size, and find child directories inside itself. Wrote functions to loop through the entire directory structure finding all the directories with sizes greater than or less than specific values. Calculating size, finding child directories, and finding directories bigger or smaller all use recursive calls of themselves to dig down into the directory tree. Looped through instructions and depending on the input added a new file, directory, or changed directories by going up one, or finding a directory in the current working directory. After building up the root object which holds the entire directory tree, ran calc_size on root to calculate sizes for the entire tree, and then found all directories less than 100000 and added them to list, finally summed list.

### Part 2
Task: Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?

- Filesystem is 70000000 bytes big  
- The update takes 30000000 bytes  

Calculated the size needed to update, found all the directories bigger than that with dir_over_value, and then looped through targets to find the smallest one and print its size.
