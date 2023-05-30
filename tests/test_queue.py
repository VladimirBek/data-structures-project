"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):

    def test_enqueue(self):
        q1 = Queue()
        q1.enqueue(1)
        self.assertEqual(q1.head.data, 1)
        q1.enqueue(2)
        self.assertEqual(q1.tail.data, 2)
        self.assertEqual(q1.head.data, 1)
        q1.enqueue(3)
        self.assertEqual(q1.head.next_node.data, 2)
        self.assertEqual(q1.tail.data, 3)
        self.assertEqual(q1.head.data, 1)

    def test_str(self):
        q1 = Queue()
        q1.enqueue(1)
        q1.enqueue(2)
        q1.enqueue(3)
        self.assertEqual(str(q1), '1\n2\n3')
        q1.enqueue(4)
        self.assertEqual(str(q1), '1\n2\n3\n4')
