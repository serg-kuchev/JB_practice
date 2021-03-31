from main import SearchTree
import unittest


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.my_tree = SearchTree()
        self.my_tree[1] = '1'
        self.my_tree[2] = '2'
        self.my_tree[3] = '3'
        self.my_tree[4] = '4'
        self.my_tree[5] = '5'

    def test_put_method(self):
        self.assertIs(self.my_tree[1], '1')

    def test_search_method(self):
        self.assertEqual(self.my_tree.search(1), '1')

    def test_height_method(self):
        self.assertEqual(self.my_tree.height(), 5)

    def tearDown(self):
        pass
