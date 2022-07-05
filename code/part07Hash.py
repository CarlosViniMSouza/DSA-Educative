import pprint


class Hashtable:
    def __init__(self, elements):
        self.bucket_size = len(elements)
        self.buckets = [[] for i in range(self.bucket_size)]
        self._assign_buckets(elements)

    def __str__(self):
        # pformat returns a printable representation of the object
        return pprint.pformat(self.buckets)

    def _assign_buckets(self, elements):
        # calculates the hash of each key
        for key, value in elements:
            hashed_value = hash(key)

            # positions the element in the bucket using hash
            index = hashed_value % self.bucket_size
            # adds a tuple in the bucket
            self.buckets[index].append((key, value))

    def get_value(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        bucket = self.buckets[index]
        for key, value in bucket:
            if key == input_key:
                return value
        return None


if __name__ == "__main__":
    capitals = [
        ('France', 'Paris'),
        ('United States', 'Washington D.C.'),
        ('Italy', 'Rome'),
        ('Canada', 'Ottawa')
    ]

    hashtable = Hashtable(capitals)

    print(hashtable)
    print(f"The capital of Italy is {hashtable.get_value('Italy')}")

    """
    output:
    
    [[('Italy', 'Rome'), ('Canada', 'Ottawa')],
     [('France', 'Paris')],
     [('United States', 'Washington D.C.')],
     []]
    The capital of Italy is Rome
    """