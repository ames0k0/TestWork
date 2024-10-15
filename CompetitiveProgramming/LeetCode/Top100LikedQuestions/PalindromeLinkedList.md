### Python
```python
# version 1: WA
class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    # [1, 2, 2, 2, 2, 1]
    # add(1)
    # add(2)
    # pop(2)
    # add(2)
    # pop(2)
    # pop(1)
    stack = []
    while (head is not None):
      if (not stack):
        stack.append(head.val)
      elif (head.val == stack[-1]):
        stack.pop()
      else:
        stack.append(head.val)
      head = head.next
    # hacks
    if stack:
      l_stack = len(stack)
      # XXX, WA: [1, 2, 2]
      if (l_stack == 1):
        return True
      # [1, 2, 3, 4]
      if (l_stack % 2 == 0):
        return False
      while True:
        first = stack.pop(0)
        if (not stack):
          return True
        if (first != stack[-1]):
          return False
        stack.pop()
        if (not stack):
          return True
    return True

# version 2
class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    p = ''
    while (head):
      p += str(head.val)
      head = head.next
    p_len = len(p)
    if (not p):
      return False
    p_len = len(p)
    if (p_len == 1):
      return True
    if (p[:p_len//2] == ''.join(reversed(p[(p_len//2) + p_len%2:]))):
      return True
    return False
```
