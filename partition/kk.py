import heapq
try:
    from Queue import LifoQueue
except ImportError:
    from queue import LifoQueue
import sys

def kk(number_list, group_len=2): # Karmarkar-Karp heuristic
    if group_len != 2:
        sys.exit("unsupported group length: %s for KK algorithm!" % group_len)
    pairs = LifoQueue()
    group1, group2 = [], []
    heap = [(-1*i, i) for i in number_list]
    heapq.heapify(heap)
    while len(heap) > 1:
        i, labeli = heapq.heappop(heap)
        j, labelj = heapq.heappop(heap)
        pairs.put((labeli, labelj))
        heapq.heappush(heap, (i-j, labeli))
    group1.append(heapq.heappop(heap)[1])
    
    while not pairs.empty():
        pair = pairs.get()
        if pair[0] in group1:
            group2.append(pair[1])
        elif pair[0] in group2:
            group1.append(pair[1])
    return [group1, group2]