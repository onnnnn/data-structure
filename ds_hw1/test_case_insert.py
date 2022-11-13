from linked_list_new import LinkedList
from dynamic_array import DynamicArray
from utils import plot_single, plot_multi, average_time
from time import time
from random import randint
import sys


# default testing parameters
k_s = range(15, 26)
n_repeat = 5


def test_linked_list(k_s) -> list[float]:
    """
    test Linked List performance (time spent) in different k.

    param k_s: range function for k
    """

    time_spent = []   # store how much will take for append 2^k elements
    print("testing for Linked List:")
    for k in k_s:   # k to use
        linked_list = LinkedList()   # create a new linked list structure for every k
        to_test = [randint(1,20) for _ in range(2**k)]   # generate 2^k random numbers
        start_time = time()   # started time to add items into linked list
        for ele in to_test:
            linked_list.insert(ele)
        used_time = time() - start_time   # used time will be current time - started time
        time_spent.append(used_time)   # keep tracking used time for every k
        print(f"\t total time spent (k={k}): {used_time}")
    print()
    return time_spent


def test_dynamic_array(k_s) -> list[float]:
    """
    test Dynamic Array performance (time spent) in different k.

    param k_s: range function for k
    """

    time_spent = []
    print("testing for Dynamic Array:")
    for k in k_s:
        dynamic_array = DynamicArray()
        to_test = [randint(1,20) for _ in range(2**k)]
        start_time = time()
        for ele in to_test:
            dynamic_array.append(ele)
        used_time = time() - start_time
        time_spent.append(used_time)
        print(f"\t total time spent (k={k}): {used_time}")
    print()
    return time_spent


def trials(n_repeat:int, which:int, k_s=k_s) -> list[list]:
    """
    repeat trials n times to get average results then return in list of lists.
    
    param n_repeat: how many time to repeat
    param which: 1 for linked list, 2 for dynamic array
    """

    assert which in (1, 2), "`which` has to be either 1 or 2"
    if which == 1:
        return [test_linked_list(k_s) for _ in range(n_repeat)]
    elif which == 2:
        return [test_dynamic_array(k_s) for _ in range(n_repeat)]


if __name__ == "__main__":

    assert len(sys.argv) == 2, "must give `single` or `average` as argv"

    if sys.argv[1] == "average":
        print("running multi test...")
        all_time_spent_linked_list = trials(n_repeat, 1)
        mean_time_linked_list = average_time(all_time_spent_linked_list, n_repeat, "linked list", k_s)
        
        all_time_spent_dynamic_array = trials(n_repeat, 2)
        mean_time_dynamic_array = average_time(all_time_spent_dynamic_array, n_repeat, "dynamic array", k_s)

        plot_single(mean_time_linked_list, k_s, title="linked list", path="/img/linked_list_insert.png")
        plot_single(mean_time_dynamic_array, k_s, title="dynamic array", path="/img/dynamic_array_insert.png")
        plot_multi(mean_time_linked_list, mean_time_dynamic_array, k_s, path="/img/multi_insert.png")

    elif sys.argv[1] == "single":
        print("running only one test...")
        time_linked_list = test_linked_list(k_s)
        time_dynamic_array = test_dynamic_array(k_s)

        plot_single(time_linked_list, k_s, title="linked list", path="/img/linked_list_insert.png")
        plot_single(time_dynamic_array, k_s, title="dynamic array", path="/img/dynamic_array_insert.png")
        plot_multi(time_linked_list, time_dynamic_array, k_s, path="/img/multi_insert.png")