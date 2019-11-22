def greedy(number_list, group_len=2):
    groups = [[] for i in range(group_len)]
    for i in sorted(number_list, reverse=True):
        groups.sort(key=lambda x: sum(x))
        groups[0].append(i)
    return groups