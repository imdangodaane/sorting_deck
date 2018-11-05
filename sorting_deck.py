#!/usr/bin/env python3
import argparse


def swap_next(pos, lst):
    temp = lst[pos + 1]
    lst[pos + 1] = lst[pos]
    lst[pos] = temp


def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                swap_next(j, lst)
                j += 1
                print(lst)


def insertion_sort(lst):
    pass


def quick_sort(lst):
    pass


def merge_sort(lst):
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('N', nargs='+', action='store', type=int, help='an integer for the list to sort')
    parser.add_argument('--algo', metavar='ALGO', default='bubble', help='specify which algorithm to use for sorting among [bubble|insert|quick|merge], default bubble')
    parser.add_argument('--gui', action='store_true', help='visualise the algorithm in GUI mode')
    args = parser.parse_args()

    if args.algo == 'bubble':
        bubble_sort(args.N)
    elif args.algo == 'insert':
        insertion_sort(args.N)
    elif args.algo == 'quick':
        quick_sort(args.N)
    elif args.algo == 'merge':
        merge_sort(args.N)


if __name__ == '__main__':
    main()
