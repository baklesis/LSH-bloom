from sklearn.feature_extraction.text import CountVectorizer
#import pandas as pd


def cosine_similarity(doc1, doc2):

    documents = [doc1, doc2]

    # Create the Document Term Matrix

    count_vectorizer = CountVectorizer(stop_words='english')
    count_vectorizer = CountVectorizer()
    sparse_matrix = count_vectorizer.fit_transform(documents)

    # OPTIONAL: Convert Sparse Matrix to Pandas Dataframe if you want to see the word frequencies.
    #doc_term_matrix = sparse_matrix.todense()
    #df = pd.DataFrame(doc_term_matrix,
    #                 columns=count_vectorizer.get_feature_names(),
    #                 index=['doc_trump', 'doc_election', 'doc_putin'])
    #df

    # Compute Cosine Similarity
    from sklearn.metrics.pairwise import cosine_similarity
    print(cosine_similarity(df, df))