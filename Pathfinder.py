'''
Ian Lizarda, Basil Latif, Jordan Sanders

The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to the
optimal goal state.

This task is done in the Pathfinder.solve method, as parameterized
by a maze pathfinding problem, and is aided by the SearchTreeNode DS.
'''
import queue
from MazeProblem import MazeProblem
from SearchTreeNode import SearchTreeNode
import unittest


class Pathfinder:

    # solve is parameterized by a maze pathfinding problem
    # (see MazeProblem.py and unit tests below), and will
    # return a list of actions that solves that problem. An
    # example returned list might look like:
    # ["U", "R", "R", "U"]

    def solve(problem):
        q = queue.Queue()
        q.put(SearchTreeNode(problem.initial, None, None))
        shadow_realm = set()
        while q:
            curr_node = q.get()
            if problem.goalTest(curr_node.state):
                return Pathfinder.find_path(curr_node)
            for action, state in problem.transitions(curr_node.state):
                if state not in shadow_realm:
                    q.put(SearchTreeNode(state, action, curr_node))
            shadow_realm.add(curr_node.state)
        return []

    def find_path(search_node):
        path = []
        curr_node = search_node
        while curr_node.parent:
            path.append(curr_node.action)
            curr_node = curr_node.parent
        return path[::-1]


class PathfinderTests(unittest.TestCase):
    def test_maze1(self):
        maze = ["XXXXX", "X..GX", "X..XX", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze2(self):
        maze = ["XXXXX", "XG..X", "XX..X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze3(self):
        maze = ["XXXXX",
                "X..GX",
                "X..XX",
                "X*..X",
                "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze4(self):
        maze = ["XXXXX",
                "X.*GX",
                "X..XX",
                "X...X",
                "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 1)

    def test_maze5(self):
        maze = ["XXXGX",
                "X...X",
                "X..XX",
                "X..XX",
                "X...*"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 7)

    def test_maze6(self):
        maze = ["...G.",
                ".....",
                ".....",
                ".....",
                "....*"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 5)


if __name__ == '__main__':
    unittest.main()
