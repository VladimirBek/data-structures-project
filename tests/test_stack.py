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

    def test_pop(self):
        s1 = Stack()
        s1.push(1)
        data = s1.pop()
        self.assertIsNone(s1.top)
        self.assertEqual(data, 1)
        self.assertRaises(IndexError, s1.pop)

    def test_str(self):
        s1 = Stack()
        s1.push(1)
        s1.push(2)
        s1.push(3)
        self.assertEqual(str(s1), '1\n2\n3')
        s1.pop()
        self.assertEqual(str(s1), '1\n2')
        s1.pop()
        self.assertEqual(str(s1), '1')
        s1.pop()
        self.assertEqual(str(s1), '')
