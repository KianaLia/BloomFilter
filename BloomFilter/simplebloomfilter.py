import numpy as np

class SimpleBloomFilter():
    """SimpleBloomFilter 
    is a static bloom filter which gets 
    array size and hash counts from the user and does rhe hashing.
    """
    def __init__(self, array_size, hash_count=1):
        """__init__ initializes the bloom filter

        :param array_size: size of the bit array
        :type array_size: int
        :param hash_count: number of hash functions, defaults to 1
        :type hash_count: int, optional
        """

        self.array_size = array_size
        self.array = np.zeros(self.array_size)
        self.hash_count = hash_count 

    def insert(self, member):
        """inserts new member into bloom filter

        :param member: new member to insert 
        :type member: int
        """
        for h in range(self.hash_count):
            idx = hash((member,h)) % self.array_size
            self.array[idx] = 1

    def lookup(self, member):
        """lookup checks if member is in set

        :param member: item to lookup
        :type member: int
        :return: is item is in set
        :rtype: Boolean
        """
        for h in range(self.hash_count):
            idx = hash((member,h)) % self.array_size
            if self.array[idx] == 0:
                return False
        return True

    def properties(self):
        """properties returns the properties of filter
        """
        print(f'Array Size: {self.array_size}')
        print(f'Hash Count: {self.hash_count}')

    def show(self):
        """show returns the bit array of the filter
        """
        print(self.array)