from script import Problem, breadth_first_graph_search


def check_valid(covece, topka, protivnici):
    if not (0 <= covece[0] < 8 and 0 <= covece[1] < 6):
        return False
    if not (0 <= topka[0] < 8 and 0 <= topka[1] < 6):
        return False
    if covece == topka:
        return False
    if topka in protivnici:
        return False
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (topka[0] + dx, topka[1] + dy) in protivnici:
                return False
    return True


def check_valid_covece(covece, protivnici):
    if not (0 <= covece[0] < 8 and 0 <= covece[1] < 6):
        return False
    if covece in protivnici:
        return False
    return True


def move(pos, direction):
    moves = {
        "gore": (0, +1),
        "dolu": (0, -1),
        "desno": (+1, 0),
        "gore-desno": (+1, +1),
        "dolu-desno": (+1, -1)
    }
    return (pos[0] + moves[direction][0], pos[1] + moves[direction][1])


class Football(Problem):
    def __init__(self, initial, goal, protivnici):
        super().__init__(initial, goal)
        self.protivnici = protivnici

    def successor(self, state):
        successors = {}
        covece, topka = state

        directions = ["gore", "dolu", "desno", "gore-desno", "dolu-desno"]

        for direction in directions:
            new_covece = move(covece, direction)
            if new_covece == topka:
                new_topka = move(topka, direction)
                if check_valid(new_covece, new_topka, self.protivnici):
                    successors[f"Turni topka {direction}"] = (new_covece, new_topka)
            else:
                if check_valid_covece(new_covece, self.protivnici):
                    successors[f"Pomesti coveche {direction}"] = (new_covece, topka)

        return successors

    def actions(self, state):
        return list(self.successor(state).keys())

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] in self.goal


if __name__ == '__main__':
    player = tuple(map(int, input().split(",")))
    ball = tuple(map(int, input().split(",")))
    obst = {(3, 3), (5, 4)}
    goal = {(7, 2), (7, 3)}

    initial_state = (player, ball)
    football = Football(initial_state, goal, obst)

    result = breadth_first_graph_search(football)
    if result:
        print(result.solution())
    else:
        print("No Solution!")
