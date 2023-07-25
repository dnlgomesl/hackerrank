def has_cycle(head):
    visited_nodes = set()
    while head:
        node_id = id(head)
        if node_id in visited_nodes:
            return 1
        else:
            visited_nodes.add(node_id)
            head = head.next

    return 0