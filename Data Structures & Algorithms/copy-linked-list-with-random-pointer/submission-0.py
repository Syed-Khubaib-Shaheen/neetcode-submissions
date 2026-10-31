
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {None: None}

        # First pass: Create copies of all nodes
        current = head

        while current:
            copy = Node(current.val)
            old_to_new[current] = copy
            current = current.next

        # Second pass: Connect next and random pointers
        current = head

        while current:
            copy = old_to_new[current]

            copy.next = old_to_new[current.next]
            copy.random = old_to_new[current.random]

            current = current.next

        # Return the head of the copied list
        return old_to_new[head]
