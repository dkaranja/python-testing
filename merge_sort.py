#!/usr/bin/python
"""
Implments the class based merge sort algorithm
"""


class MergeSort(object):

    def divide_conquer(self, full_list):
        list_length = len(full_list)

        #   list with one item
        if list_length <= 1:
            return full_list
        else:
            mid = list_length / 2

            #   divide list into two halfs
            left_half = full_list[0:mid]
            right_half = full_list[mid:]

            #   conquer
            conquered_list_one = MergeSort().divide_conquer(left_half)
            conquered_list_two = MergeSort().divide_conquer(right_half)

        return MergeSort().merge(conquered_list_one, conquered_list_two)

