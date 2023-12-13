class LinkedList:
    class Node:
        def __init__(self, data, next):
            self._data = data
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def count_nodes(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_head(self, elem):
        data = self.Node(elem, self._head)
        self._head = data
        self._size += 1

    def add_tail(self, elem):
        data = self.Node(elem, None)
        if self.is_empty():
            self._head = data
        else:
            last_node = self._head
            while last_node._next:
                last_node = last_node._next
            last_node._next = data
        self._size += 1

    def pop_head(self):
        data = self._head
        if self.is_empty():
            raise ValueError()

        self._head = self._head._next
        return data

    def pop_tail(self):
        data = self._head
        if self.is_empty():
            raise ValueError()
        if self._size == 1:
            self._head = self._head._next
        else:
            last_node = self._head
            while last_node._next._next:
                last_node = last_node._next
            data = last_node._next._data
            last_node._next = None
        self._size -= 1
        return data

    def search(self, elem):
        if self.is_empty():
            raise ValueError("The linked list is empty.")

        current = self._head
        while current is not None:
            if current._data == elem:
                return True
            current = current._next
        return False

    def reverse(self):
        if self.is_empty():
            raise ValueError()

        prev = None
        current = self._head
        while current is not None:
            next_node = current._next
            current._next = prev
            prev = current
            current = next_node
        self._head = prev

    def find_middle(self):
        if self.is_empty():
            raise ValueError("Связанный список пуст.")

        slow_pointer = self._head
        fast_pointer = self._head

        while fast_pointer is not None and fast_pointer._next is not None:
            slow_pointer = slow_pointer._next
            fast_pointer = fast_pointer._next._next

        return slow_pointer._data

    def remove_duplicates(self):
        if self._head is None:
            return None
        seen_values = set()
        current = self._head
        prev = None
        while current is not None:
            if current._data in seen_values:
                prev._next = current._next
            else:
                seen_values.add(current._data)
                prev = current

            current = current._next
        return self._head

    def finding_loop(self):
        if self.is_empty():
            raise ValueError()

        fast = self._head._next._next
        slow = self._head._next
        while fast is not None and fast._next is not None:
            if slow == fast:
                return True

        return False

    def __repr__(self):
        ret_str = ""
        ret_str = ret_str + '['
        trav = self._head
        while trav is not None:
            ret_str = ret_str + str(trav._data)
            if trav._next is not None:
                ret_str = ret_str + ', '
            trav = trav._next

        ret_str = ret_str + ']'
        return ret_str
