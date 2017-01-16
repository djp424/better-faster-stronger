# Description
3 Things can be done to a sting in this problem:
1. insert character
2. remove character
3. replace character
Given 2 strings, write a function that checks if they are one edit or zero edits away

# Test Cases
pale, pal (true) - remove one
pales, pale (true) - add one
pale, bale (true) - change one
pale, bake (false) - two steps away

# Thought Process
1. Check for all 3 cases
2. Check for amount of instances of each case
3. Consider edge case - only having one character
4. Does uppercase count? - no
5. Do spaces count? - no
6. Can we check for both insert and remove at the same time? - probably yes
7. Can you check for all 3 at the same time? - probably yes
8. Do a separate check for 0 edits away
9. Thought of this case later: removing a char from the beginning of string
