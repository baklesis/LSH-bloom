import random

# Maximum possible value of a single 32-bit shingle.
# since we hash them to a length of 32 bits the max value is:
max_shingle_value = 2 ** 32 - 1
# The closest prime number above x,where x is the input to the has function.
# max input is 2^32-1 so the next prime of that is the following one to be using as the hashing ring
next_prime = 4294967311
# The number of functions we will use to generate a signature.
hash_functions = 10
# the form of the hash functions is:
# H(x)=(ax+b)%c.
# where a,b are random coefficients in the range (0, 2^32-1)
# and c is our prime number


def generate_random_unique_numbers(number_of_functions):
    '''The variable number_of_functions serves as a counter to the number
    of random numbers we need to create a list to host the numbers we create.'''
    list_of_numbers = []
    while number_of_functions > 0:
        random_number = random.randint(0, max_shingle_value)
        # Make sure the number is unique.
        while random_number in list_of_numbers:
            # Re-roll the number if it is not unique
            random_number = random.randint(0, max_shingle_value)
        # Add the number into the list once it's certain it's unique.
        list_of_numbers.append(random_number)
        # Reduce the counter.
        number_of_functions = number_of_functions - 1
    return list_of_numbers


def min_hash(number_of_hash_functions, input_matrix_height, number_of_documents, input_matrix):
    print('Creating the signature matrix using minhash algorithm.')
    # This list is going to contain all the lists we create below.
    signature_matrix = []
    # before we start hashing we initialize all the values to a "max" value out of their range
    # which will be replaced later on with the minimum value we find
    # 2 lists of 10 unique coefficients each
    a_coefficients = generate_random_unique_numbers(hash_functions)
    b_coefficients = generate_random_unique_numbers(hash_functions)
    for function in range(number_of_hash_functions):
        signature_matrix.append([next_prime + 1] * number_of_documents)
    for row in range(input_matrix_height):
        # empty list to contain the signature
        # temporary, used to hold the "permuted" value
        list_of_hashed_values = []
        # start hashing and appending the values in the list
        for function in range(number_of_hash_functions):
            list_of_hashed_values.append((a_coefficients[function] * row + b_coefficients[function]) % next_prime)
        # for each document:
        for column in range(number_of_documents):
            # if in the input matrix we find an 1 for any of the shingles
            if input_matrix.matrix.list_2D[row][column] == 1:
                # we check if  the value inside our temporary list of signatures
                # (the small one that is going to be inserted to the matrix):
                for function in range(number_of_hash_functions):
                    # if our value produced by the hash function is smaller that that of our signature matrix
                    # we replace the value inside the signature matrix with the smallest one
                    # which represents a random permutation
                    if list_of_hashed_values[function] < signature_matrix[function][column]:
                        signature_matrix[function][column] = list_of_hashed_values[function]
    # return the matrix containing the signature
    return signature_matrix
