#!/usr/bin/python
from unittest import TestCase

from merge_sort import MergeSort


class MergeSortTest(TestCase):

    def setUp(self):# NOQA
        self.algo_under_test = MergeSort()

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







