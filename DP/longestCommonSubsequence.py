class Solution:
    """
    #lookup table approach
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lookup_table = [ [0 for x in range(len(text2)+1)]for x in range(len(text1)+1)]
        for char_1_i, char_1 in enumerate(text1):
            for char_2_i, char_2 in enumerate(text2):
                if char_1 == char_2:
                    lookup_table[char_1_i][char_2_i] = lookup_table[char_1_i][char_2_i]+1
                else:
                    lookup_table[char_1_i][char_2_i] = max(
                              lookup_table[char_1_i][char_2_i+1],
                              lookup_table[char_1_i+1][char_2_i])
        return lookup_table[-1][-1]    
    """
    #recursive with memoization
    def helper(self,s1,s2,i, j,memo):
        if memo[i][j] < 0:    
            if i == len(s1) or j == len(s2):
                memo[i][j] = 0
            elif s1[i] == s2[j]:
                memo[i][j] = 1+ self.helper(s1,s2,i+1,j+1,memo)
            else:
                memo[i][j] = max(self.helper(s1,s2,i+1,j,memo),self.helper(s1,s2,i,j+1,memo))
        return memo[i][j]       
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = [ [-1 for _ in range(n+1)]for _ in range(m+1)]
        return self.helper(text1,text2,0,0,memo)