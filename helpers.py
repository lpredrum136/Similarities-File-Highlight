from nltk.tokenize import sent_tokenize
from helpersSubstrings import extractSubstrings

def lines(a, b):
    """Return lines in both a and b"""

    # Extract the lines
    linesA = a.splitlines()
    linesB = b.splitlines()

    # A list of similar lines
    similarLines = []
    
    # Compare and make a list of all the similar occurrences in linesA and linesB
    for line in linesA:
        if line in linesB:
            if line not in similarLines:
                similarLines.append(line)

    # Return
    return similarLines


def sentences(a, b):
    """Return sentences in both a and b"""

    # Extract the sentences
    sentencesA = sent_tokenize(a)
    sentencesB = sent_tokenize(b)

    # A list of similar sentences
    similarSentences = []
    
    # Compare and make a list of all the similar occurrences in sentencesA and sentencesB
    for sentence in sentencesA:
        if sentence in sentencesB:
            if sentence not in similarSentences:
                similarSentences.append(sentence)

    # Return
    return similarSentences

def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # Extract substrings
    substringsA = extractSubstrings(a, n)
    substringsB = extractSubstrings(b, n)

    # A list of similar substrings
    similarSubstrings = []
    
    # Compare and make a list of all the similar occurrences in substringsA and substringsB
    for substring in substringsA:
        if substring in substringsB:
            if substring not in similarSubstrings:
                similarSubstrings.append(substring)

    # Return
    return similarSubstrings