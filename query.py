import os

def bm25(query, documents):
    # Get average document length
    averageLength = 0
    for docName, docText in documents:
        averageLength += len(docText)
    averageLength /= len(documents)

    print(averageLength)


def skip_bigrams(query, documents):
    print("Not implemented")


def split_nonalphanumeric(s):
    split_str = []
    lastPos = 0
    pos = 0
    while pos < len(s):
        if not s[pos].isalnum():
            if lastPos == pos:
                lastPos += 1
            else:
                split_str.append(s[lastPos:pos])
                lastPos = pos + 1
        pos += 1
    if lastPos != pos:
        split_str.append(s[lastPos:pos])
    return split_str


query = raw_input("Enter your search query:\n")
presidents = []
directory = './Presidents/edited'
for doc in os.listdir(directory):
    docText = split_nonalphanumeric(open(directory + "/" + doc, "r").read())
    presidents.append((doc, docText))

bm25(query, presidents)