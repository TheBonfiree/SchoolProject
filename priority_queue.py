# priority_queue.py
# Mirador, Josh Matthew, C.


class Pet:
    """Pet model — convert Ben's dict into this before enqueuing."""
    def __init__(self, pet_id, name, breed, owner_name, severity, arrival_order):
        self.pet_id        = pet_id
        self.name          = name
        self.breed         = breed
        self.owner_name    = owner_name
        self.severity      = severity        # int (1-5)
        self.arrival_order = arrival_order   # int, for tie-breaking

    @staticmethod
    def from_dict(pet_id, details, arrival_orsssder):
        """Convert Ben's dict format into a Pet object."""
        return Pet(
            pet_id        = pet_id,
            name          = details["Pet Name"],
            breed         = details["Breed"],
            owner_name    = details["Owner Name"],
            severity      = int(details["Condition Severity"]),
            arrival_order = arrival_order
        )


# ---------------------------------------------------------------

class PriorityQueueNode:
    def __init__(self, pet):
        self.pet  = pet
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head  = None
        self._size = 0

    def enqueue(self, pet):

        new_node = PriorityQueueNode(pet)

        if self.is_empty():
            self.head   = new_node
            self._size += 1
            return

        current  = self.head
        previous = None

        while current is not None:

            if pet.severity < current.pet.severity:
                break

            if pet.severity == current.pet.severity:
                if pet.arrival_order < current.pet.arrival_order:
                    break

            previous = current
            current  = current.next

        if previous is None:
            new_node.next = self.head
            self.head     = new_node
        else:
            new_node.next = current
            previous.next = new_node

        self._size += 1

    def dequeue(self):

        if self.is_empty():
            print("[Queue] No pets to serve. Queue is empty.")
            return None

        served_pet = self.head.pet
        self.head  = self.head.next
        self._size -= 1

        return served_pet

    def remove(self, pet_id):

        if self.is_empty():
            print("[Queue] Nothing to remove. Queue is empty.")
            return False

        current  = self.head
        previous = None

        while current is not None:

            if current.pet.pet_id == pet_id:

                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                self._size -= 1
                return True

            previous = current
            current  = current.next

        print(f"[Queue] Pet with ID '{pet_id}' was not found in the queue.")
        return False

    def peek(self):
        if self.is_empty():
            print("[Queue] No pets to peek at. Queue is empty.")
            return None
        return self.head.pet

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size
