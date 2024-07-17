from my_list_node import MyListNode


class MySortedDoublyLinkedList:
    """A base class providing a doubly linked list representation."""

    def __init__(self, head: 'MyListNode' = None, tail: 'MyListNode' = None, size: int = 0) -> None:
        """Create a list and default values are None."""
        self._head = head
        self._tail = tail
        self._size = size

    def __len__(self) -> int:
        """Return the number of elements in the list."""
        return self._size

    def __str__(self) -> str:
        """Return linked list in string representation."""
        result = []
        node = self._head
        while node:
            result.append(node.elem)
            node = node.next_node
        return str(result)

    # The following methods have to be implemented.

    def get_value(self, index: int) -> int:
        """Return the value (elem) at position 'index' without removing the node.

        Args:
            index (int): 0 <= index < length of list

        Returns:
            (int): Retrieved value.

        Raises:
            ValueError: If the passed index is not an int or out of range.
        """
        # TODO
        if not isinstance(index, int) or index < 0 or index >= len(self):
            raise ValueError("The index is not an int or out of range")

        current = self._head
        for i in range(index):
            current = current.next_node

        return current.elem


    def search_value(self, val: int) -> int:
        """Return the index of the first occurrence of 'val' in the list.

        Args:
            val (int): Value to be searched.

        Returns:
            (int): Retrieved index.

        Raises:
            ValueError: If val is not an int.
        """
        # TODO

        if not isinstance(val, int):
            raise ValueError("The Value is not an int")

        current_node = self._head
        index = 0
        while current_node:
            if current_node.elem == val:
                return index
            current_node = current_node.next_node
            index += 1
        return -1

    def insert(self, val: int) -> None:
        """Add a new node containing 'val' to the list, keeping the list in ascending order.

        Args:
            val (int): Value to be added.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError("The Value is not an int")

        new_node = MyListNode(val)
        prev_node = None
        current_node = self._head


        if current_node == None or current_node.elem >= val:
            new_node.next_node = current_node
            self._head = new_node
            self._size += 1
            return

        while current_node:
            if current_node.elem > val:
                break
            prev_node = current_node
            current_node = current_node.next_node

        prev_node.next_node = new_node
        new_node.next_node = current_node
        self._size += 1

    def remove_first(self, val: int) -> bool:
        """Remove the first occurrence of the parameter 'val'.

        Args:
            val (int): Value to be removed.

        Returns:
            (bool): Whether an element was successfully removed or not.

        Raises:
            ValueError: If val is not an int.
        """
        # TODO
        if not isinstance(val, int):
            raise ValueError("Value is not an int")

        current_node = self._head
        prev_node = None

        if current_node == None:
            return False

        if current_node.elem == val:
            self._head = current_node.next_node
            self._size -= 1
            return True

        while current_node:
            if current_node.elem == val:
                prev_node.next_node = current_node.next_node
                self._size -= 1
                return True
            prev_node = current_node
            current_node = current_node.next_node

        return False

    def remove_all(self, val: int) -> bool:
        """Remove all occurrences of the parameter 'val'.

        Args:
            val (int): Value to be removed.

        Returns:
            (bool): Whether elements were successfully removed or not.

        Raises:
            ValueError: If val is not an int.
        """
        # TODO
        if not isinstance(val, int):
            raise ValueError("Value is not an int")

        current_node = self._head
        prev_node = None
        has_something_been_removed = False

        while current_node:
            if current_node.elem == val:
                if prev_node == None:
                    self._head = current_node.next_node
                else:
                    prev_node.next_node = current_node.next_node
                self._size -= 1
                has_something_been_removed = True
            else:
                prev_node = current_node
            current_node = current_node.next_node

        return has_something_been_removed

    def remove_duplicates(self) -> None:
        """Remove all duplicate occurrences of values from the list."""

        current_node = self._head
        prev_node = None

        while current_node:
            if prev_node != None and prev_node.elem == current_node.elem:
                prev_node.next_node = current_node.next_node
                self._size -= 1
            elif current_node.next_node and current_node.elem == current_node.next_node.elem:
                prev_node = current_node
                prev_node.next_node = current_node.next_node.next_node
                self._size -= 1
            else:
                prev_node = current_node
            current_node = current_node.next_node

    def filter_n_max(self, n: int) -> None:
        """Filter the list to only contain the 'n' highest values.

        Args:
            n (int): 0 < n <= length of list

        Raises:
            ValueError: If the passed value n is not an int or out of range.
        """
        if not isinstance(n, int) or n <= 0 or n > len(self):
            raise ValueError("n must be an integer greater than 0 and less than or equal to the length of the list.")

        elements = []

        current_node = self._head
        while current_node:
            elements.append(current_node.elem)
            current_node = current_node.next_node

        elements.sort()

        elements = elements[-n:]

        new_head = None
        new_tail = None
        for elem in elements:
            new_node = MyListNode(elem)
            if new_head is None:
                new_head = new_node
            if new_tail is not None:
                new_tail.next_node = new_node
                new_node.prev_node = new_tail
            new_tail = new_node

        self._head = new_head
        self._tail = new_tail
        self._size = n

    def filter_odd(self) -> None:
        """Filter the list to only contain odd values."""
        # TODO
        current_node = self._head

        while current_node:
            if current_node.elem % 2 == 0:
                if current_node.prev_node != None:
                    current_node.prev_node.next_node = current_node.next_node
                else:
                    self._head = current_node.next_node
                if current_node.next_node != None:
                    current_node.next_node.prev_node = current_node.prev_node
                self._size -= 1
            current_node = current_node.next_node

    def filter_even(self) -> None:
        """Filter the list to only contain even values."""
        # TODO
        current_node = self._head

        while current_node:
            if current_node.elem % 2 != 0:
                if current_node.prev_node != None:
                    current_node.prev_node.next_node = current_node.next_node
                else:
                    self._head = current_node.next_node
                if current_node.next_node != None:
                    current_node.next_node.prev_node = current_node.prev_node
                self._size -= 1
            current_node = current_node.next_node