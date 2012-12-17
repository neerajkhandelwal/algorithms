Algorithms
==========

**N Kings**  
You have to place the N kings in on N squared chess board so that no two kings are in same row and column and do not attack each other.

About input, first line of the input is number of testcases T. Then every next 2 lines are for the testcase. In the first line N is the size of chess board and K is the number of Kings already in place starting from first row. Next line has K numbers. Each "number"(pos) in position i is in the row i and column "number" in which king is already placed. 0 <= K <= N. 0 <= pos[i] <= N-1

About output: Output will be the number of possible ways kings can be placed modulus 1000000007.

Input:  
2  
3 0  

4 1  
2  

Output:  
0  
1

**Algorithm**  
Solved the problem recursively by setting up board and checking every column for each row if the current position is valid. You can see the solution as Depth First Search as we traverse up till the leaf(solution). The algorithm uses Constraint Programming by default as the first row after the place peice will always have minimum constraint that is will have less possible positions to start with.
______________________________________________