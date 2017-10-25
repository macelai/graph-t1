import unittest
from graph import Graph, VertexNotFoundException

class GraphTest(unittest.TestCase):
    def test_is_on_graph(self):
        g = Graph()
        g.add_vertex('a')
        self.assertEqual(g.single_vertex('a'), set())

    def test_not_on_graph(self):
        g = Graph()
        self.assertRaises(VertexNotFoundException, g.single_vertex('a'))

if __name__ == '__main__':
    unittest.main()
