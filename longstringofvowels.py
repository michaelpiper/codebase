def longstringofvowels(string):
    result =0
    found =[]
    vowel = ['a','e','i','o','u']
    for i in range(0,len(string)):
        if string[i] in vowel and string[i] not in found:
            result += 1
            found.append(string[i])
    return found
def maxlen(strings):
    if not strings: return 0
    return max([len(s) for s in strings])


def vowelsonly(s):
    parts = []
    current = []

    for i, char in enumerate(s):
        if char in 'aeiou':
            current.append(char)
        else:
            if current:
                parts.append(''.join(current))
            current = []

    # last remaining
    if current: parts.append(''.join(current))

    best = float('-inf')

    # if vowel substring is at front and end, aaaBBaaaBBaaa
    # we could consider front, 1 middle, end which makes 3 elements
    if len(parts) > 1 and s.startswith(parts[0]) and s.endswith(parts[-1]):
        best = max(best, len(parts[0]) + len(parts[-1]) + maxlen(parts[1:-1]))

    # if vowel substring is at front only, aaaBBaaBBaaaBB,
    # we could consider front, 1 middle which is 2 elements only
    if len(parts) > 1 and s.startswith(parts[0]):
        best = max(best, len(parts[0]) + maxlen(parts[1:]))

    # if vowel substring is at the end, BBaaBBaaa,
    # we could consider 1 middle, end which makes 2 elements only
    if len(parts) > 1 and s.endswith(parts[-1]):
        best = max(best, len(parts[-1]) + maxlen(parts[:-1]))

    # if substring does not happen at front or end, BBaaaBBBaaaaBBB,
    #   we could consider 1 middle only
    best = max(best, maxlen(parts))

    return best


string = "earthproblem"
result = longstringofvowels(string)
print(result)
print(vowelsonly(string))
