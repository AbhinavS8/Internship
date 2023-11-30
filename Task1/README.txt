The program uses recursion to find all possible combinations of a set of characters/numbers
For example take 1,2,3,4. First it will find all combinations under 1 specifically 1  1,2  1,2,3  1,2,3,4  1,3  1,3,4  1,4
Then it will find combinations under 2 ie  2  2,3  2,3,4  2,4 and then for the rest of the characters
To sort the combinations, it adds all the elements in order into a dictionary based on the length of the combination
Finally it allows the user to search for the index position of a combination in the sorted list
