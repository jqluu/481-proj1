from search import *
# YOUR CODE GOES HERE


class WolfGoatCabbage(Problem):

    def __init__(self, initial=('F', 'W', 'G', 'C'), goal=()):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)


    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        return state == self.goal
    

    def result(self, state, action):

        newState = ()

        if (state == ('F', 'W', 'G', 'C') and action == {'G', 'F'}):
            newState = ('W', 'C')
        elif (state == ('W', 'C') and action == {'F'}):
            newState = ('F', 'W', 'C')
        elif (state == ('F', 'W', 'C') and action == {'W', 'F'}):
            newState = ('C')
        elif (state == ('F', 'W', 'C') and action == {'C', 'F'}):
            newState = ('W')
        elif (state == ('W') and action == {'G','F'}):
            newState = ('F', 'G', 'W')
        elif (state == ('C') and action == {'G','F'}):
            newState = ('F', 'G', 'C')
        elif (state == ('F', 'G', 'C') and action == {'C', 'F'}):
            newState = ('G')
        elif (state == ('F', 'G', 'W') and action == {'W', 'F'}):
            newState = ('G')
        elif (state == ('G') and action == {'F'}):
            newState = ('F', 'G')
        elif (state == ('F', 'G') and action == {'G', 'F'}):
            newState = ()
        elif (action == {}):
            newState = ()

        return newState
    

    def actions(self, state):

        possibleActions = []
        #[('F'), ('F', 'G'), ('F', 'W'), ('F', 'C'), ('G', 'F'), ()]
        # depending on what is in the current state, returns list of possible actions

        if (state == ('F', 'W', 'G', 'C')):
            possibleActions = [{'G', 'F'}]
        elif(state == ('W', 'C')):
            possibleActions = [{'F'}]
        elif(state == ('F', 'W', 'C')):
            possibleActions = [{'W', 'F'}, {'C', 'F'}]
        elif(state == ('C') or state == ('W')):
            possibleActions = [{'G', 'F'}]
        elif(state == ('F', 'G', 'C')):
            possibleActions = [{'C', 'F'}]
        elif(state == ('F', 'G', 'W')):
            possibleActions = [{'W', 'F'}]
        elif(state == ('G')):
            possibleActions = [{'F'}]
        elif(state == ('F', 'G')):
            possibleActions = [{'G', 'F'}]
        elif(state == ()):
            possibleActions = []
        
        return possibleActions
    
    
# TODO
# constructor WolfGoatCabbage(), sets initial and goal states
# method goat_test(state), returns true if state is goal state
# method result(state, action), returns new state reached from given state and action
# method actions(state), returns list of valid actions given state

    
if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)



