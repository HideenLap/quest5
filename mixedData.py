from queue import Queue
import time


class AlternatingOrder:
    def __init__(self):
        self.stack = []
        self.queue = []

    def push(self, elem):
        self.stack.append(elem)

    def enqueue(self, elem):
        self.queue.insert(0, elem)

    def pop_and_print(self):
        if self.stack:
            print(self.stack.pop(), end=' ')
        elif self.queue:
            print(self.queue.pop(), end=' ')

    def print_alternating_order(self):
        while self.queue or self.stack:
            self.pop_and_print()


class TextEditor:
    def __init__(self):
        self.text = ''
        self.undo_stack = []
        self.redo_stack = []

    def insert_text(self, new_text):
        self.undo_stack.append(new_text)
        self.text += new_text
        self.redo_stack = []

    def delete_last_char(self):
        if self.text:
            self.undo_stack.append(self.text)
            self.text = self.text[:-1]
            self.redo_stack = []

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.text)
            self.text = self.redo_stack.pop()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.text)
            self.text = self.redo_stack.pop()

    def get_text(self):
        return self.text


class TwoStack:
    def __init__(self, size):
        self._size = size
        self.array = [None] * size
        self.top1 = -1
        self.top2 = size

    def push1(self, elem):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.array[self.top1] = elem
        else:
            print("Stack Overflow - Cannot push into stack 1")

    def push2(self, elem):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.array[self.top2] = elem
        else:
            print("Stack Overflow - Cannot push into stack 2")

    def pop1(self):
        if self.top1 >= 0:
            poped_item = self.array[self.top1]
            self.top1 -= 1
            return poped_item
        else:
            print('Stack 1 is empty')

    def pop2(self):
        if self.top2 < self._size:
            poped_item = self.array[self.top2]
            self.top2 += 1
            return poped_item
        else:
            print('Stack 2 is empty')


class Stakc:
    def __init__(self):
        self.stack = []

    def reverse(self, elem):
        words = elem.split()
        for word in words:
            self.stack.append(word)
        reversed = ''
        while self.stack:
            reversed += self.stack.pop() + " "

        return reversed


def sort_array_with_queues(arr):
    if not arr:
        return []

    queue1 = Queue()
    queue2 = Queue()

    for element in arr:
        queue1.put(element)

    while queue1.qsize() > 1:
        for _ in range(queue1.qsize() - 1):
            queue2.put(queue1.get())

        max_element = queue1.get()

        while not queue2.empty():
            current_element = queue2.get()
            if current_element > max_element:
                queue1.put(max_element)
                max_element = current_element
            else:
                queue1.put(current_element)

        queue2.put(max_element)

    sorted_array = []
    while not queue2.empty():
        sorted_array.append(queue2.get())

    return sorted_array


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next_song = None


class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, title, artist):
        new_song = Song(title, artist)

        if not self.head:
            self.head = new_song
        else:
            current_song = self.head
            while current_song.next_song:
                current_song = current_song.next_song
            current_song.next_song = new_song

    def display_playlsit(self):
        current_song = self.head
        while current_song:
            print(f'{current_song.title} by {current_song.artist}')
            current_song = current_song.next_song


def is_balanced_parentheses(value):
    left = '{[('
    right = '}])'
    stack = []

    for character in value:
        if character in left:
            stack.append(character)
        elif character in right:
            if len(stack) == 0:
                return False
            if right.index(character) != left.index(stack.pop()):
                return False
    return len(stack) == 0


class CustomerServiceSimulation:
    def __init__(self):
        self.customer_queue = Queue()

    def enqueue_customer(self, customer_name):
        print(f"{customer_name} has joined the queue.")
        self.customer_queue.put(customer_name)

    def process_customers(self):
        while not self.customer_queue.empty():
            customer_name = self.customer_queue.get()
            print(f"Now serving {customer_name}.")
            time.sleep(2)  # Simulating some processing time

    def run_simulation(self):
        print("Customer service simulation is starting.")
        self.enqueue_customer("Customer1")
        self.enqueue_customer("Customer2")
        self.enqueue_customer("Customer3")

        self.process_customers()

        print("Customer service simulation is complete.")


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def merge_sorted_list(list1, list2):
    temp = Node()
    current = temp
    while list1 is not None and list2 is not None:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return temp.next


class LinkedList:
    def __init__(self):
        self._size = 0
        self._head = None

    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def add(self, elem):
        new_node = self.Node(elem, self._head)
        self._head = new_node
        self._size += 1

    def is_empty(self):
        return self._size == 0

    def remove_nth_node(self, n):
        if self.is_empty() or n <= 0:
            return

        if n == 1:
            self._head = self._head.next
            self._size -= 1
            return

        current = self._head
        for _ in range(n - 2):
            if current is None or current.next is None:
                return

            current = current.next

        if current.next is not None:
            current.next = current.next.next
            self._size -= 1

    def display_linked_list(self):
        current = self._head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage:
if __name__ == "__main__":
    ll = LinkedList()

    for i in range(1, 6):
        ll.add(i)

    print("Original linked list:")
    ll.display_linked_list()

    n = 3
    ll.remove_nth_node(n)

    print(f"Linked list after removing every {n}th node:")
    ll.display_linked_list()
