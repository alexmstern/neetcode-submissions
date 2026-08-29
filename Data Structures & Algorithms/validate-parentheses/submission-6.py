class Solution:
    def isValid(self, s: str) -> bool:
        matches = {'(':')', '{':'}', '[':']'}
        stack = []
        for c in s:
            if c in matches.keys():
                stack.append(c)
            else:
                if not stack:
                    return False
                if matches[stack.pop()] != c:
                    return False
        
        return len(stack) == 0