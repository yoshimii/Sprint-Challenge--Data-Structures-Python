from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_oldest = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == 0:
            self.storage.add_to_tail(item)
            self.current_oldest = self.storage.head
        elif self.storage.length == self.capacity:
            self.current_oldest.value = item
            if self.current_oldest.next == None:
                self.current_oldest = self.storage.head
            else:
                self.current_oldest = self.current_oldest.next
            return
            # self.current_oldest = self.current_oldest.prev.next
        else: self.storage.add_to_tail(item) 

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        node = self.storage.head
        
        while node:
            list_buffer_contents.append(node.value)
            node = node.next

        
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
