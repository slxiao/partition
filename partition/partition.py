import sys

from . import argument
from . import greedy 
from . import kk
from . import dp
from . import __version__

def partition(args=None):
    parser = argument.get_parser()
    args = parser.parse_args(args)
    if args.version:
        print("partition v" + __version__)
        return args.version

    number_list = [int(i) for i in args.numbers.split(",")]

    if args.algorithm == "greedy":
        groups = greedy.greedy(number_list, args.grouplen)
    elif args.algorithm == "kk":
        groups = kk.kk(number_list, args.grouplen)
    elif args.algorithm == "dp":
        #TODO: fix the dp algorithm bug
        groups = dp.dp(number_list, args.grouplen)
    else:
        sys.exit("unsupported partition algorithm: %s" % args.algorithm)
    print("Partition %s into %s groups, using algorithm: %s" % (args.numbers, args.grouplen, args.algorithm))
    min_groupsum = min([sum(i) for i in groups])
    max_groupsum = max([sum(i) for i in groups])
    min_groupsum_indices, max_groupsum_indices = [], []
    for i in range(len(groups)):
        print("Group: %s, numbers: %s"%(i, groups[i]))
        if sum(groups[i]) == min_groupsum:
            min_groupsum_indices.append(i)
        if sum(groups[i]) == max_groupsum:
            max_groupsum_indices.append(i)
    print("Min group sum: %s, Max group sum: %s, difference: %s" % (min_groupsum, max_groupsum, max_groupsum-min_groupsum))
    print("Group(s) with min sum: %s" % ",".join([str(groups[i]) for i in min_groupsum_indices]))
    print("Group(s) with max sum: %s" % ",".join([str(groups[i]) for i in max_groupsum_indices]))
    return groups, max_groupsum-min_groupsum

if __name__ == "__main__":
    partition()