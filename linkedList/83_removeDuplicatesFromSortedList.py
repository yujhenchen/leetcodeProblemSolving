# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head

        nodes = {}
        currNode = head
        while currNode != None:
            key = currNode.val
            if key in nodes:
                nextNode = currNode.next
                nodes[key].next = nextNode
                # del nodes[key]
                currNode = nextNode
            else:
                nodes[key] = currNode
                currNode = currNode.next
        return head
