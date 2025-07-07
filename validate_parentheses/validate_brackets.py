


class Solution:
    def isValid(self, s: str) -> bool:
        # validate parenthesis
        stack = []
        for c in s:
            if '(' in c or '{' in c or '[' in c:
                if len(stack) == 0:
                    return False

            match c:
                case ')':
                    if '(' in stack[-1]:
                        stack.pop()
                    else:
                        return False

                case '}':
                    if '{' in stack[-1]:
                        stack.pop()
                    else:
                        return False

                case ']':
                    if '[' in stack[-1]:
                        stack.pop()
                    else:
                        return False

                case _:
                    stack.append(c)

        if len(stack) == 0:
            return True
        else:
            return False



    def isValidBetter(self, s: str):
        stack = []
        map_close_to_open = { ')': '(', '}': '{', ']': '[' }
        for c in s:
            if c in map_close_to_open: # getting only close bracket keys
                if stack and stack[-1] == map_close_to_open[c]: # get values of closed bracked keys
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False