# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(sub_string):
            print(sub_string)
            return sub_string == sub_string[-1::-1]
    
        i, j = 0, len(s)-1
        count = 0
        while i <= j:
            if s[i] != s[j]:
                if is_palindrome(s[i+1:j+1]):
                    i+=1
                elif is_palindrome(s[i:j]):
                    j-=1
                    print("here")
                else:
                    return False
                count+=1
                continue
            i, j = i+1, j-1
        return True if count <= 1 else False
