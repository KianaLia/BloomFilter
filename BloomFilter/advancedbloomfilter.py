import numpy as np
from math import log

class AdvancedBloomFilter():
    """AdvancedBloomFilter 
        is a dynamic bloom filter which calculates the optimal 
        size and hash function numbers to store n given elements with 
        false positive probability of p
    """
    def __init__(self, num_items, false_pos_prob):
        """__init__ initializes the AdvancedBloomFilter

        :param num_items: max number of items to hash
        :type num_items: int
        :param false_pos_prob: desired probability of false positive answers
        :type false_pos_prob: float
        """
        self.array_size = self.array_size(num_items, false_pos_prob)
        self.array = np.zeros(self.array_size)
        self.hash_count = self.hash_count(self.array_size, num_items) 
    
    def array_size(self,n,p):
        """Returns the size of the array"""
        return int(-(n * log(p))/(log(2)**2))

    def hash_count(self,m,n):
        """hash_count calculates optimal number of hash functions

        :param m: size of the bit array
        :type m: int
        :param n: max nuber of items to hash
        :type n: int
        :return: optimal number of hashes
        :rtype: int
        """
        return int((m/n) * log(2))

    def insert(self, member):
        for h in range(self.hash_count):
            idx = hash((member,h)) % self.array_size
            self.array[idx] = 1

    def lookup(self, member):
        for h in range(self.hash_count):
            idx = hash((member,h)) % self.array_size
            if self.array[idx] == 0:
                return False
        return True

    def properties(self):
        print(f'Array Size: {self.array_size}')
        print(f'Hash Count: {self.hash_count}')

    def show(self):
        print(self.array)