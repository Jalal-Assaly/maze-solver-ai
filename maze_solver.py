from pyamaze import maze, agent
from a_star import aStarAlg
import random

# Create Maze instance
myMaze = maze(101,101)
# Generate start (center) and goal positions (random)
start = (myMaze.rows//2 + 1, myMaze.cols//2 + 1)
goal = (random.randint(1, myMaze.rows+1), random.randint(1, myMaze.cols+1))

# Place the goal at the bottom right corner
myMaze.CreateMaze(goal[0],goal[1], loopPercent=5)

# Create searching agent
srchAgent = agent(myMaze, x=start[0], y=start[1], filled=True, color='blue', footprints=True,)
# Create searching agent
rvrsAgent = agent(myMaze, x=goal[0], y=goal[1], goal=start, filled=True, color='green', footprints=True)
# Create the moving agent instance at the upper left corner
myAgent = agent(myMaze, x=start[0], y=start[1], color='red', shape='arrow')

# Get all paths from A* algorithm
srchPath, rvrsPath, fwdPath = aStarAlg(myMaze, start, goal)

#Trace searching path
myMaze.tracePath({srchAgent:srchPath}, delay=int(2000/max(myMaze.rows,myMaze.cols)))    # Delay depends on maze size. The larger, the faster the plotting
# Trace reverse path
myMaze.tracePath({rvrsAgent:rvrsPath}, delay=int(2000/max(myMaze.rows,myMaze.cols)))
# Trace forward path
myMaze.tracePath({myAgent:fwdPath}, delay=200)

myMaze.run()