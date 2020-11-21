import input_matrix
import minhash
import lsh
import jaccard_sim
from ttictoc import TicToc
import os
from sys import argv

# Time counters for the preprocessing and the LSH procedure.
pre = TicToc()
aft = TicToc()

# Here starts the preprocessing.
pre.tic()
# create an input matrix and a signature matrix using minhash
in_matrix = input_matrix.input_matrix()
sig_matrix = minhash.min_hash(minhash.hash_functions, in_matrix.get_height(), in_matrix.get_width(), in_matrix)
pre.toc()
# Here ends the preprocessing.

print(f'The preprocessing took: {pre.elapsed} seconds')
input('Press enter to continue with the LSH procedure:')

# Here starts the LSH procedure.
aft.tic()
# The second argument is either none or zero.
# If it is zero we print the steps else we don't.
# used for testing mainly
candidates = lsh.procedure(sig_matrix, None)
aft.toc()
# Here ends the LSH procedure.

print(f'The LSH procedure took: {aft.elapsed} seconds')
input('Press enter to continue with calculating the Jaccard similarity between the candidates:')

# Now having the candidates we can calculate the Jaccard similarity of them.
checked_pairs = []
results = []
# start comparing the "promising" candidates as the lsh algorithm is probabilistic with posibble false positives
for row in range(len(candidates)):
    # start for each row
    for column in range(len(candidates[row])):
        # start comparing the pairs
        for sub_column in range(len(candidates[row][column])):
            for element in range(sub_column + 1, len(candidates[row][column])):
                # check if the pair has already been checked to avoid comparing it twice
                if not (((candidates[row][column][sub_column], candidates[row][column][element]) in checked_pairs) or ((candidates[row][column][element], candidates[row][column][sub_column]) in checked_pairs)):
                    # update the list that contains the pair of elements that has been checked with our current pair
                    checked_pairs.append((candidates[row][column][sub_column], candidates[row][column][element]))
                    # compute the jaccard similarity
                    jac_sim = jaccard_sim.jaccard_similarity(in_matrix.doc_shingle_lists[candidates[row][column][sub_column]], in_matrix.doc_shingle_lists[candidates[row][column][element]])
                    # store the result
                    index1 = int(str(candidates[row][column][sub_column])) + 1
                    index2 = int(str(candidates[row][column][element])) + 1
                    comparison = f'Comparison between the documents: {argv[index1]} and {argv[index2]}. Jaccard similarity: {jac_sim}\n'
                    results.append(comparison)

count = 0
# print all results
for comp in results:
    count = count + 1
    print(comp)
print(f'Did {count} comparisons.')

filelist = [ f for f in os.listdir(os.getcwd()) if f.endswith(".txt") ]
for f in filelist:
    os.remove(os.path.join(os.getcwd(), f))
