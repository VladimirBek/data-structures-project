"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList


class TestQueue(unittest.TestCase):

    def test_linked_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})
        ll.insert_beginning({'id': 2})
        self.assertEqual(str(ll), "{'id': 2} -> {'id': 1} -> None")
        ll.insert_beginning({'id': 3})
        self.assertEqual(ll.head.data, {'id': 3})
        self.assertEqual(ll.tail.data, {'id': 1})
        self.assertEqual(str(ll), "{'id': 3} -> {'id': 2} -> {'id': 1} -> None")
        ll.insert_at_end({'id': 0})
        self.assertEqual(str(ll), "{'id': 3} -> {'id': 2} -> {'id': 1} -> {'id': 0} -> None")

    def test_linked_list_exceptions(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 0})
        self.assertEqual(str(ll), "{'id': 1} -> {'id': 0} -> None")
        self.assertEqual(ll.insert_beginning([122132134]), None)

    def test_linked_list_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 0})
        self.assertEqual(ll.to_list(), [{'id': 1}, {'id': 0}])

    def test_linked_list_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 0})
        self.assertEqual(ll.get_data_by_id(1), {'id': 1})
