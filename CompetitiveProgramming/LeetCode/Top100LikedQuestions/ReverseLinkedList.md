### Python
```python
class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # [1, 2, 3]
    # 1.next -> 2.next -> 3.next -> None
    # 3.next -> 2.next -> 1.next -> None
    prev_h = None
    while head:
      # 1.next
      if (prev_h is None):
        # [1]
        if (head.next is None):
          return head
        prev_h = head
        head = head.next
        prev_h.next = None
        continue
      # prev_h  -> 1.next
      # head    -> 2.next
      temp = head.next
      head.next = prev_h
      prev_h = head
      head = temp
    return prev_h
```
