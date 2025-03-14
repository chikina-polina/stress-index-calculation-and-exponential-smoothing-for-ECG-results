import time
import pandas as pd


class Exponential_Smoothing:
    def __init__(self, time_series, alpha=0.4):
        self.alpha = alpha
        self.time_series = time_series
        self.smooth_values = []
        self.smooth_value = 0
    def main_callback(self, value):
        if not self.smooth_values:
            self.smooth_value = sum(time_series[:10]) / 10
        else:
            self.smooth_value = self.alpha * value + (1 - self.alpha) * self.smooth_values[-1]
        self.smooth_values.append(self.smooth_value)
        return self.smooth_value


def test(time_series):
    exp_smooth_instance = Exponential_Smoothing(time_series)
    new_values = []
    for value in time_series:
        new_values.append(exp_smooth_instance.main_callback(value))
        time.sleep(0.1)
    print(new_values)
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
    time_series = pd.read_csv("test.csv", header=None)
    time_series = alter_data(time_series)
    test(time_series)