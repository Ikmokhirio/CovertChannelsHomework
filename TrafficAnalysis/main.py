from scapy.all import *
import matplotlib.pyplot as plt
import statistics


def plot_shit(arr, amount):
    plt.hist(arr, bins=amount)
    plt.show()


def calculate_probability(arr):
    avg_val = statistics.mean(arr)
    max_val = max(arr)

    print(max_val, avg_val)

    return 1 - (avg_val / max_val)


def decode(arr, divide):
    bits = []

    for elem in arr:
        if elem < divide:
            # print("0", end="")
            bits.append(0)
        else:
            # print("1", end="")
            bits.append(1)

    bytes_res = [sum([byte[7 - b] << b for b in range(0, 8)])
                 for byte in zip(*(iter(bits),) * 8)]

    res = ""
    for byte in bytes_res:
        res += chr(byte)

    print(res)

    # some_cc_ez_2_dtct

def first_task():


if __name__ == "__main__":
    scapy_cap = rdpcap('1.pcapng')

    is_first = True
    prev_time = 0

    intervals = []
    i = 0
    for packet in scapy_cap:

        if i >= 100:
            intervals.append(packet.time - prev_time)

        prev_time = packet.time

        i += 1

    # plot_shit(intervals, 10)

    # print("PROBABILITY {0} : ".format(calculate_probability(intervals)))

    decode(intervals, 1.5)
