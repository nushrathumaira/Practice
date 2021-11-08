class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        #dp solution
        # idea comes from that current substring(i,j) is palindrome
        #if if substring(i + 1, j - 1) is a palindrome and Si == Sj,
        #i.e. In other words, if we already know that
        #current substring is a palindrome we need to add equal characters on both
        #sides to make a longer palindrome.
        #Time complexity: O(n ^ 2). Space complexity: O(n ^ 2), where
        #n is the length of the string.
        
        #Initialize 2d table for storing results
        n = len(s)
        results = [[False]*n for i in range(n)]
        x, y = 0, 0  # start, end of longest palindromic substring so far
        # every 1-letter substring is a palindrome
        for i in range(n):
            results[i][i] = True
        # 2-letter substring(i, j) is a palindrome if string[i] == string[j]
        for i in range(n-1): #n-1 because of index i+1
            if s[i] == s[i+1]:
                results[i][i+1] = True
                # change longest palindrome to the 1st 2-letter palindrome
                if not x and not y:
                    x, y = i , i + 1
        #now for when results[i][j] == true then results[i+1][j-1] == true
        #and s[i] == s[j]
        for k in range(2,n):
            for i in range(n-2): #loop goes from 0 to n-1,because i+1 needs to stop one element before n
                j = i+k # j needs to start from 2 at least to get valid j-1
                # break the loop if it exceeds the boundaries of the matrix
                if j == n:
                    break
                # check if current substring is a palindrome
                if results[i+1][j-1] and s[i] == s[j]:
                    results[i][j] = True
                    # len(substring(i, j)) > len(substring(x, y))
                    # this way we always choose 1st longest palindrome
                    if j -1 > y -x:
                        x,y = i,j
        return s[x:y+1]
        """
        #one of the solution for this problem uses manacher's algorithm which has 0(N) complexity
        s_len = len(s)
        if s_len <= 1: 
            return s
        min_start_idx = 0
        max_len_of_substr = 1
        i = 0
        while i < s_len:
            r_ptr = i
            l_ptr = i
            #skip duplicate characters in the middle and find the middle of palindrome
            while r_ptr < s_len-1 and s[r_ptr] == s[r_ptr+1]: r_ptr += 1
            i = r_ptr+1 #for next iter
            #expland the selection from middle out as long as it is a palindrome
            while r_ptr < s_len-1 and l_ptr and s[r_ptr+1] == s[l_ptr-1]:
                r_ptr += 1
                l_ptr -= 1
            new_len = r_ptr-l_ptr+1 #record best palindrome
            if new_len > max_len_of_substr:
                min_start_idx = l_ptr
                max_len_of_substr = new_len
        return s[min_start_idx:min_start_idx+max_len_of_substr]