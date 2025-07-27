from indexer import build_index
import math
from collections import defaultdict

index, doc_freq, doc_lengths, documents = build_index()

def search(query):
    query_terms = query.lower().split()
    scores = defaultdict(float)

    for term in query_terms:
        if term in index:
            postings = index[term]
            idf = math.log(len(documents) / (1 + doc_freq[term]))
            for doc, tf in postings:
                tfidf = (tf / doc_lengths[doc]) * idf
                scores[doc] += tfidf

    results = sorted(scores.items(), key=lambda x: -x[1])
    return results
