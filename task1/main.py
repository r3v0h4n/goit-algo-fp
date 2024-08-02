from linked_list import LinkedList

def reverse_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev

def merge_sort(linked_list):
    if linked_list.head is None or linked_list.head.next is None:
        return linked_list

    middle = get_middle(linked_list.head)
    next_to_middle = middle.next

    middle.next = None

    left = LinkedList()
    left.head = linked_list.head
    right = LinkedList()
    right.head = next_to_middle

    left = merge_sort(left)
    right = merge_sort(right)

    sorted_list = merge(left.head, right.head)
    sorted_linked_list = LinkedList()
    sorted_linked_list.head = sorted_list
    return sorted_linked_list

def get_middle(node):
    if node is None:
        return node

    slow = node
    fast = node

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.data <= right.data:
        result = left
        result.next = merge(left.next, right)
    else:
        result = right
        result.next = merge(left, right.next)
    return result

def merge_sorted_lists(list1, list2):
    merged_head = merge(list1.head, list2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head
    return merged_list

def main():
    llist = LinkedList()
    llist.append(10)
    llist.append(20)
    llist.append(15)
    llist.append(5)
    llist.append(30)

    print("Original list:")
    llist.print_list()

    reverse_list(llist)
    print("Reversed list:")
    llist.print_list()

    sorted_llist = merge_sort(llist)
    print("Sorted list:")
    sorted_llist.print_list()

    llist1 = LinkedList()
    llist1.append(1)
    llist1.append(3)
    llist1.append(5)

    llist2 = LinkedList()
    llist2.append(2)
    llist2.append(4)
    llist2.append(6)

    merged_llist = merge_sorted_lists(llist1, llist2)
    print("Merged sorted lists:")
    merged_llist.print_list()

if __name__ == "__main__":
    main()