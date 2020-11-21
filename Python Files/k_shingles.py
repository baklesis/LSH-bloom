import murmurhash
from sys import argv

class list_pointer(object):
    # Helpful class that implements a pointer to a list.
    def __init__(self):
        self.list = []

    def set_list(self, s_list):
        self.list = s_list

    def print_list(self):
        print(self.list)

# function used to parse the shingles
def shingles_parser():
    while True:
        # Ask the user for the shingles size.
        try:
            # The k of the k-shingles.
            shingle_size = int(input("Give me the size of shingles: "))
        except ValueError:
            # To avoid giving anything different than a number.
            print("Input is invalid please give me a number: ")
            continue
        if shingle_size <= 0:
            # If the number is not valid.
            continue
        else:
            break

    # This list will hold the hashed document shingles and will be accessed by the documents id.
    documents_list = []

    doc_shin_list = []

    for doc_argument in range(len(argv[1:])):
        # Append a list pointer for every document so it can later point to the hashed shingles list.
        documents_list.append(list_pointer())

    for document_name, document_id in zip(argv[1:], range(len(argv[1:]))):
        # Opens a file stream to read the document.
        file = open(document_name, 'r', encoding = 'utf8')

        # To store the document's text in line.
        document = file.read()

        # Replaces the newline characters with blank space.
        document = document.replace('\n', ' ').replace('\r', '')

        # Initialise an empty list which will hold the values from hashing the unique shingles.
        hashed_doc_shingles = []
        shingles = []
        print(f'Shingling the document: {document_name}')
        # Loop through the entire document to get shingles.
        for i in range(len(document) - shingle_size + 1):
            # The shingle will be a slice starting from i and ending at i + shingle_size.
            shingle = document[i: (i + shingle_size)]
            # We hash the shingle to a 32-bit integer.
            hashed_shingle = murmurhash.hash(shingle)
            # Same way we want only want to keep unique hashed shingles.
            if hashed_shingle not in hashed_doc_shingles:
                hashed_doc_shingles.append(hashed_shingle)
            if shingle not in shingles:
                shingles.append(shingle)
        documents_list[document_id].set_list(hashed_doc_shingles)
        doc_shin_list.append(shingles)
    return documents_list, doc_shin_list
