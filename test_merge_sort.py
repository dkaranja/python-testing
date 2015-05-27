#!/usr/bin/python
from unittest import TestCase
from merge_sort import MergeSort


class MergeSortDivideConquerTest(TestCase):

    #   test an empty list
    def test_empty_list(self):
        test_case = []
        expected = []
        algo_result = MergeSort().divide_conquer(test_case)
        self.assertEqual(expected, algo_result)

    #   test one element
    def test_one_element(self):
        test_case = [10]
        expected = [10]
        algo_result = MergeSort().divide_conquer(test_case)
        self.assertEqual(expected, algo_result)

    #   test list with two unsorted elements
    def test_two_unsorted_elements(self):
        test_case = [100, -2]
        expected = [-2, 100]
        algo_result = MergeSort().divide_conquer(test_case)
        self.assertEqual(expected, algo_result)

    #   test list with two sorted elements
    def test_two_sorted_elements(self):
        test_case = [3, 10]
        expected = [3, 10]
        algo_result = MergeSort().divide_conquer(test_case)
        self.assertEqual(expected, algo_result)

    #   test with 5 unsorted elements
    def test_five_unsorted_elements(self):
        test_case = [20, -3, 2, 40, -10]
        expected = [-10, -3, 2, 20, 40]
        algo_result = MergeSort().divide_conquer(test_case)
        self.assertEqual(expected, algo_result)

    #   test with 5 sorted elements
    def test_five_sorted_elements(self):
        test_case = [1, 5, 7, 8, 9]
        expected = [1, 5, 7, 8, 9]
        algo_result = MergeSort().divide_conquer(test_case)
        self.assertEqual(expected, algo_result)

    #   test many elements
    def test_many_elements(self):
        test_case = [1, 20, 3, 0, -2, 10, 4, 20, 34, 45, 45, 65]
        expected = [-2, 0, 1, 3, 4, 10, 20, 20, 34, 45, 45, 65]
        algo_result = MergeSort().divide_conquer(test_case)
        self.assertEqual(expected, algo_result)

    #   test for negative numbers
    def test_negative_numbers(self):
        test_case = [-1, -20, -40, -20, -3, -34, -45]
        expected = [-45, -40, -34, -20, -20, -3, -1]
        algo_result = MergeSort().divide_conquer(test_case)
        self.assertEqual(expected, algo_result)

    #   test divide_conquer param
    def test_divide_conquer_param_is_list(self):
        test_case = type([8])
        expected = type(list)
        algo_result = MergeSort().divide_conquer(test_case)
        self.assertEqual(expected, algo_result)


class MergeSortMergeTest(TestCase):

    #   test when both lists are empty
    def test_two_empty_lists(self):
        test_list_one = []
        test_list_two = []

        expected = []
        algo_result = MergeSort().merge(test_list_one, test_list_two)
        self.assertEqual(expected, algo_result)

    #   test when list_one is empty
    def test_when_list_one_is_empty(self):
        list_one = []
        list_two = [7, 90]

        expected = [7, 90]
        algo_result = MergeSort().merge(list_one, list_two)
        self.assertEqual(expected, algo_result)

    #   test when list two is empty
    def test_when_list_two_is_empty(self):
        list_one = [1, 3, 7]
        list_two = []

        expected = [1, 3, 7]
        algo_result = MergeSort().merge(list_one, list_two)
        self.assertEqual(expected, algo_result)

    #   test when both lists have data
    def test_when_both_lists_have_data(self):
        list_one = [8, 9, 20, 34]
        list_two = [3, 8, 10, 23, 39, 40]

        expected = [3, 8, 8, 9, 10, 20, 23, 34, 39, 40]
        algo_result = MergeSort().merge(list_one, list_two)
        self.assertEqual(expected, algo_result)











