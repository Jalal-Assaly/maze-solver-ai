import unittest
import random
# Import the components that need to be tested
from pyamaze import maze
from a_star import aStarAlg


class AStarAlgTestCase(unittest.TestCase):
    def setUp(self):
        # Retrieve the existing maze from maze_solver.py
        from maze_solver import myMaze, start, goal
        self.myMaze = myMaze
        self.start = start
        self.goal = goal


    def test_aStarAlg(self):
        # Call the A* algorithm
        srchPath, rvrsPath, fwdPath = aStarAlg(self.myMaze, self.start, self.goal)

        # Assertions
        self.assertIsInstance(srchPath, list)
        self.assertIsInstance(rvrsPath, dict)
        self.assertIsInstance(fwdPath, dict)

        # Start position should be in the search path
        self.assertIn(self.start, srchPath)
        # Goal position should be in the search path
        self.assertIn((self.goal[0], self.goal[1]), srchPath)
        # Start position should be in the forward path
        self.assertIn(self.start, fwdPath)
        # Goal position should be in the forward path
        self.assertIn((self.goal[0], self.goal[1]), fwdPath)


    def test_aStarAlg_large_maze(self):
        # Create a large maze
        largeMaze = maze(101, 101)
        largeMaze.CreateMaze(largeMaze.rows, largeMaze.cols)

        # Create start cell and goal cell
        start = (51, 51)
        goal = (random.randint(1, 101), random.randint(1, 101))

        # Call the A* algorithm on the large maze
        srchPath, rvrsPath, fwdPath = aStarAlg(largeMaze, start, goal)

        # Assertions
        self.assertIsInstance(srchPath, list)
        self.assertIsInstance(rvrsPath, dict)
        self.assertIsInstance(fwdPath, dict)

        # Start position should be in the search path
        self.assertIn(start, srchPath)
        # Goal position should be in the search path
        self.assertIn((goal[0], goal[1]), srchPath)
        # Start position should be in the forward path
        self.assertIn(start, fwdPath)
        # Goal position should be in the forward path
        self.assertIn((goal[0], goal[1]), fwdPath)


    def test_aStarAlg_many_paths(self):
        # Create a maze without any obstacles
        emptyMaze = maze(11, 11)
        emptyMaze.CreateMaze(emptyMaze.rows, emptyMaze.cols, loopPercent=100)

        # Create start cell and goal cell
        start = (6, 6)
        goal = (random.randint(1, 11), random.randint(1, 11))

        # Call the A* algorithm on the empty maze
        srchPath, rvrsPath, fwdPath = aStarAlg(emptyMaze, start, goal)

        # Assertions
        self.assertIsInstance(srchPath, list)
        self.assertIsInstance(rvrsPath, dict)
        self.assertIsInstance(fwdPath, dict)

        # Start position should be in the search path
        self.assertIn(start, srchPath)
        # Goal position should be in the search path
        self.assertIn((goal[0], goal[1]), srchPath)
        # Start position should be in the forward path
        self.assertIn(start, fwdPath)
        # Goal position should be in the forward path
        self.assertIn((goal[0], goal[1]), fwdPath)


    def test_aStarAlg_no_solution(self):
        # Create a maze with no solution
        unsolvableMaze = maze(3, 3)

        # Design maze map
        unsolvableMaze.maze_map = {
            (1,1): {'E': 0, 'W': 0, 'N': 0, 'S': 1},
	        (1,2): {'E': 0, 'W': 0, 'N': 0, 'S': 0},
	        (1,3): {'E': 0, 'W': 0, 'N': 0, 'S': 1},
	        (2,1): {'E': 0, 'W': 0, 'N': 1, 'S': 0},
	        (2,2): {'E': 0, 'W': 0, 'N': 0, 'S': 1},
	        (2,3): {'E': 0, 'W': 0, 'N': 1, 'S': 0},
	        (3,1): {'E': 1, 'W': 0, 'N': 0, 'S': 0},
	        (3,2): {'E': 0, 'W': 1, 'N': 1, 'S': 0},
	        (3,3): {'E': 0, 'W': 0, 'N': 0, 'S': 0}
        }

        # Create start cell and goal cell
        start = (2,2)
        goal = (1,3)

        # Call the A* algorithm on the unsolvable maze
        srchPath, rvrsPath, fwdPath = aStarAlg(unsolvableMaze, start, goal)

        # Assertions
        self.assertEqual(srchPath, [])  # Search path should be empty as there is no solution
        self.assertEqual(rvrsPath, {})  # Reverse path should be empty as there is no solution
        self.assertEqual(fwdPath, {})  # Forward path should be empty as there is no solution


if __name__ == '__main__':
    unittest.main()