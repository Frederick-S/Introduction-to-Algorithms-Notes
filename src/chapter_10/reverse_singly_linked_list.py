def reverse_singly_linked_list(singly_linked_list):
    prev = singly_linked_list.head
    current = prev.next if prev is not None else None

    while current is not None:
        next = current.next
        current.next, prev = prev, current
        current = next

    singly_linked_list.head.next = None
    singly_linked_list.head, singly_linked_list.tail = \
        singly_linked_list.tail, singly_linked_list.head

    return singly_linked_list
