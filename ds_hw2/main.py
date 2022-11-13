from MergeSort import merge_sort
from InsertionSort import insertion_sort
from CountingSort import counting_sort
from RandomizedQuickSort import lomuto, hoare, three_ways
from random import randint
from time import time
from utils import plot_multi, average_time


k_s = range(15, 19)
n_repeat = 2


def test(algorithm, k_s, name: str) -> list:
    """
    param algorithm: the sorting algorithm we want to test
    param k_s: the range function for 2^k (15 < k < 30)
    """
    time_spent = []
    print(f"testing for {name}...")
    for k in k_s:
        to_test = [randint(1, 1000) for _ in range(2**k)]
        start = time()
        if name in {"lomuto", "hoare", "three_ways"}:
            sorted_list = algorithm(to_test, 0, len(to_test)-1)
        else:
            sorted_list = algorithm(to_test)
        used_time = time() - start
        time_spent.append(used_time)
        print(f"...total time spent (k={k}): {used_time}")
    print()
    return time_spent


def trials(algorithm, n_repeat: int, name: str, k_s) -> list[list]:
    return [test(algorithm=algorithm, k_s=k_s, name=name) for _ in range(n_repeat)]


if __name__ == "__main__":
    
    time_spent_1 = average_time(trials(algorithm=merge_sort, n_repeat=n_repeat, k_s=k_s, name="merge sort"), n_repeat, "merge sort", k_s)
    time_spent_2 = average_time(trials(algorithm=counting_sort, n_repeat=n_repeat, k_s=k_s, name="counting sort"), n_repeat, "counting sort", k_s)
    time_spent_3 = average_time(trials(algorithm=three_ways, n_repeat=n_repeat, k_s=k_s, name="three_ways"), n_repeat, "three ways", k_s)
    time_spent_4 = average_time(trials(algorithm=hoare, n_repeat=n_repeat, k_s=k_s, name="hoare"), n_repeat, "hoare", k_s)
    time_spent_5 = average_time(trials(algorithm=lomuto, n_repeat=n_repeat, k_s=k_s, name="lomuto"), n_repeat, "lomuto", k_s)
    time_spent_6 = average_time(trials(algorithm=insertion_sort, n_repeat=n_repeat, k_s=k_s, name="insertion sort"), n_repeat, "insertion sort", k_s)
    plot_multi(time_spent_1, time_spent_2, time_spent_3, time_spent_4, time_spent_5, time_spent_6, k_s, "sorting comparision.png")
