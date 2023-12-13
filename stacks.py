class ArrayStack:
    def __init__(self):
        self._data = []
        self._min_stack = []
        self.stack = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, obj):
        self._data.append(obj)
        if not self._min_stack or obj <= self._min_stack[-1]:
            self._min_stack.append(obj)

    def peek_top(self):
        if self.is_empty():
            raise IndexError()
        return self._data[-1]

    def get_min(self):
        if not self._min_stack:
            raise ValueError("Стек пуст.")
        return self._min_stack[-1]

    def peek_bot(self):
        if self.is_empty():
            raise IndexError()
        return self._data[0]

    def pop(self):
        if self.is_empty():
            raise IndexError()
        popped = self._data.pop()
        if popped == self._min_stack[-1]:
            self._min_stack.pop()
        return popped

    def postfix(self, expression):
        def operation(operator, operand1, operand2):
            if operator == '+':
                return operand1 + operand2
            elif operator == '*':
                return operand1 * operand2
            elif operator == '/':
                return operand1 / operand2
            elif operator == '-':
                return operand1 - operand2

        arr = expression.split()

        for token in arr:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                self.stack.append(int(token))
            else:
                operand2 = self.stack.pop()
                operand1 = self.stack.pop()
                result = operation(token, operand1, operand2)
                self.stack.append(result)
        return self.stack[0]

    def reverse(self):
        def reverse_help():
            if not self.is_empty():
                top_element = self.pop()
                reverse_help()
                self.push_to_bottom(top_element)

        reverse_help()

    def push_to_bottom(self, item):
        if self.is_empty():
            self.push(item)
        else:
            top_element = self.pop()
            self.push_to_bottom(item)
            self.push(top_element)

    def sort_stack(self):
        sorted_stack = ArrayStack()
        while not self.is_empty():
            temp = self.pop()
            while not sorted_stack.is_empty() and sorted_stack.peek_top() > temp:
                self.push(sorted_stack.pop())
            sorted_stack.push(temp)
        while not sorted_stack.is_empty():
            self.push(sorted_stack.pop())

    def is_balanced_parentheses(self, value):
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
