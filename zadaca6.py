
import bisect
import sys

class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def successor(self, state):
        raise NotImplementedError

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def value(self):
        raise NotImplementedError

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node %s>" % (self.state,)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        return Node(next_state, self, action,
                    problem.path_cost(self.path_cost, self.state,
                                      action, next_state))

    def solution(self):
        return [node.action for node in self.path()[1:]]

    def solve(self):
        return [node.state for node in self.path()[0:]]

    def path(self):
        x, result = self, []
        while x:
            result.append(x)
            x = x.parent
        result.reverse()
        return result

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)

class Queue:
    def __init__(self):
        raise NotImplementedError

    def append(self, item):
        raise NotImplementedError

    def extend(self, items):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __contains__(self, item):
        raise NotImplementedError

class Stack(Queue):
    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop()

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data

class FIFOQueue(Queue):
    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop(0)

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data

class PriorityQueue(Queue):
    def __init__(self, order=min, f=lambda x: x):
        assert order in [min, max]
        self.data = []
        self.order = order
        self.f = f

    def append(self, item):
        bisect.insort_right(self.data, (self.f(item), item))

    def extend(self, items):
        for item in items:
            bisect.insort_right(self.data, (self.f(item), item))

    def pop(self):
        if self.order == min:
            return self.data.pop(0)[1]
        return self.data.pop()[1]

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return any(item == pair[1] for pair in self.data)

    def __getitem__(self, key):
        for _, item in self.data:
            if item == key:
                return item

    def __delitem__(self, key):
        for i, (value, item) in enumerate(self.data):
            if item == key:
                self.data.pop(i)

def tree_search(problem, fringe):
    fringe.append(Node(problem.initial))
    while fringe:
        node = fringe.pop()
        if problem.goal_test(node.state):
            return node
        fringe.extend(node.expand(problem))
    return None

def breadth_first_tree_search(problem):
    return tree_search(problem, FIFOQueue())

def depth_first_tree_search(problem):
    return tree_search(problem, Stack())

def graph_search(problem, fringe):
    closed = set()
    fringe.append(Node(problem.initial))
    while fringe:
        node = fringe.pop()
        if problem.goal_test(node.state):
            return node
        if tuple(sorted(node.state)) not in closed:
            closed.add(tuple(sorted(node.state)))
            fringe.extend(node.expand(problem))
    return None

def breadth_first_graph_search(problem):
    return graph_search(problem, FIFOQueue())

def depth_first_graph_search(problem):
    return graph_search(problem, Stack())

def depth_limited_search(problem, limit=50):
    def recursive_dls(node, problem, limit):
        cutoff_occurred = False
        if problem.goal_test(node.state):
            return node
        elif node.depth == limit:
            return 'cutoff'
        else:
            for successor in node.expand(problem):
                result = recursive_dls(successor, problem, limit)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
        if cutoff_occurred:
            return 'cutoff'
        return None

    return recursive_dls(Node(problem.initial), problem, limit)

def iterative_deepening_search(problem):
    for depth in range(sys.maxsize):
        result = depth_limited_search(problem, depth)
        if result is not 'cutoff':
            return result

def uniform_cost_search(problem):
    return graph_search(problem, PriorityQueue(min, lambda a: a.path_cost))

def check_valid(state, walls, n):
    for ball in state:
        i, j = ball
        if not (0 <= i < n and 0 <= j < n and (i, j) not in walls):
            return False
    return True

def gore_levo(state, removed_ball, moved_ball):
    new_state = []
    for ball in state:
        if ball == moved_ball:
            new_state.append((ball[0] - 2, ball[1] + 2))
        elif ball != removed_ball:
            new_state.append(ball)
    return tuple(new_state)

def gore_desno(state, removed_ball, moved_ball):
    new_state = []
    for ball in state:
        if ball == moved_ball:
            new_state.append((ball[0] + 2, ball[1] + 2))
        elif ball != removed_ball:
            new_state.append(ball)
    return tuple(new_state)

def dolu_levo(state, removed_ball, moved_ball):
    new_state = []
    for ball in state:
        if ball == moved_ball:
            new_state.append((ball[0] - 2, ball[1] - 2))
        elif ball != removed_ball:
            new_state.append(ball)
    return tuple(new_state)

def dolu_desno(state, removed_ball, moved_ball):
    new_state = []
    for ball in state:
        if ball == moved_ball:
            new_state.append((ball[0] + 2, ball[1] - 2))
        elif ball != removed_ball:
            new_state.append(ball)
    return tuple(new_state)

def levo(state, removed_ball, moved_ball):
    new_state = []
    for ball in state:
        if ball == moved_ball:
            new_state.append((ball[0] - 2, ball[1]))
        elif ball != removed_ball:
            new_state.append(ball)
    return tuple(new_state)

def desno(state, removed_ball, moved_ball):
    new_state = []
    for ball in state:
        if ball == moved_ball:
            new_state.append((ball[0] + 2, ball[1]))
        elif ball != removed_ball:
            new_state.append(ball)
    return tuple(new_state)

class Zadaca6(Problem):
    def __init__(self, initial, walls, n, goal):
        super().__init__(initial,goal)
        self.walls = walls
        self.n = n

    def successor(self, state):
        successors = {}
        n = self.n
        walls = self.walls
        for moved_ball in state:
            x, y = moved_ball
            # gore-levo
            removed_ball = (x - 1, y + 1)
            if removed_ball in state:
                gorelevo = gore_levo(state, removed_ball, moved_ball)
                if check_valid(gorelevo, walls, n):
                    successors[f"Gore Levo: (x={x},y={y})"] = gorelevo

            # gore-desno
            removed_ball = (x + 1, y + 1)
            if removed_ball in state:
                goredesno = gore_desno(state, removed_ball, moved_ball)
                if check_valid(goredesno, walls, n):
                    successors[f"Gore Desno: (x={x},y={y})"] = goredesno

            # dolu-levo
            removed_ball = (x - 1, y - 1)
            if removed_ball in state:
                dolulevo = dolu_levo(state, removed_ball, moved_ball)
                if check_valid(dolulevo, walls, n):
                    successors[f"Dolu Levo: (x={x},y={y})"] = dolulevo

            # dolu-desno
            removed_ball = (x + 1, y - 1)
            if removed_ball in state:
                doludesno = dolu_desno(state, removed_ball, moved_ball)
                if check_valid(doludesno, walls, n):
                    successors[f"Dolu Desno: (x={x},y={y})"] = doludesno

            # desno
            removed_ball = (x + 1, y)
            if removed_ball in state:
                right = desno(state, removed_ball, moved_ball)
                if check_valid(right, walls, n):
                    successors[f"Desno: (x={x},y={y})"] = right
            # levo
            removed_ball = (x - 1, y)
            if removed_ball in state:
                left = levo(state, removed_ball, moved_ball)
                if check_valid(left, walls, n):
                    successors[f"Levo: (x={x},y={y})"] = left
        #print(successors)
        return successors

    def goal_test(self, state):
        print(state)
        return len(state) == 1 and state == self.goal

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    balls = []
    for _ in range(m):
        inputt = tuple(map(int, input().split(",")))
        balls.append(inputt)
    w = int(input())
    walls = []
    for _ in range(w):
        inputt = tuple(map(int, input().split(",")))
        walls.append(inputt)
    balls = tuple(balls)
    walls = tuple(walls)
    goal = ((n // 2, n - 1),)
    start = Zadaca6(balls, walls, n,goal)
    result_node = breadth_first_graph_search(start)
    if result_node is not None:
        print(result_node.solution())
    else:
        print([])