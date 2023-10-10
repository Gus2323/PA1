#
# ucost.py
#
# This file provides a function implementing uniform cost search for a
# route finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# Gustavo Castañeda - 10/09/2023
#


from route import Node
from route import Frontier


def uniform_cost_search(problem, repeat_check=False):
    """Perform uniform cost search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    initial_node = Node(problem.start)
    if problem.is_goal(initial_node.loc):
        return initial_node

    frontier = Frontier(initial_node, False)  # queue
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
                    reached_set.add(child_loc)
            else:
                frontier.add(child)
                reached_set.add(child)

    return None
