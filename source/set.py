#!python
from linkedlist import LinkedList
from hashtable import HashTable
from copy import deepcopy

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
        self.ht.set(element, None)
        self.size = self.ht.size

    def remove(self, element):
        """Remove element from set if present. Else raise keyerror."""
        self.ht.delete(element)  # Key error is raised in function
        self.size = self.ht.size

    def union(self, other_set):
        """Return a new set that is the union of self and other_set."""
        union_set = deepcopy(self)

        for item in other_set.ht.items():
            union_set.add(item)
        return union_set

    def intersection(self, other_set):
        """Return a new set that is the intersection of self and other_set."""
        intersection_set = Set()
        my_items = self.ht.items()
        other_items = self.ht.items()
        if len(my_items) < len(other_items):
            for item in my_items:
                if my_items.contains(item):
                    intersection_set.add(item)
        else:
            for item in other_items:
                if other_items.contains(item):
                    intersection_set.add(item)

        return intersection_set

    def difference(self, other_set):
        """Return a new set that is the difference of self and other_set."""
        difference_set = Set()

        for item in self.ht.items():
            if not other_set.contains(item):
                difference_set.add(item)
        return difference_set

    def is_subset(self, other_set):
        """Return a boolean indicating whether other_set is a subset of this set."""
        for item in other_set.ht.items():
            if not self.contains(item):
                return False
        return True


if __name__ == "__main__":
    s1 = Set()
    s2 = Set()
    s2.add("Andrew")
    s1.add("Apple")
    s3 = s1.union(s2)
    print(s3.ht.items())
