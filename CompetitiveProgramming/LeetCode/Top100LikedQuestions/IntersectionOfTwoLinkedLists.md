### Python
```python
class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    merges = set()
    it = None
    while headA:
      merges.add(id(headA))
      headA = headA.next
    while headB:
      bid = id(headB)
      if (bid in merges):
        return headB
      headB = headB.next
```
