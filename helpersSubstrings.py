""" To extract substrings without duplicates
Parameters: string s, int n where n is the number of characters required in the substring
return a list of substrings without duplicates"""

def extractSubstrings(s, n):
    # A list of substrings
    substrings = []

    # Start extracting
    for i in range(len(s)):
        if i + n > len(s):
            break
        substring = s[i:i + n]
        if substring in substrings:
            continue
        substrings.append(substring)

    # Return
    return substrings