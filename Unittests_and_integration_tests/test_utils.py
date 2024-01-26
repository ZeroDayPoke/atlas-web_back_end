#!/usr/bin/env python3
"""utils testing module"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""
    @parameterized.expand([
        ({"i": 1}, ["i"], 1),
        ({"j": {"k": 2}}, ["j", "k"], 2),
        ({"i": {"j": {"k": 3}}}, ["i", "j"], {"k": 3}),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test_access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({"a": 1}, ["b"]),
        ({"a": {"b": 2}}, ["a", "c"]),
        ({"a": 1}, ["a", "b"]),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test_access_nested_map_exception"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertIn(str(path[-1]), str(context.exception))


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """test_get_json"""
        with patch('requests.get') as mocked_get:
            mocked_get.return_value = MagicMock(json=lambda: test_payload)

            result = get_json(test_url)

            mocked_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """TestMemoize class"""
    def test_memoize(self):

        class TestClass:
            """TestClass class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass,
                          'a_method', return_value=42) as mock_method:
            test = TestClass()

            result_the_first = test.a_property
            result_the_second = test.a_property

            self.assertEqual(result_the_first, 42)
            self.assertEqual(result_the_second, 42)

            mock_method.assert_called_once()
