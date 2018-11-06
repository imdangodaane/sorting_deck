#!/usr/bin/env python3
import argparse


def swap_next(pos, lst):
    lst[pos], lst[pos + 1] = lst[pos + 1], lst[pos]


def bubble_sort(lst):
    for _ in lst:
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                swap_next(i, lst)
                print(' '.join(str(x) for x in lst))


def insert_sort(lst):
    # Insertion Sort Type I
    # sorted_list = [] + lst[0]
    # for i in range(1, len(lst)):
    #     for j in range(len(sorted_list)):
    #         if lst[i] < sorted_list[j]:
    #             sorted_list.insert(j, lst[i])
    #             print(sorted_list)
    #             break

    # Insertion Sort Type II
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            for j in range(i + 1):
                if lst[i + 1] <= lst[j]:
                    lst.insert(j, lst[i + 1])
                    del(lst[i + 2])
                    print(' '.join(str(x) for x in lst))
                    break


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print('P:', pivot)
    print(' '.join(str(x) for x in arr))
    return (i + 1)


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


def merge_sort(lst):
    if len(lst) > 1:
        m = int(len(lst)/2)
        L = lst[:m]
        R = lst[m:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1
        print(' '.join(str(x) for x in lst))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('N', nargs='+', action='store', type=int,
                        help='an integer for the list to sort')
    parser.add_argument('--algo', metavar='ALGO', default='bubble',
                        help='specify which algorithm to use for sorting among\
                        [bubble|insert|quick|merge], default bubble')
    parser.add_argument('--gui', action='store_true',
                        help='visualise the algorithm in GUI mode')
    args = parser.parse_args()

    if args.algo == 'bubble':
        bubble_sort(args.N)
    elif args.algo == 'insert':
        insert_sort(args.N)
    elif args.algo == 'quick':
        quick_sort(args.N, 0, len(args.N) - 1)
    elif args.algo == 'merge':
        merge_sort(args.N)


if __name__ == '__main__':
    main()
