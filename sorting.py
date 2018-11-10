#!/usr/bin/env python3
import pyglet
import argparse
import time
from math import sqrt


def swap_next(pos, lst):
    lst[pos], lst[pos + 1] = lst[pos + 1], lst[pos]


def bubble_sort(lst):
    for _ in lst:
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                swap_next(i, lst)
                print(' '.join(str(x) for x in lst))
                #
            _list.append(list(lst))
            cmp_ele.append((lst[i], lst[i+1]))


def insert_sort(lst):
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
    global _list, cmp_ele, display_list
    _list = []
    cmp_ele = []
    parser = argparse.ArgumentParser()
    parser.add_argument('N', nargs='+', action='store', type=int,
                        help='an integer for the list to sort')
    parser.add_argument('--algo', metavar='ALGO', default='bubble',
                        help='specify which algorithm to use for sorting among\
                        [bubble|insert|quick|merge], default bubble')
    parser.add_argument('--gui', action='store_true',
                        help='visualise the algorithm in GUI mode')
    args = parser.parse_args()

    display_list = list(args.N)
    # Sorting
    if args.algo == 'bubble':
        bubble_sort(args.N)
    elif args.algo == 'insert':
        insert_sort(args.N)
    elif args.algo == 'quick':
        quick_sort(args.N, 0, len(args.N) - 1)
    elif args.algo == 'merge':
        merge_sort(args.N)


##############################################################################
display_list = []
main()
##############################################################################
speed = 0.2
##############################################################################
# Making window
platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_default_screen()
gui_window = pyglet.window.Window(width=screen.width,
                                  height=screen.height,
                                  resizable=True,
                                  caption='Sorting GUI')
numb_batch = pyglet.graphics.Batch()
f_size = int(sqrt(gui_window.width * 2 + gui_window.height * 2))
pos_x = f_size
for m in range(len(display_list)):
    pyglet.text.Label(str(display_list[m]),
                      font_size=f_size,
                      anchor_x='center',
                      font_name='Times New Roman',
                      x=pos_x, y=gui_window.height * 2/4,
                      batch=numb_batch)
    pos_x += gui_window.width // len(display_list)
# Reindex resource path
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

# i = 0
# labels = []
# def update(dt):
#     global i
#     if i < len(display_list):
#         # Making labels
#         pos_x = (gui_window.width // len(display_list[i])) // 3
#         for j in range(len(display_list[i])):
#             label = pyglet.text.Label(str(display_list[i][j]),
#                                       font_size=(gui_window.width // len(display_list[i])) // 3,
#                                       anchor_x='center',
#                                       x=pos_x, y=gui_window.height // 2.3)
#             if i > 0 and display_list[i][j] != display_list[i-1][j]:
#                 label.color = (0, 255, 0, 255)
#             labels.append(label)
#             pos_x += gui_window.width // len(display_list[i])
#         i += 1


cmp_count = 0
swap_count = 0
labels = []
cmp_label = None
swap_label = None
i = 0


def update(dt):
    global i, labels, cmp_count, swap_count, cmp_label, swap_label
    if i < len(_list):
        cmp_count += 1
        cmp_label = pyglet.text.Label('Compares : ' + str(cmp_count),
                                      font_size=f_size,
                                      font_name='Times New Roman',
                                      y=gui_window.height * 7/8)
        # Making labels
        pos_x = f_size
        for j in range(len(_list[i])):
            label = pyglet.text.Label(str(_list[i][j]),
                                      font_size=f_size,
                                      font_name='Times New Roman',
                                      anchor_x='center',
                                      x=pos_x, y=gui_window.height * 1/4)
            if i > 0 and _list[i][j] != _list[i-1][j]:
                label.color = (255, 0, 0, 255)
                swap_count += 1
                swap_label = pyglet.text.Label('Swap : ' + str(swap_count // 2 + 1),
                                               font_size=f_size,
                                               font_name='Times New Roman',
                                               y=gui_window.height * 3/4)
            elif _list[i][j] in cmp_ele[i]:
                label.color = (0, 255, 0, 255)
            labels.append(label)
            pos_x += gui_window.width // len(_list[i])
        i += 1

@gui_window.event
def on_draw():
    global labels, cmp_label, swap_label
    if len(labels) > 0:
        gui_window.clear()
        numb_batch.draw()
        cmp_label.draw()
        for _ in range(len(labels)):
            labels[_].draw()
    if swap_label:
        swap_label.draw()
    numb_batch.draw()
    labels = []


pyglet.clock.schedule_interval(update, speed)
pyglet.app.run()
