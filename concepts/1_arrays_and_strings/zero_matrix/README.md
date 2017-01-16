# Description
Write an algorithm to check if an element in an MxN matrix is 0, then set the entire row and col to 0.

# How to solve
Make two arrays to see if the 0 has already been set.

# Thought Process
1. loop though the entire matrix.
2. can reduce to O(1) time by only setting to 0 when needed.
3. check for the first col and row on its own.
