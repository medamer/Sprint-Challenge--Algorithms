#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The time complexity for while loop is O(n), this mean the algorithm will walk trough
   the range of 0 and n*n*n.


b) The time complexity of the this function is O(nlog n), because it has loop inside a loop.
   The for loop time complexity is O(n) and the for while loop is also O(n).


c) The time complexity of this function is O(n), this function is using a fixed number of operations, 
   if 0 retuens 0, otherwise make recursive to bunnyEars(bunnies-1).

## Exercise II
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution

The best algorithm to use in this problem is the binary search:
   - First the base case will be : if the n == 1, we return 0m this mean the egg breaks already in if thrown off the 1st floor.
   - If n is > 1, then we will have to find midpoint: then check if the egg breaks we won't need to go up, so our searching will be between 0 and n-1 floor.
   - otherwide if the egg does not break, we elemenate the lower floors and we search up, between n+1 and the last floor.
   - and we repeat the process for our new range of search, find the midpoit and check..
   - Once we found the last floor where the egg does not break, we return the answer as list of floors starting from 0 to n-target.

   the time complexity for this algorithm is O(log n)
