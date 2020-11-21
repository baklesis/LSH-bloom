from bplus_tree import BPlusTree
from bloom_filter import bloom_filter
import time

# false positive probability for the bloom filter:
fp_probability = 0.05
# elements estimated for the bloom filter:
estimated_elements = 20
# maximum amount of children in the b+ tree:
order = 4
# Starting time to compare:
start_time = 0


#create one tree and one filter
bplustree = BPlusTree(order)
bloom_filter = bloom_filter(fp_probability, estimated_elements)

# read from the file words_cut.txt
# a smaller version of the file words.txt
file = open('words_cut.txt', 'r')
# empty list
words = []

# start reading line by line
line = file.readline()
# formatting of the line remove the \n
formated_line = line[: - 1]
#add the word to the list of words
words.append(formated_line)
# repeat the same process till the EOF
while line:
    line = file.readline()
    formated_line = line[: - 1]
    words.append(formated_line)

# counter for the b+ tree
bplus_key_counter = 0

# populate the tree with elements
for word in words[: - 1]:

    bplustree.insert(bplus_key_counter, word)
    print(bplustree.retrieve(bplus_key_counter))
    bplus_key_counter = bplus_key_counter + 1

print(f'Number of entries in B+ tree: {bplus_key_counter - 1}')

start_time = time.time()
i = 0
for word in words[: - 1]:
    bplustree.retrieve(i)
    i = i + 1

print("--- %s seconds ---" % (time.time() - start_time))

input(">")

#counter for the bloom filter insertion process
bloom_filter_counter = 0
# and now fill the bloom filter
for word in words[: - 1]:

    bloom_filter.add_element(word)
    bloom_filter.check_membership(word)
    bloom_filter_counter = bloom_filter_counter + 1

print(f'Number of entries in bloom filter: {bloom_filter_counter - 1}')

start_time = time.time()

for word in words[: - 1]:
    bloom_filter.check_membership(word)

print("--- %s seconds ---" % (time.time() - start_time))
