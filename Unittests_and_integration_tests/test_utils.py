#!/usr/bin/env python3
"""utils testing module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""
    @parameterized.expand([
        ({"i": 1}, ["i"], 1),
        ({"j": {"k": 2}}, ["j", "k"], 2),
        ({"i": {"j": {"k": 3}}}, ["i", "j"], {"k": 3}),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({"a": 1}, ["b"]),
        ({"a": {"b": 2}}, ["a", "c"]),
        ({"a": 1}, ["a", "b"]),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertIn(str(path[-1]), str(context.exception))
