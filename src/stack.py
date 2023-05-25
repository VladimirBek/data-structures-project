class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self):
        res = []
        obj = self.top
        if obj is None:
            return ''
        while obj is not None:
            res.append(str(obj.data))
            obj = obj.next_node
        return '\n'.join(res)[::-1]

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        self.top = Node(data, next_node=self.top)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.top is None:
            raise IndexError('Попытка удаления элемента из пустого стека')
        copy_top = self.top.data
        self.top = self.top.next_node
        return copy_top
