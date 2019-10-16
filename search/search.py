# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import searchAgents as scha
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    visited=util.Counter()#Handle cycle cases in graph
    s=util.Stack()
    s.push((problem.getStartState(),[],[]))#Push start state onto stack
   
    while True:
        if(s.isEmpty()==True):#If Stack is empty no graph to traverse
            return []

        startstat=s.pop() 
        action=startstat[1]#Store currentstate action to reach next successor
        visited[startstat[0]]=1#Mark currentsate visited

        if(problem.isGoalState(startstat[0])):
            #print(action)
            return action

        #Iterate over all child nodes and push in stack.We have to just expand 
        #node not visit the child nodes
        for stat in problem.getSuccessors(startstat[0]):  
            #Push to stack when node is not visited already
            if(visited[stat[0]]==0):  
                #Push nodes to stack with updated actions taken to reach state
                s.push((stat[0],startstat[1]+[stat[1]],stat[2]))
                #Save actions taken to reach a state
                action=action+[stat[1]]
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    visited=[]#Handle cycle cases in graph
   
    q=util.Queue()
    if(problem.isGoalState(problem.getStartState())):
        return []
    q.push((problem.getStartState(),[]))

    while not q.isEmpty():

        startstat=q.pop()

        visited.append(startstat[0])

        action=startstat[1]
        #print(startstat[0])
        if(problem.isGoalState(startstat[0])):


            return action

        for stat in problem.getSuccessors(startstat[0]):

            if(stat[0] not in visited): 
               
                q.push((stat[0],startstat[1]+[stat[1]],stat[2]))

                visited.append(stat[0])

    util.raiseNotDefined()


def uniformCostSearch(problem):
    visited=util.Counter()#Handle cycle cases in graph
    pq=util.PriorityQueue()
    pq.push((problem.getStartState(),[],0.0),0.0)
    
    while not pq.isEmpty():
        startstat=pq.pop()
        
        
        action=startstat[1]

        if(problem.isGoalState(startstat[0])):
           
            return action

        if(visited[startstat[0]]==0):
            visited[startstat[0]]=1
            
            for stat in problem.getSuccessors(startstat[0]):
                if(visited[stat[0]]==0): 
                    prior=startstat[2]+stat[2]
                   
                    pq.push((stat[0],startstat[1]+[stat[1]],prior),prior)
                
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    visited=[]#Handle cycle cases in graph
    pq=util.PriorityQueue()
    start=problem.getStartState()
    pq.push((start,[],0.0),(0.0+heuristic(start,problem)))
    
    while not pq.isEmpty():
        startstat=pq.pop()
        
        
        action=startstat[1]
       
        if(problem.isGoalState(startstat[0])):
            return action

        
        if(startstat[0] not in visited):
            visited.append(startstat[0])
    
            
            for stat in problem.getSuccessors(startstat[0]):
                if(stat[0] not in visited): 
                    prior=startstat[2]+stat[2]
                   
                    pq.push((stat[0],startstat[1]+[stat[1]],prior),(prior+heuristic(stat[0],problem)))
    return []               
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch