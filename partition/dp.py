import math
import numpy as np
import sys

def dp(number_list, group_len=2):
    if group_len != 2:
        sys.exit("unsupported group length: %s for DP algorithm!" % group_len)

    n = len(number_list)
    k = sum(number_list)
    s = int(math.floor(k/2))
    p = np.zeros((s+1, n+1))
    p[0] = 1
    for i in range(1, s+1):
        for j in range(1, n+1):
            if i - number_list[j-1] >= 0:
                p[i][j] = p[i][j-1] or p[i-number_list[j-1]][j-1]
            else:
                p[i][j] = p[i][j-1]
    return p[s][n]