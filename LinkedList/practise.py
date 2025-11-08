# Interview question of linkedlist

# remove duplicates from sorted
def sorted(self):  # since the duplicates can be found in the neigbour, we can only take 1 pointer
    current = self.head
    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return


# remove duplicates from unsorted
def unsorted(self):
    current = self.head
    prev = None
    seen = set()
    while current:
        if current.value in seen:
            prev.next = current.next
        else:
            seen.add(current.value)
            prev = current
        current = current.next