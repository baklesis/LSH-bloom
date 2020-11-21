import k_shingles

# We implement a simple 2D list which will be the input matrix.
class list_2D:
    def __init__(self):
        self.list_2D = []

    def add_row(self, row):
        self.list_2D.append(row)


# Here we implement the input matrix.
class input_matrix(object):
    def __init__(self):
        self.doc_shingle_lists = []
        # list to contain the unique not hashed shingles
        self.doc_hashed_lists = []
        # list to contain the unique shingles
        self.unique_shingles_vector = []
        # create a list to hold the input matrix
        self.matrix = list_2D()
        # This list will contain the hashed shingle list for each document.
        self.doc_hashed_lists, self.doc_shingle_lists = k_shingles.shingles_parser()
        # create the shingle vector
        self.create_shingle_vector()
        # based on that vector create the input matrix
        self.create_input_matrix()

    # helper functions:
    def get_width(self):
        return len(self.matrix.list_2D[0])

    def get_height(self):
        return len(self.matrix.list_2D)

    # function to create the shingle vector keeping only the unique shingles found
    def create_shingle_vector(self):
        for hashed_list in self.doc_hashed_lists:
            for hashed_shingle in hashed_list.list:
                if hashed_shingle not in self.unique_shingles_vector:
                    self.unique_shingles_vector.append(hashed_shingle)

    # here we create the input matrix
    def create_input_matrix(self):
        print('Creating the input matrix.')
        # for each shingle in the vector
        for shingle in self.unique_shingles_vector:
            row_to_be_inserted = []
            # append 1s or 0s depending if the shingle exists in the corresponding document
            # this process is ran for each document
            for hashed_list in self.doc_hashed_lists:
                if shingle in hashed_list.list:
                    row_to_be_inserted.append(1)
                else:
                    row_to_be_inserted.append(0)
            self.matrix.add_row(row_to_be_inserted)

    # function to return the document that has the corresponding id
    def find_doc(self, doc_id):
        list = []
        for row in range(len(self.matrix.list_2D)):
            list.append(self.matrix.list_2D[row][doc_id])
        return list










