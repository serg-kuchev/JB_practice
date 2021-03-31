class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.value = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem


class SearchTree:

    def __init__(self):
        self.root = None

    def __iter__(self):
        """Итератор по корням"""
        return self.root.__iter__()

    def put(self, key, val):
        """Построение дерева"""
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)

    def _put(self, key, val, current_node):
        """Рекурсивное построение дерева"""
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)

    def __setitem__(self, key, value):
        """Присваивание значений для дерева в виде ключ-значение"""
        self.put(key, value)

    def search(self, key):
        """Поиск по дереву"""
        if self.root:
            res = self._search(key, self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def _search(self, key, current_node):
        """Вспомогательный метод поиска"""
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._search(key, current_node.left_child)
        else:
            return self._search(key, current_node.right_child)

    def __getitem__(self, key):
        """Доступ к данным как в словаре"""
        return self.search(key)

    def height(self):
        """Определение высоты дерева"""
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node is None:
            return current_height
        left_height = self._height(current_node.left_child, current_height + 1)
        right_height = self._height(current_node.right_child, current_height + 1)
        return max(left_height, right_height)
