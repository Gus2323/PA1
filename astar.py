#
# astar.py
#
# This file provides a function implementing A* search for a route finding
# problem. Various search utilities from "route.py" are used in this function,
# including the classes RouteProblem, Node, and Frontier. Also, this function
# uses heuristic function objects defined in the "heuristic.py" file.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# Gustavo Castañeda - 10/09/2023
#


from route import Node
from route import Frontier


def a_star_search(problem, h, repeat_check=False):
    """Perform A-Star search to solve the given route finding problem,
    returning a solution node in the search tree, corresponding to the goal
    location, if a solution is found. Only perform repeated state checking if
    the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    initial_node = Node(problem.start)
    if problem.is_goal(initial_node.loc):
        return initial_node

    frontier = Frontier(initial_node, {h})
    reached_set = set()

    if repeat_check:
        reached_set.add(initial_node.loc)

    while not frontier.is_empty():
        popped_node = frontier.pop()
        if problem.is_goal(popped_node.loc):
            return popped_node
        for child in popped_node.expand(problem):
            if repeat_check:
                child_loc = child.loc
                if child_loc in reached_set:
                    if child in frontier:
                        #print(f'Child_loc Path cost {Node.value(popped_node)}.')
                        #print(f'Popped Node Path cost {Node.value(popped_node.loc)}.')
                        if Node.value(child) < Node.value(popped_node):
                            frontier.pop()
                            frontier.add(child)
                else:
                    frontier.add(child)
                    reached_set.add(child)
            else:
                frontier.add(child)
                reached_set.add(child)

    return None
