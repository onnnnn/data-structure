import matplotlib.pyplot as plt


def plot_single(time_spent:list[float], k_s:range, title:str, path:str):
    """
    plot data structure time spent among each k.

    param time_spent: time spent of the data sturcture
    param k_s: range function for k
    param title: figure title, usually the name of the data sturcture
    param path: where you want your figure saved with figure name
    """
    
    plt.title(title)
    plt.plot(list(k_s), time_spent)
    plt.ylabel("total time spent")
    plt.xlabel("2^k")
    plt.savefig(path)
    print(f"figure saved in(as) {path}")
    plt.show()


def plot_multi(
    time_spent_1:list[float], 
    time_spent_2:list[float], 
    time_spent_3:list[float], 
    time_spent_4:list[float], 
    time_spent_5:list[float], 
    time_spent_6:list[float], 
    k_s:range, path:str):
    """
    plot two data structures time spent among each k in one figure.

    param time_spent_1: time spent of the data sturcture 1
    param time_spent_2: time spent of the data structure 2
    param k_s: range function for k
    param path: where you want your figure saved with figure name
    """

    plt.title("")
    plt.plot(list(k_s), time_spent_1)
    plt.plot(list(k_s), time_spent_2)
    plt.plot(list(k_s), time_spent_3)
    plt.plot(list(k_s), time_spent_4)
    plt.plot(list(k_s), time_spent_5)
    plt.plot(list(k_s), time_spent_6)
    plt.ylabel("total time spent")
    plt.xlabel("2^k")
    plt.legend(["merge sort", "counting sort", "three ways", "hoare", "lomuto", "insertion sort"])
    plt.savefig(path)
    print(f"figure saved in(as) {path}")
    plt.show()


def average_time(all_time_spent:list[list], n_repeat:int, name:str, k_s:range) -> list[float]:
    """
    count average spent time in n repeat then return in list.

    param all_time_spent: list contains list of testing time
    param n_repeat: how many time to repeat
    param name: name this data structure
    param k_s: range function for k
    """

    mean_time = []
    for i in range(len(all_time_spent[0])):
        _sum = 0
        for each in all_time_spent:
            _sum += each[i]
        mean = _sum / n_repeat
        mean_time.append(mean)
        print(f"{name} (k={k_s[i]}) mean time: {mean}")
    print()
    return mean_time
