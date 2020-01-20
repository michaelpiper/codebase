import math
def rearrangestring( str, k):
    """
    :type str: str
    :type k: int
    :rtype: str
    """
    cnts = [0] * 26;
    for c in str:
        cnts[ord(c) - ord('a')] += 1

    sorted_cnts = []
    for i in range(0,26):
        sorted_cnts.append((cnts[i], chr(i + ord('a'))))
    sorted_cnts.sort(reverse=True)

    max_cnt = sorted_cnts[0][0]
    blocks = [[] for _ in range(0,max_cnt)]
    i = 0
    for cnt in sorted_cnts:
        for _ in range(0,cnt[0]):
            blocks[i].append(cnt[1])
            i = (i + 1) % max(cnt[0], max_cnt - 1)

    for i in range(0,max_cnt-1):
        if len(blocks[i]) < k:
            return ""

    return "".join(map(lambda x : "".join(x), blocks))
string="aaaabbb"
result = rearrangestring(string,2)
print(result)
    