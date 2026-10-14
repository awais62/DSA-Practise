class Solution:

  def isValid(self, s: str) -> bool:
    stack = []
    # Map closing brackets to their corresponding opening brackets
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
      if char in mapping:
        # Pop the top element from stack if it's not empty, otherwise assign a dummy value
        top_element = stack.pop() if stack else "#"

        # If the mapped opening bracket doesn't match the top element, it's invalid
        if mapping[char] != top_element:
          return False
      else:
        # If it's an opening bracket, push it onto the stack
        stack.append(char)

    # Return True if the stack is empty (all brackets matched), False otherwise
    return not stack