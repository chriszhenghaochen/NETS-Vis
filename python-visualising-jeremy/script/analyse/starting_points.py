import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import data


def get_end_point_per_day(day):
    df = data.read_data(day)
    first = df.groupby('id').first().groupby(['X', 'Y']).size()
    last = df.groupby('id').last().groupby(['X', 'Y']).size()
    return first, last


def get_end_point_totals():
    first = None
    last = None
    for day in ['Fri', 'Sat', 'Sun']:
        print(day)
        first2, last2 = get_end_point_per_day(day)
        if first is None:
            first = first2
        else:
            first = first.add(first2, fill_value=0)
        if last is None:
            last = last2
        else:
            last = last.add(last2, fill_value=0)
    return first, last


def get_end_key_points(day):
    df = data.read_visited_key_points(day)
    first = df.groupby('id').first().groupby('place_id').size()
    last = df.groupby('id').first().groupby('place_id').size()
    return first, last


def get_end_key_point_totals():
    first = None
    last = None
    for day in ['Fri', 'Sat', 'Sun']:
        print(day)
        first2, last2 = get_end_key_points(day)
        if first is None:
            first = first2
        else:
            first = first.add(first2, fill_value=0)
        if last is None:
            last = last2
        else:
            last = last.add(last2, fill_value=0)
    return first, last


def main():
    # first, last = get_end_point_totals()
    # print(first)
    # print(last)
    first, last = get_end_key_point_totals()
    print(first)
    print(last)

if __name__ == '__main__':
    main()
