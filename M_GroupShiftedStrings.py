# TC:O(k*n) =SC, where n be the length of strings and k be the maximum length of a string in strings

def groupStrings(self, strings):
    groups = collections.defaultdict(list)
    for s in strings:
        groups[tuple((ord(c) - ord(s[0])) % 26 for c in s)] += s,
    return groups.values()
