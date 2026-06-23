#!/usr/bin/env python3
"""Test suite for hello world application."""

import unittest
from hello import hello


class TestHello(unittest.TestCase):
    """Test cases for the hello function."""

    def test_hello_output(self):
        """Test that hello() returns the correct greeting."""
        self.assertEqual(hello(), "Hello, World!")

    def test_hello_type(self):
        """Test that hello() returns a string."""
        self.assertIsInstance(hello(), str)


if __name__ == "__main__":
    unittest.main()
