def set_union(s1, s2):
    s1.tail.next = s2.head
    s1.tail = s2.tail

    return s1
