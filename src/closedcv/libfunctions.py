class Stack:
    def __init__(self, init_list:list=[]):
        """
        Initializes the stack.
        :param init_list: The contents of the stack, defaults to empty, if passed a list the first 0th item will be the first in, and the last item of the list will be last item in.
        """
        self._list = init_list

    def __str__(self):
        return str(self._list)

    def __len__(self):
        return len(self._list)

    def push(self, item):
        """
        Used to add something to the stack.
        :param item: Adds item to the stack (following LIFO)
        :return: None
        """
        self._list.append(item)
        return None

    def pop(self):
        """
        Used to get the last item added to the stack, then delete it from the stack.
        :return: the last item in the stack
        """
        return self._list.pop()

    def peek(self):
        """
        Also known as top(), returns the last item added to the stack WITHOUT deleting it.
        :return: the last item in the stack
        """
        return self._list[len(self._list)]

    def top(self):
        """
        Also known as peek(), returns the last item added to the stack WITHOUT deleting it.
        :return: the last item in the stack
        """
        return self._list[len(self._list)]

    def empty(self):
        """
        Returns boolean whether or not the stack is empty.
        :return: True/False is the stack empty.
        """
        return len(self._list) > 0