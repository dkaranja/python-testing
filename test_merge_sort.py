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
        sorted_list = MergeSort().divide_conquer(test_case)
        self.assertEqual(expected, sorted_list)

    #   test one element
    def test_one_element(self):
        test_case = [10]
        expected = [10]
        algo_result = MergeSort().divide_conquer(test_case)
        self.assertEqual(expected, algo_result)





