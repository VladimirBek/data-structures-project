class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):

        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        try:
            if not isinstance(data, dict) or data.get('id') == None:
                raise TypeError('Данные не являются словарем или в словаре нет id.')
            if self.head is None:
                self.head = self.tail = Node(data)
            else:
                self.head = Node(data, next_node=self.head)
        except TypeError:
            print('Данные не являются словарем или в словаре нет id.')

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        try:
            if not isinstance(data, dict) or data.get('id') == None:
                raise TypeError('Данные не являются словарем или в словаре нет id.')
            node = Node(data)
            if self.head is None:
                self.head = self.tail = node
            else:
                self.tail.next_node = node
                self.tail = node
        except TypeError:
            print('Данные не являются словарем или в словаре нет id.')

    def to_list(self):
        res = []
        node = self.head
        if node is None:
            return res

        while node:
            res.append(node.data)
            node = node.next_node
        return res

    def get_data_by_id(self, id_val):
        node = self.head
        while node:
            if node.data['id'] == id_val:
                return node.data
            node = node.next_node
        return f'В списке нет элемента с таким id'

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string
