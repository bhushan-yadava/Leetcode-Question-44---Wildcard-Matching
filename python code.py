class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # Get the lengths of the input string and the pattern
        length_s, length_p = len(s), len(p)
      
        # Create a DP table with default values False
        dp = [[False] * (length_p + 1) for _ in range(length_s + 1)]
      
        # The empty pattern matches the empty string
        dp[0][0] = True
      
        # Initialize first row of the DP table, considering the pattern starting with '*'
        for j in range(1, length_p + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
      
        # Fill the DP table
        for i in range(1, length_s + 1):
            for j in range(1, length_p + 1):
                # If characters match or pattern has '?', we can move back diagonally in the table (match found)
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                # If pattern has '*', we check two cases:
                # 1. '*' matches no character: move left in the table
                # 2. '*' matches at least one character: move up in the table
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        # Return the value at the bottom-right corner of the DP table
        return dp[length_s][length_p]
