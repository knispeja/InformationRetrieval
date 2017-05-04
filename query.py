def bm25(query):
    # TODO: get average document length
    print("Not implemented")


def skip_bigrams(raw_text):
    print("Not implemented")


def overall_score(query, document):
    print("Not implemented")


def split_nonalphanumeric(s):
    pos = 1
    while pos < len(s) and s[pos].isalnum():
        pos += 1
    return (s[:pos], s[pos:])

query = raw_input("Enter something")
print split_nonalphanumeric(query)
