#!/usr/bin/python3
""" Utils testing module."""
import unittest
from parametized import parametized
from utils import (access_nested_map)

class TestAccessNestedMap(unittest.TestCase):
    """ Check Nested Map Values with Unit Tests."""
    @parametized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b" 2}}, ("a",) {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test method output is as intended."""
        self.assertEqual(access_nested_map, path), expected)
    @parametized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Check KeyError is raised for the respective inputs."""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))
