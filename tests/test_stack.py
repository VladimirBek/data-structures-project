"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack
class TestStack(unittest.TestCase):

    def test_push(self):
        s1 = Stack()
        s1.push(1)
        self.assertEqual(s1.top.data, 1)
        s1.push(2)
        self.assertEqual(s1.top.data, 2)
        self.assertEqual(s1.top.next_node.data, 1)
        self.assertIsNone(s1.top.next_node.next_node)
