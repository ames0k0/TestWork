### Python
```python
class Solution:
  def mergeTwoLists(self,
                    list1: Optional[ListNode],
                    list2: Optional[ListNode]) -> Optional[ListNode]:
    merged_head = None
    next_data = None
    while True:
      to_peek = None
      if (list1 is not None) and list1:
        to_peek = list1
      if (list2 is not None) and list2:
        if (to_peek is not None):
          if (list1.val > list2.val):
            to_peek = list2
            list2 = list2.next
          else:
            list1 = list1.next
        else:
          to_peek = list2
          list2 = list2.next
      else:
        if (list1 is not None):
          list1 = list1.next
      if (to_peek is None):
        break
      if (merged_head is None):
        merged_head = ListNode(to_peek.val)
        next_data = merged_head
        continue
      merged_head.next = ListNode(to_peek.val)
      merged_head = merged_head.next
    return next_data
```
