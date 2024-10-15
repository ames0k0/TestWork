### Python
```python
class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    hids = set()
    while True:
      if (head is None):
        return False
      hid = id(head)
      if (hid in hids):
        return True
      hids.add(hid)
      if (head.next is None):
        return False
      head = head.next
```
