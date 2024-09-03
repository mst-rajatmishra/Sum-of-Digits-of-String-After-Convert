class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Step 1: Convert the string to a large number based on alphabet positions
        num_str = ''.join(str(ord(c) - ord('a') + 1) for c in s)
        
        # Convert the large number string to integer
        num = int(num_str)
        
        # Step 2: Perform the digit sum transformation k times
        for _ in range(k):
            num = sum(int(digit) for digit in str(num))
        
        return num
