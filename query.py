import os

def bm25(query):
    # TODO: get average document length
    print("Not implemented")


def skip_bigrams(raw_text):
    print("Not implemented")


def overall_score(query, document):
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
for doc in os.listdir('./Presidents/edited'):
    overall_score(query, doc)