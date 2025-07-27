import os
from collections import defaultdict

def tokenize(text):
    return text.lower().split()

def build_index(folder="pages"):
    doc_freq = defaultdict(int)
    index = defaultdict(list)
    doc_lengths = {}
    documents = {}

    for filename in os.listdir(folder):
        with open(os.path.join(folder, filename), encoding='utf-8') as f:
            content = f.read()
            tokens = tokenize(content)
            documents[filename] = content
            doc_lengths[filename] = len(tokens)

            tf = defaultdict(int)
            for token in tokens:
                tf[token] += 1

            for term, freq in tf.items():
                index[term].append((filename, freq))
                doc_freq[term] += 1

    return index, doc_freq, doc_lengths, documents
