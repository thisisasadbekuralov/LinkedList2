class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def count_elements(self):
        count_dict = {}
        current = self.head
        while current:
            data_type = type(current.data).__name__
            if data_type not in count_dict:
                count_dict[data_type] = 1
            else:
                count_dict[data_type] += 1
            current = current.next
        return count_dict

    def find_string_indices(self, string):
        indices = []
        current = self.head
        index = 0
        while current:
            if isinstance(current.data, str) and string in current.data:
                indices.append(index)
            current = current.next
            index += 1
        return indices

    def remove_zeros(self):
        prev = None
        current = self.head
        while current:
            if current.data == 0:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
            else:
                prev = current
            current = current.next

    def to_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def to_tuple(self):
        return tuple(self.to_list())

    def zigzag_swap(self):
        current = self.head
        while current and current.next:
            current.data, current.next.data = current.next.data, current.data
            current = current.next.next

