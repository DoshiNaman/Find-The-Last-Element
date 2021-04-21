# Find-The-Last-Element
Find the last element after repeatedly removing every second element from either end alternately

Given an array arr[] consisting of N integers, the task is to find the last remaining array element after removing every second element, starting from the first and last alternately.

Examples:

Input: arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Output: 8
Explanation: Elements in the list are: 1 2 3 4 5 6 7 8 9 10
Starting from first array element, removing every second element from arr[] = {1, 2. 3, 4, 5, 6, 7, 8, 9, 10} modifies arr[] to {2, 4, 6, 8, 10}.
Starting from last array element, removing every second element from arr[] = {2, 4, 6, 8, 10} modifies arr[] to {4, 8}.
Starting from first array element, removing every second element from arr[] = {4, 8} modifies arr[] to {8}.
Therefore, the last remaining element in the array is 8.

Input: arr[] = {2, 3, 5, 6}
Output: 3

Naive Approach: 
  The simplest approach to solve this problem is to remove every second element in the array starting from the first and last indices alternately, until the size of the array reduces to 1. Print the last array element remaining after performing the given operations. 
