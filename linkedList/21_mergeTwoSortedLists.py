# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if list1 == None and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        result = None
        insertNode = None
        currNode = None
        if list1.val >= list2.val:
            result = currNode = list2
            insertNode = list1
        else:
            result = currNode = list1
            insertNode = list2

        currPre = None
        while insertNode is not None and currNode is not None:
            nextInsert = insertNode.next
            nextCurr = currNode.next
            if insertNode.val < currNode.val:
                currPre.next = insertNode
                insertNode.next = currNode
                currPre = insertNode
                insertNode = nextInsert
            else:
                currPre = currNode
                currNode = nextCurr
        if insertNode is not None:
            currPre.next = insertNode
        return result
