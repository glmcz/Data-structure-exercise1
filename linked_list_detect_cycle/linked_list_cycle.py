# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # it is based on idea that faster pointer in case of present cycle will cache slower pointer
    # or if the cycle is not present it will reach null faster then slow pointer.
    # The cycle distances where fast pointer have to catch slow one is equal to size of NodeList
    def hasCycle(self, head: ListNode | None) -> bool:
        slow_pointer = head
        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True

        return False



if __name__ == "__main__":
    head = [1, 2, 3, 4]
    index = 1
    print("result is:")
    print(Solution().hasCycle(head=head))