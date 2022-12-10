from functools import reduce
from functional import seq


def for_loop(data: list[int]) -> int:
    sum = 0
    for datum in data:
        sum += datum * 2
    return sum


def map_reduce(data):
    reduce(lambda a, b: a + b, map(lambda n: n * 2, data))


def comprehension(data):
    sum(datum * 2 for datum in data)


def pyfunctional(data):
    (seq(data).map(lambda n: n * 2).reduce(lambda a, b: a + b))

data = range(1000)

def test_for_loop(benchmark):
    benchmark(for_loop, data)

def test_mapreduce(benchmark):
    benchmark(map_reduce, data)

def test_comprehension(benchmark):
    benchmark(comprehension, data)

def test_pyfunctional(benchmark):
    benchmark(pyfunctional, data)
