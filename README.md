<p align="center">
	<img alt="madge" src="https://github.com/slxiao/partition/blob/master/logo.png" width="200">
</p>

<p align="center">
	<img alt="Last version" src="https://img.shields.io/github/tag/slxiao/partition.svg?style=flat-square" />
	<a href="https://travis-ci.org/slxiao/partition">
		<img alt="Build Status" src="http://img.shields.io/travis/slxiao/partition/master.svg?style=flat-square" />
	</a>
	<a href="https://pypi.org/project/partition/">
		<img alt="Python Version" src="https://img.shields.io/pypi/pyversions/partition.svg" />
	</a>
	<a href="https://coveralls.io/github/slxiao/partition?branch=master">
		<img alt="Coverage" src="https://coveralls.io/repos/github/slxiao/partition/badge.svg?branch=master" />
	</a>
	<a href="https://pepy.tech/project/partition">
		<img alt="Downloads" src="https://pepy.tech/badge/partition" />
	</a>
</p>

# partition
```partiton` is a Python algorithm library which provides efficient algorithms for the [number partition problem](https://en.wikipedia.org/wiki/Partition_problem). You can also use it from shell command. These algorithms have many applications. One typical one is for [parallel software testing](https://mp.weixin.qq.com/s/oq3-mJ7cA6f_lK0SviMVyw). Currently, the following three algorithms are supported:
- greedy algorithm, which is a benchmark algorithm with simple login
- differencing algorithm, a.k.a. Karmarkar–Karp(KK) algorithm
- dynamic programming(DP) algorithm, which is optimal for scenarios where the size of integers is not too large

# Install
Use pip:
```shell
pip install partition
```
From source code:
```shell
python setup.py develop
```
# How to use
## command line usage
Get help:
```shell
partition -h
```
Query version:
```shell
partition --version
```
Available options:
```shell
usage: partition [-h] [--numbers NUMBERS] [--grouplen GROUPLEN]
                 [--algorithm {greedy,kk,dp}] [--version]

optional arguments:
  -h, --help            show this help message and exit
  --numbers NUMBERS     integer numbers to be partitioned, seperated by comma
  --grouplen GROUPLEN   length of groups to hold the partitioned integer
                        numbers, default is 2
  --algorithm {greedy,kk,dp}
                        select partition algorithms, available options are
                        greedy, kk and dp
  --version             print version
```
For example:
```shell
root@foo:~# partition --numbers 1,2,3,4,5 --grouplen 2 --algorithm greedy
Partition 1,2,3,4,5 into 2 groups, using algorithm: greedy
Group: 0, numbers: [5, 2, 1]
Group: 1, numbers: [4, 3]
Min group sum: 7, Max group sum: 8, difference: 1
Group(s) with min sum: [4, 3]
Group(s) with max sum: [5, 2, 1]
([[5, 2, 1], [4, 3]], 1)
```

## python library usage
```python
In [1]: import partition

In [2]: partition.partition.__version__
Out[2]: '0.1.0'

In [3]: partition.greedy.greedy([1,2,3,4,5], 2)
Out[3]: [[5, 2, 1], [4, 3]]

In [4]: partition.kk.kk([1,2,3,4,5], 2)
Out[5]: [[5, 3], [1, 2, 4]]
```

# Lisense
MIT
# Maintenance
This tool is developed by [slxiao](https://github.com/slxiao). You are welcome to raise any [issues](https://github.com/slxiao/partition/issues) about the tool.