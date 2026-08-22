# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode();
        # head will always be occupied, so therefore we have to do work on the tail node adn then return next on dummy
        tail = dummy
        # if l1 value is less, add first, other way around as well
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1;
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next;
            # move forward for next case
            tail = tail.next
    # edge case for non equal length linked lists
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
        