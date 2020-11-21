from minhash import generate_random_unique_numbers

# rows per band to be used in lsh
band_rows = 10
# the next prime of 2^32-1
next_prime = 4294967311
# the number of buckets to be used in lsh
buckets_number = 10000000


# partitioning function to split the matrix into bands
def partition_to_bands(signature_matrix):
    signature_matrix_height = len(signature_matrix)
    # List bands will be a 3D-list which will hold the bands.
    bands = []
    # from 0 until the height of the matrix
    # append a block of the signature matrix to the bands until we have
    # parsed the whole signature matrix
    for index in range(0, signature_matrix_height, band_rows):
        band = signature_matrix[index: (index + band_rows)][:]
        bands.append(band)
    return bands


# here we concatenate the signatures inside a band so we hash them all together
def conc_signatures_in_bands(signature_matrix, bands):
    signature_matrix_width = len(signature_matrix[0])
    # This list holds the concatenated signatures for all the bands.
    conc_signatures = []
    # initialize the signature
    conc_signature = 0
    for band in range(len(bands)):
        # create a temporary list
        band_conc_signatures = []
        for signature in range(signature_matrix_width):
            # for each signature we have
            for row in range(band_rows):
                # start concatenating the signatures
                conc_signature = int(str(conc_signature) + str(bands[band][row][signature]))
            # append the concatenated signature and start over
            band_conc_signatures.append(conc_signature)
            conc_signature = 0
        # return the final list containing 1 string per band
        conc_signatures.append(band_conc_signatures)
    return conc_signatures


# the hashing of the concatenating signatures
def hash_conc_signatures(conc_signatures, bands):
    number_of_bands = len(bands)
    # dynamically calculate the number of hash functions to be used equal to the number of bands
    number_of_hash_functions = number_of_bands
    # generate 2 lists of unique coefficients to be used by the hash functions
    a_coefficients = generate_random_unique_numbers(number_of_hash_functions)
    b_coefficients = generate_random_unique_numbers(number_of_hash_functions)
    hash_tables_list = []
    # create a hash_table to hold the buckets for each signature
    for band in (range(len(conc_signatures))):
        hash_table = []
        # append empty lists to hold the buckets
        for counter in range(buckets_number):
            hash_table.append([])
        # parallel for loop
        for column, signature in zip(range(len(conc_signatures[band])), conc_signatures[band]):
            # hash each signature to a bucket (20 buckets in total)
            index = (a_coefficients[band] * signature + b_coefficients[band]) % buckets_number
            # append the corresponding column to the corresponding position based on the hash
            hash_table[index].append(column)
        # append the table to our list of tables
        hash_tables_list.append(hash_table)
    return hash_tables_list


# function to determine the candidates
def candidates(hash_tables_list):
    # empty list to contain the to-be candidates
    candidate_list = []
    # start iterating over the list the previous function returned
    for row in range(len(hash_tables_list)):
        # temporary list to hold the candidates of one band
        row_candidates_matches = []
        for column in range(len(hash_tables_list[row])):
            # if there are at least 2 elements in our list we have a candidate pair
            if len(hash_tables_list[row][column]) > 1:
                column_candidates_matches = []
                # append all the candidates to a new list and pass it to the candidate_list
                for matches in range(len(hash_tables_list[row][column])):
                    column_candidates_matches.append(hash_tables_list[row][column][matches])
                row_candidates_matches.append(column_candidates_matches)
        candidate_list.append(row_candidates_matches)
    return candidate_list


# this function runs all of the required functions
# for the comparison in the correct order
def procedure(signature_matrix, mode):
    # If mode = 0 it prints else it doesn't.
    # create the babds based on the signature matrix
    bands = partition_to_bands(signature_matrix)
    if mode == 0:
        print("Here is the bands matrix:")
        print(bands)
        input("Press enter to continue:")
    # concatenate the signatures belonging to the same band
    conc_signatures = conc_signatures_in_bands(signature_matrix, bands)
    if mode == 0:
        print("Here is the concatenated signatures matrix:")
        print(conc_signatures)
        input("Press enter to continue:")
    # create the list holding the buckets
    hash_tables_list = hash_conc_signatures(conc_signatures, bands)
    # extract the candidate pairs from the list
    candidates_list = candidates(hash_tables_list)
    if mode == 0:
        print("Here is the candidates list: ")
        print(candidates_list)
        input("Press enter to continue:")
    # return the extracted pairs
    return candidates_list
