import time
import pandas as pd
import random
from collections import Counter


class Stress_Index:
    def __init__(self):
        self.RR_intervals = []
    def append_interval(self, value):
        value = round(value, 1)
        print(value)
        self.RR_intervals.append(value)
    def main_callback(self):
        self.RR_intervals.pop(0)
        Mo = Counter(self.RR_intervals).most_common()[0][0]
        AMo = Counter(self.RR_intervals).most_common()[0][1] / len(self.RR_intervals) * 100
        dRR = max(self.RR_intervals) - min(self.RR_intervals)
        SI = AMo / (2 * dRR * Mo)
        return SI


def test(time_series):
    stress_index_instance = Stress_Index()
    new_values = []
    start_time = time.time()
    previous_time = time.time()
    for value in time_series:
        current_time = time.time()
        interval = current_time - previous_time
        previous_time = current_time
        stress_index_instance.append_interval(interval)
        time.sleep(random.uniform(0.3, 3))
        if time.time() - start_time >= 300:
            stress_index = stress_index_instance.main_callback()
            new_values.append(stress_index)
            print(stress_index)
            start_time = time.time()
            stress_index_instance.RR_intervals = []
    return new_values


def alter_data(time_series):
    def alter_row(row):
        row_list = row.tolist()
        row_list.pop()
        while row_list[-1] == 0.0:
            row_list.pop()
        return row_list

    time_series = [x for xs in time_series.apply(alter_row, axis=1).tolist() for x in xs]
    return time_series


if __name__ == "__main__":
    time_series = pd.read_csv("C:/Users/svetlana/Downloads/test.csv", header=None)
    time_series = alter_data(time_series)
    test(time_series)