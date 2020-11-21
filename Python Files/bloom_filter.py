import math
import murmurhash
from bitarray import bitarray

class bloom_filter(object):
    def __init__(self, false_pos_prob, expected_elements):
        # The false positive probability will be given as an argument.
        self.false_pos_prob = false_pos_prob
        # The number of expected elements will be given as an argument.
        self.expected_elements = expected_elements
        # The bit array size will be calculated by a function.
        self.bit_size = self.calculate_bit_size()
        # The number of hash functions used will also be calculated by a function.
        self.hash_num = self.calculate_hash_num()
        # To create the bit array we will use the function bitarray(size) from the module bitarray.
        self.bit_array = bitarray(self.bit_size)
        # We initialise the bit array with all values as zero.
        self.bit_array.setall(0)

    def calculate_bit_size(self):
        # We calculate the array bit size which is provided by a mathematical formula which is shown below.
        bit_size = - ((self.expected_elements * math.log(self.false_pos_prob)) / math.log(2) ** 2)
        # We cast the result to int because we need an integer size.
        return int(bit_size)

    def calculate_hash_num(self):
        # We calculate the optimal number of hash functions using the formula below.
        hash_num = (self.bit_size / self.expected_elements) * math.log(2)
        # We cast the result to int because we need an integer number of hash functions.
        return int(hash_num)

    def add_element(self, element):
        # We will hash the element as many times as hash_num defines.
        for times in range(self.hash_num):
            '''We hash using the murmur hashing method which is a widespread choice.
            Using times as a seed each time we will get a different response.
            With this we manage to get hash_num different hash functions.
            We module the response with bit_size to avoid getting out of bounds.'''
            response = murmurhash.hash(element, times) % self.bit_size
            # Set the bit of the indexed cell of the array to true.
            self.bit_array[response] = True
        print(f'Element {element} was added successfully.')

    def check_membership(self, element):
        # We will hash the element as many times as hash_num defines.
        for times in range(self.hash_num):
            #We hash again.
            response = murmurhash.hash(element, times) % self.bit_size
            '''If we find at least one array cell indexed by response whose
            value is false then we surely know that the element cannot exist.'''
            if (self.bit_array[response] == False):
                print(f'Element {element} definitely does not exist.')
                return
        # If every indexed cell was found true the element may exist.
        print(f'The element {element} might exist.')
