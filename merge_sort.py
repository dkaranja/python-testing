#!/usr/bin/python
"""
Implments the class based merge sort algorithm
"""


class MergeSort(object):
    """Merge Sort implementation."""

    def divide_conquer(self, full_list):
        """Recursively dividde and conquer a list."""
        param_type = type(full_list)
        if param_type is list:
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
                conquered_list_one = self.divide_conquer(left_half)
                conquered_list_two = self.divide_conquer(right_half)

            return self.merge(conquered_list_one, conquered_list_two)
        else:
            print("{} was given, a list was expected".format(param_type))
            return param_type

    def merge(self, list_one, list_two):
        """Merge two conquered lists."""
        i, j, sorted_list = 0, 0, []
        length_one = len(list_one)
        length_two = len(list_two)

        #   while any of the list is not empty
        while(i < length_one) or (j < length_two):
            if(i < length_one) and (j < length_two):
                #   both lists have data
                if list_one[i] <= list_two[j]:
                    sorted_list.append(list_one[i])
                    i += 1
                else:
                    sorted_list.append(list_two[j])
                    j += 1
            elif i < length_one:
                #   only list one has data
                sorted_list.append(list_one[i])
                i += 1
            else:
                #   only list two has data
                sorted_list.append(list_two[j])
                j += 1
        else:
            return sorted_list


if __name__ == "__main__":
    my_list = [-2, 3, 6, 8, -20, 2, 67, 345, 2345, 34, -299]
    sort_instance = MergeSort()

    print("Before: \n {}".format(my_list))
    print("After: \n {}".format(sort_instance.divide_conquer(my_list)))



