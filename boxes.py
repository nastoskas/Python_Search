from searching_framework import *

class Boxes(Problem):
    def __init__(self, initial,boxes,n,goal=None):
        super().__init__(initial, goal)
        self.boxes = boxes
        self.n = n

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[1]) == len(self.boxes) and state[-1] == 0

    def successor(self, state):
        successors = {}
        man_x = state[0][0]
        man_y = state[0][1]
        filled_boxes = list(state[1])

        remaining_balls = state[2]

        dirs = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
        new_man = (man_x, man_y+1)
        #gore
        if new_man not in self.boxes and new_man[1] < self.n:
            new_remaining_balls = remaining_balls
            filled = filled_boxes
            for direction in dirs:
                if (new_man[0]+direction[0],new_man[1]+direction[1]) not in filled and (new_man[0]+direction[0],new_man[1]+direction[1]) in self.boxes:
                    new_remaining_balls -= 1
                    filled.append((new_man[0]+direction[0],new_man[1]+direction[1]))
            successors["Gore"] = (new_man,tuple(filled),new_remaining_balls)

        #desno
        new_man = (man_x+1, man_y)
        if new_man not in self.boxes and new_man[0] < self.n:
            new_remaining_balls = remaining_balls
            filled = filled_boxes
            for direction in dirs:
                if (new_man[0] + direction[0], new_man[1] + direction[1]) not in filled and (
                new_man[0] + direction[0], new_man[1] + direction[1]) in self.boxes:
                    new_remaining_balls -= 1
                    filled.append((new_man[0] + direction[0], new_man[1] + direction[1]))
            successors["Desno"] = (new_man, tuple(filled), new_remaining_balls)

        return successors

if __name__ == '__main__':
    n = int(input())
    man_pos = (0, 0)

    num_boxes = int(input())
    boxes = list()
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))
    num_balls = num_boxes
    initial = (man_pos, (), num_balls)
    problem = Boxes(initial, boxes, n)
    solution = breadth_first_graph_search(problem)
    if solution is not None:
        print(solution.solution())
    else:
        print("No Solution!")