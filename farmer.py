from script import *

def valid(state):
    farmer, volk, jare, zelka = state
    if volk == jare and volk!=farmer:
        return False
    if jare == zelka and jare != farmer:
        return False
    return True

class Farmer(Problem):
    def __init__(self,initial, goal):
        super().__init__(initial,goal)

    def successor(self, state):
        # state = (farmer,volk,jare,zelka) (e,w,e,w)
        successors = dict()
        farmer, volk, jare, zelka = state

        # Farmer nosi farmer
        farmer_new = 'e' if farmer == 'w' else 'w'
        state_new = (farmer_new, volk, jare, zelka)
        if valid(state_new):
            successors["Farmer_nosi_farmer"] = state_new

        #Farmer nosi volk
        if farmer == volk:
            volk_new = 'e' if volk == 'w' else 'w'
            state_new = (farmer_new,volk_new,jare,zelka)
            if valid(state_new):
                successors["Farmer nosi volk"] = state_new

        #Farmer nosi jare
        if farmer == jare:
            jare_new = 'e' if jare == 'w' else 'w'
            state_new = (farmer_new,volk, jare_new, zelka)
            if valid(state_new):
                successors["Farmer nosi jare"] = state_new

        #Farmer nosi zelka
        if farmer == zelka:
            zelka_new = 'e' if zelka == 'w' else 'w'
            state_new = (farmer_new,volk,jare,zelka_new)
            if valid(state_new):
                successors["Farmer nosi zelka"] = state_new

        return successors

    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def h(self, node):
        state = node.state
        goal = self.goal

        value = 0

        for x,y in zip(state,goal):
            if x!=y:
                value+=1
        return value

if __name__=='__main__':
    initial_state = ('e','e','e','e')
    goal_state = ('w','w','w','w')

    farmer = Farmer(initial_state,goal_state)

    result = astar_search(farmer)

    print(result.solution())