#
# heuristic.py
#
# This script defines a utility class that can be used as an implementation
# of a frontier state (location) evaluation function for use in route-finding
# heuristic search algorithms. When a HeuristicSearch object is created,
# initialization code can be executed to prepare for the use of the heuristic
# during search. In particular, a RouteProblem object is typically provided 
# when the HeuristicFunction is created, providing information potentially
# useful for initialization. The actual heuristic cost function, simply
# called "h_cost", takes a state (location) as an argument.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# Gustavo Castañeda - 10/08/2023
# Comments: Professor David gave a tip on how to come up with
# a heuristic function that calculates mpg. This means we will use the values of
# the vertices to determine which path to take.


import route


class HeuristicFunction:
    """A heuristic function object contains the information needed to
    evaluate a state (location) in terms of its proximity to an optimal
    goal state."""

    def __init__(self, problem=None):
        self.problem = problem
        # PLACE ANY INITIALIZATION CODE HERE
        self.goal = problem.goal
        self.map = problem.map



    def h_cost(self, loc=None):
        """An admissible heuristic function, estimating the cost from
        the specified location to the goal state of the problem."""
        # a heuristic value of zero is admissible but not informative
        value = 0.0
        goal = self.problem.goal
        problem = self.problem

        if loc is None:
            return value
        else:
            # PLACE YOUR CODE FOR CALCULATING value OF loc HERE
            miles = problem.euclidean_distance(loc, goal) #distance from goal
            roads = problem.actions(loc) #all possible nodes
            gallon = 0

            for i in roads:  #iterate through nodes to get mpg
                node = problem.result(loc, i)
                gallon = gallon + problem.action_cost(loc, node)
                value = miles / gallon  # mpg calculated

            return value