import breadthFirstSearch as bfs
import unittest as ut

class TestBreadthFirst(ut.TestCase):
    def test_case_one(self):
        graph = bfs.Node('A')
        graph.addChild('B').addChild('C').addChild('D')
        graph.children[0].addChild('E').addChild('F')
        graph.children[2].addChild('G').addChild('H')
        graph.children[0].children[1].addChild('I').addChild('J')
        graph.children[2].children[0].addChild('K')
        result = graph.breadthFirstSearch([])
        expected = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
        self.assertEqual(result, expected)

if __name__ == '__main__':
    ut.main()
