Intuition
we have to generate subsets of an array .the total no of subsets is
2**n where n is length of an array

Approach
we know gray code by using that method generating subsets of an array
example:[1,2,3]
0 1 2
0 0 0 0 --> []
1 0 0 1 --> [3]
2 0 1 0 --> [2]
3 0 1 1 --->[2,3]
4 1 0 0 -->[1]
5 1 0 1--->[1,3]
6 1 1 0 -->[1,2]
7 1 1 1 -->[1,2,3]
-->in above gray code we use to generate subsets .
-->where 0 we dont take
-->where 1 is there we take that position element in this we can generate all substes (2**n)

Complexity
Time complexity:O(2∗∗n∗n)O(2**n*n)O(2∗∗n∗n)
Space complexity:O(n)O(n)O(n)
Code:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=1<<len(nums) #total no of subsets (2**3)
        # binary format 1<<3=8
        a=[]
        for i in range(n):
            l=[]
            for j in range(len(nums)):#cases 
                if (i&1<<j):# checking each setbit with number i 
                    l.append(nums[j])
            a.append(l)
        return a



        
