import argparse

def get_parser():

    parser = argparse.ArgumentParser()

    parser.add_argument("--numbers", help="integer numbers to be partitioned, seperated by comma")

    parser.add_argument("--grouplen", type=int, help="length of groups to hold the partitioned integer numbers, default is 2", default=2)

    parser.add_argument("--algorithm", help="select partition algorithms, available options are greedy, kk and dp", choices=["greedy", "kk", "dp"])

    parser.add_argument("--version", action='store_true', help="print version")

    return parser