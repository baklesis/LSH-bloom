from bloom_filter import bloom_filter
# false positive probability
fp_probability = 0.05
# number of expected elements
estimated_elements = 20

# create a bloom filter object
bloom_filter = bloom_filter(fp_probability, estimated_elements)

# words that are inserted
inserted_words = ['Hello', 'Goodbye', 'Peace', 'War', 'Love', 'Bank', 'School', 'London', 'Germany', 'Grades', 'Power',
                  'Safe', 'Bomb', 'Study', 'Rage', 'Land', 'House']

# words that are not inserted
non_inserted_words = ['Why', 'Did', 'You', 'Not', 'Insert', 'Us', 'Mean', 'That', 'Is', 'What', 'You', 'Are', 'Miserable',
                      'Person', 'Mad', 'Devastated', 'Humiliated']


# driver code add the first list, check for the first list for existence of elements
# and then check for the list that was not added
for element in inserted_words:
    bloom_filter.add_element(element)

for element in inserted_words:
    bloom_filter.check_membership(element)

for element in non_inserted_words:
    bloom_filter.check_membership(element)
