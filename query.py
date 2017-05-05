import os, math

# Constants
directory = './Presidents/edited'
k1 = 2
b = 0.4

def bm25(query, bigram_query, documents):
    # Document names to scores
    scored_documents = []

    # Get average document length
    average_length = 0
    for docName, docText, doc_bigrams in documents:
        average_length += len(docText)
    average_length /= len(documents)

    # Computing document name to word frequency
    documents_containing = {}  # items like word -> count
    word_frequency = {}  # items like (word, doc_name) -> frequency
    for word in query:
        for doc_name, doc_text, doc_bigrams in documents:
            frequency = doc_text.count(word)
            if word not in documents_containing:
                documents_containing[word] = 0
            if frequency > 0:
                documents_containing[word] += 1
            word_frequency[(word, doc_name)] = frequency
    for bigram in bigram_query:
        for doc_name, doc_text, doc_bigrams in documents:
            frequency = doc_bigrams.count(bigram)
            if bigram not in documents_containing:
                documents_containing[bigram] = 0
            if frequency > 0:
                documents_containing[bigram] += 1
            word_frequency[(bigram, doc_name)] = frequency

    # Score each document
    for doc_name, doc_text, doc_bigrams in documents:
        score = 0
        for word in (query + bigram_query):
            nq = documents_containing[word]
            idf_sum = math.log10(
                (len(documents) - nq + 0.5) / 
                (nq + 0.5)
            )
            term_freq = word_frequency[(word, doc_name)]
            score += abs(idf_sum * (
                (term_freq * (k1 + 1)) / 
                (term_freq + k1 * ((1 - b) + b * (len(doc_text) / average_length)))
            ))

        scored_documents.append((doc_name, score))

    return scored_documents


def split_nonalphanumeric(s):
    split_str = []
    last_pos = 0
    pos = 0
    while pos < len(s):
        if not s[pos].isalnum():
            if last_pos == pos:
                last_pos += 1
            else:
                split_str.append(s[last_pos:pos].lower())
                last_pos = pos + 1
        pos += 1
    if last_pos != pos:
        split_str.append(s[last_pos:pos].lower())
    return split_str

def create_skip_bigrams(arr):
    bigrams = []
    for i in range(0, len(arr) - 1):
        bigrams.append((arr[i], arr[i + 1]))
        if i < len(arr) - 2:
            bigrams.append((arr[i], arr[i + 2]))

    return bigrams

while True:
    query = raw_input("Enter your search query, or 'q' to quit:\n")
    if query == "q":
        break
    query = split_nonalphanumeric(query)

    presidents = []
    for doc in os.listdir(directory):
        docText = split_nonalphanumeric(open(directory + "/" + doc, "r").read())
        presidents.append((doc, docText, create_skip_bigrams(docText)))

    scored_bm25 = bm25(query, create_skip_bigrams(query), presidents)
    scored_bm25 = sorted(scored_bm25, key=lambda x: x[1], reverse=True)
    num_to_print = 10
    for doc_name, score in scored_bm25:
        if num_to_print > 0:
            print((doc_name, score))
        num_to_print -= 1
