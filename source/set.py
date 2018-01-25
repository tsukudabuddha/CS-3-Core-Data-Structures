#!python
from linkedlist import LinkedList
from hashtable import HashTable


class Set(object):
    """Set Data Structure w/."""

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.ht = HashTable(init_size)
        self.size = 0

    def contains(self, element):
        """Check if the element is store in set (self)."""
        return self.ht.contains(element)

    def add(self, element):
        """Add new element to set, if unique."""
        self.ht.set(element, True)  # TODO: Try using None
        self.size = self.ht.size

    def remove(self, element):
        """Remove element from set if present. Else raise keyerror."""
        self.ht.delete(element)  # Key error is raised in function
        self.size = self.ht.size

    def union(self, other_set):
        """Return a new set that is the union of self and other_set."""
        all_items = self.ht.items()
        all_items.append(other_set.items())

        if len(self.ht.buckets) > len(other_set.buckets):
            new_table = self.__init__(len(self.ht.buckets))
        else:
            new_table = self.__init__(len(other_set.buckets))

        for item in all_items:
            new_table.add(item)
        return new_table
