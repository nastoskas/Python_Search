from searching_framework import Problem, astar_search
class Lab2(Problem):
    def __init__(self,initial,allowed):
        super().__init__(initial)
        self.allowed = allowed

    def move_house(self, house):
        house_x = house[0][0]
        house_y = house[0][1]
        direction = house[1]
        #desno
        if direction == 1:
            if house_x == 4:
                direction = 0
                house_x -= 1
            else:
                house_x += 1
        else: #levo
            if house_x == 0:
                direction = 1
                house_x += 1
            else:
                house_x -= 1
        return ((house_x,house_y),direction)

    def successor(self, state):
        man, house = state
        #print(f"Current state: {state}")

        man_x = man[0]
        man_y = man[1]
        new_house = self.move_house(house)

        successors = {}
        if (man_x, man_y) in self.allowed or (man_x, man_y) == new_house[0]:
            successors["Stoj"] = ((man_x, man_y), new_house)
        #gore1
        if (man_x,man_y + 1) in self.allowed or (man_x, man_y+1) == new_house[0]:
            successors["Gore 1"] = ((man_x, man_y+1), new_house)

        #gore2
        if (man_x, man_y + 2) in self.allowed or (man_x, man_y+2) == new_house[0]:
            successors["Gore 2"] = ((man_x, man_y + 2), new_house)

        # gore-levo1
        if (man_x - 1, man_y + 1) in self.allowed or (man_x - 1, man_y + 1) == new_house[0]:
            successors["Gore-levo 1"] = ((man_x - 1, man_y + 1), new_house)

        # gore-levo2
        if (man_x - 2, man_y + 2) in self.allowed or (man_x - 2, man_y + 2) == new_house[0]:
            successors["Gore-levo 2"] = ((man_x - 2, man_y + 2), new_house)

        #gore-desno1
        if (man_x + 1, man_y + 1) in self.allowed or (man_x+1, man_y+1) == new_house[0]:
            successors["Gore-desno 1"] = ((man_x + 1, man_y + 1), new_house)

        #gore-desno2
        if (man_x + 2, man_y + 2) in self.allowed or (man_x+2, man_y+2) == new_house[0]:
            successors["Gore-desno 2"] = ((man_x + 2, man_y + 2), new_house)


        #print(f"State: {state}, Successors: {successors}")
        return successors

    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        return state[0] == state[1][0]
    def h(self, node):
        x_man,y_man = node.state[0]
        x_house,y_house = node.state[1]
        if y_man == 8:
            return 0
        return (8 - y_man)/2

if __name__ == '__main__':
    allowed = [(1,0), (2,0), (3,0), (1,1), (2,1), (0,2), (2,2), (4,2), (1,3), (3,3), (4,3), (0,4), (2,4), (2,5), (3,5), (0,6), (2,6), (1,7), (3,7)]
    man = tuple(map(int,input().split(',')))
    house = tuple(map(int,input().split(',')))
    house_dir = input()
    house_direction = 1 if house_dir == "desno" else 0

    initial = (man,(house,house_direction))
    problem = Lab2(initial,allowed)
    solution = astar_search(problem)

    if solution:
        print(solution.solution())
    else:
        print("[]")

