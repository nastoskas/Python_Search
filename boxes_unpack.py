from searching_framework import *

class Boxes(Problem):
    def __init__(self, initial, n, boxes, goal=None):
        super().__init__(initial, goal)
        self.n = n
        self.boxes = boxes

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        print(state)
        return state[-1]==0 and len(state[1])== len(self.boxes)

    def successor(self, state):
        successors = {}
        man_x, man_y = state[0]
        visited_boxes = state[1]
        n_boxes = state[2]

        #dolu
        new_man = (man_x, man_y-1)
        if man_y-1 >=0 and new_man not in self.boxes:
            visited_new = list(visited_boxes)
            new_n = n_boxes
            for box in self.boxes:
                if box not in visited_new and abs(box[0]-new_man[0]) <= 1 and abs(box[1]-new_man[1]) <= 1:
                    visited_new.append(box)
                    new_n -= 1
            successors["Dolu"] = (new_man,tuple(visited_new),new_n)

        #levo
        new_man = (man_x-1, man_y)
        if man_x - 1 >= 0 and new_man not in self.boxes:
            visited_new = list(visited_boxes)
            new_n = n_boxes
            for box in self.boxes:
                if box not in visited_new and abs(box[0]-new_man[0]) <= 1 and abs(box[1]-new_man[1]) <= 1:
                    visited_new.append(box)
                    new_n -= 1
            successors["Levo"] = (new_man, tuple(visited_new), new_n)

        return successors
if __name__ == '__main__':
    n = int(input())
    man_pos = (n-1, n-1)

    num_boxes = int(input())
    boxes = list()
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))
    initial = (man_pos, (), num_boxes)
    problem = Boxes(initial,n,boxes)
    solution = breadth_first_graph_search(problem)
    if solution is not None:
        print(solution.solution())
    else:
        print("No Solution!")