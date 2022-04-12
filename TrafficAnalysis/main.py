import numpy as np
from scapy.all import *
import matplotlib.pyplot as plt
import statistics


def plot_intervals(arr, amount):
    counts, bins, bars = plt.hist(arr, bins=amount)
    plt.xlabel("Interval")
    plt.ylabel("Amount")

    step = float(max(arr) / amount)
    end = int(max(arr) + 1)
    plt.xticks(np.arange(0, end, step=step))
    plt.show()
    plt.clf()
    plt.cla()
    plt.close()

    return counts, bins


def calculate_covert_channel_probability(counts, bins, avg_val):
    max_val_count = max(counts)
    avg_val_count = 0

    for index in range(len(bins)):
        if bins[index] <= avg_val:
            avg_val_count = counts[index]

    return 1 - (avg_val_count / max_val_count)


def decode_message_from_covert_channel(arr, divide):
    bits = []

    for elem in arr:
        if elem < divide:
            bits.append(0)
        else:
            bits.append(1)

    bytes_res = [sum([byte[7 - b] << b for b in range(0, 8)])
                 for byte in zip(*(iter(bits),) * 8)]

    res = ""
    for byte in bytes_res:
        res += chr(byte)

    return res

    # some_cc_ez_2_dtct


def get_intervals(start_index):
    scapy_cap = rdpcap('1.pcapng')

    prev_time = 0

    intervals = []
    i = 0
    for packet in scapy_cap:

        if i >= start_index:
            intervals.append(packet.time - prev_time)

        prev_time = packet.time

        i += 1

    return intervals


if __name__ == "__main__":
    # First task

    intervals = get_intervals(1)

    counts, bins = plot_intervals(intervals, 10)

    avg_val = statistics.mean(intervals)

    print("PROBABILITY : {0}".format(calculate_covert_channel_probability(counts, bins, avg_val)))

    # Second task

    intervals = get_intervals(100)

    counts, bins = plot_intervals(intervals, 10)

    avg_val = statistics.mean(intervals)

    print("PROBABILITY : {0}".format(calculate_covert_channel_probability(counts, bins, avg_val)))

    print("DECODED : {0}".format(decode_message_from_covert_channel(intervals, 1.5)))
