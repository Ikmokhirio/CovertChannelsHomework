from math import log2
import matplotlib.pyplot as plt


def get_probability_of(value, amount):
    return 1 / amount


def calculate_entropy_of_random_value(amount):
    entropy = 0.0
    for g in range(1, amount + 1):
        entropy += get_probability_of(g, amount) * log2(get_probability_of(g, amount))
    return -entropy


def calculate_time(amount):
    return (amount + 1) / 2


def calculate_bandwidth(amount):
    return calculate_entropy_of_random_value(amount) / calculate_time(amount)


if __name__ == '__main__':

    values = [[], []]

    max_value = -1
    max_value_i = -1

    for i in range(1, 25):
        values[0].append(i)
        values[1].append(calculate_bandwidth(i))

        if calculate_bandwidth(i) > max_value:
            max_value = calculate_bandwidth(i)
            max_value_i = i

    print(max_value, max_value_i)
    plt.plot(values[0], values[1])
    plt.ylabel('Bandwidth')
    plt.xlabel("Amount of values")
    plt.show()
