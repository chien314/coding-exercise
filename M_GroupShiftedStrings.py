# TC:O(k*n) =SC, where n be the length of strings and k be the maximum length of a string in strings
# note that: 
# C++/Java: a % b = a - int(a / b) * b
# Python: a % b = a - floor(a / b) * b

def groupStrings(self, strings):
    groups = collections.defaultdict(list)
    for s in strings:
        groups[tuple((ord(c) - ord(s[0])) % 26 for c in s)].append(s)
    return groups.values()
