# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head

        # Find middle of the list
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next

        # Slit the list into 2 
        curr = slow.next
        prev = None
        slow.next = None

        # Reverse the 2nd portion of the list
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        list1 = head
        list2 = prev

        # Merge the 2 lists
        while (list2):
            temp1 = list1.next
            temp2 = list2.next

            list1.next = list2
            list2.next = temp1

            list1 = temp1
            list2 = temp2
