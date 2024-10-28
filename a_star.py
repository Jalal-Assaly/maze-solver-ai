"""
This module implements the A* algorithm for maze solving.
"""
from queue import PriorityQueue
from pyamaze import maze

def h(cell1, cell2):
    """
    This function implements the heuristic function
    by calculating the Manhattan distance between the 
    agent's position and the goal node (10,10).
    """
    x1,y1 = cell1
    x2,y2 = cell2

    return abs(x1-x2) + abs(y1-y2)


def aStarAlg(myMaze: maze, start, goal):

    # Initialize g_costs for all cells with infinity
    g_costs = {cell:float('inf') for cell in myMaze.grid}
    # Cost of moving from start cell to start cell is zero
    g_costs[start] = 0

    # Initialize h_costs for all cell with infinity
    h_costs = {cell:float('inf') for cell in myMaze.grid}
    # Heuristic cost of start cell
    h_costs[start] = h(start, goal)

    # Initialize h_costs for all cell with infinity
    f_costs = {cell:float('inf') for cell in myMaze.grid}
    # Heuristic cost of start cell
    f_costs[start] = g_costs[start] + h_costs[start]

    # Create priority queue
    open_list = PriorityQueue()
    # Add the tuple (f_costs priority, h_score priority, start_coordinates)
    open_list.put((f_costs[start], h_costs[start], start))

    # Create variables for path memorization
    srchPath = []
    rvrsPath = {}
    fwdPath = {}

    while not open_list.empty():
        # Get the next cell coordinates with highest priority
        currCell = open_list.get()[2]
        srchPath.append(currCell)
        # If goal is reached, break
        if currCell == goal:
            break
        
        # Explore surrounding cells (added to the graph)
        for direction in "ESNW":
            # If there is a wall, skip to the next direction
            if not myMaze.maze_map[currCell][direction]:
                continue
            
            if direction == 'E':
                nextCell = (currCell[0], currCell[1] + 1)
            elif direction == 'W':
                nextCell = (currCell[0], currCell[1] - 1)
            elif direction == 'N':
                nextCell = (currCell[0] - 1, currCell[1]) 
            elif direction == 'S':
                nextCell = (currCell[0] + 1, currCell[1])

            # Update costs of next cells
            next_g_cost = g_costs[currCell] + 1
            next_h_cost = h(nextCell, goal)
            next_f_cost = next_g_cost + next_h_cost

            
            if next_f_cost < f_costs[nextCell]:
                # Update the dictionary costs
                g_costs[nextCell] = next_g_cost
                h_costs[nextCell] = next_h_cost
                f_costs[nextCell] = next_f_cost

                # Add the the cell to the open list
                open_list.put((next_f_cost, next_h_cost, nextCell))
                # Add the cells to the reverse dictionary
                rvrsPath[nextCell] = currCell

    # Create a temporary cell starting at the goal
    cell = goal

    # Add the goal cell in fwdPath
    fwdPath[goal] = None

    # Move backward and write down the path taken in the fwdPath
    while cell != start:
        fwdPath[rvrsPath[cell]] = cell
        cell = rvrsPath[cell]

    # Return all paths for plotting
    return srchPath, rvrsPath, fwdPath