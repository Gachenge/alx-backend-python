#!/usr/bin/env python3
"""unittests to test utils"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize

class TestAccessNestedMap(unittest.TestCase):
    """class that inherits from unittest.Testcase to test nested map function"""
    @parameterized.expand([
        # Test case 1
        [{"a": 1}, ("a",), 1],
        # Test case 2
        [{"a": {"b": 2}}, ("a",), {"b": 2}],
        # Test case 3
        [{"a": {"b": 2}}, ("a", "b"), 2]
    ])
             
    def test_access_nested_map(self, nested_map, path, expected_result):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        [{}, ("a",), KeyError],
        [{"a": 1}, ("a", "b"), KeyError]
    ])

    def test_access_nested_map_exception(self, nested_map, path, expected_result):
        with self.assertRaises(expected_result) as context:
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """test json request to api"""
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    def test_get_json(self, json, expected):
        mock = Mock()
        mock.json.return_value = expected
        with patch('requests.get', return_value=mock):
            self.assertEqual(get_json(json), expected)

class TestMemoize(unittest.TestCase):
    """memoization with utils.memoize decorator"""
    def test_memoize(self):
        """implement class testclass"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
            
        test = TestClass()
        with patch.object(test, 'a_method') as mock:
            mock.return_value = 42

            res = test.a_property
            resi = test.a_property
            self.assertEqual(res, 42)
            self.assertEqual(resi, 42)
            mock.assert_called_once()
