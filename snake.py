from script import Problem, breadth_first_graph_search,Node

def valid_move(snake, r_a):
    if len(snake) != len(set(snake)):
        return False
    for head in snake:
        if head in r_a:
            return False
    if 0<=snake[-1][0]<10 and 0<=snake[-1][1]<10:
        return True
    return False
#define moves
def dvizi_napred(state):
    snake = state[0]
    green_a = state[2]
    direction = state[1]
    dir_head = {
        'l': (-1,0), #1down, 2up, 3left, 4right
        'r': (+1,0),
        'g' : (0,+1),
        'd' : (0,-1)
    }
    new_head = (snake[-1][0]+dir_head[direction][0], snake[-1][1]+dir_head[direction][1])
    if new_head in green_a:
        snake1 = list(snake)
        snake1.append(new_head)
        snake1 = tuple(snake1)
        update_green = [green for green in green_a if green!=new_head]
        update_green = tuple(update_green)
        final_update = (snake1,direction,update_green)
        return final_update
    else:
        snake1 = list(snake)
        snake1.append(new_head)
        snake1.pop(0)

        snake1 = tuple(snake1)
        final_update = (snake1, direction,green_a)
        return final_update

def dvizi_levo(state):
    snake = state[0]
    green_a = state[2]
    direction = state[1]
    dir_head = {
        'l': (0,-1), #1down, 2up, 3left, 4right
        'r': (0,+1),
        'g': (-1,0),
        'd': (+1,0)
    }
    change_dir_of_head = {
        'l': 'd',
        'r': 'g',
        'g':'l',
       'd' : 'r'
    }
    new_dir = change_dir_of_head[direction]
    new_head = (snake[-1][0]+dir_head[direction][0], snake[-1][1]+dir_head[direction][1])
    if new_head in green_a:
        snake1 = list(snake)
        snake1.append(new_head)
        snake1 = tuple(snake1)
        update_green = [green for green in green_a if green!=new_head]
        update_green = tuple(update_green)
        final_update = (snake1,new_dir,update_green)
        return final_update
    else:
        snake1 = list(snake)
        snake1.append(new_head)
        snake1.pop(0)

        snake1 = tuple(snake1)
        final_update = (snake1,new_dir,green_a)
        return final_update

def dvizi_desno(state):
    snake = state[0]
    green_a = state[2]
    direction = state[1]
    dir_head = {
        'l': (0, +1), #1down, 2up, 3left, 4right
        'r': (0, -1),
        'g': (+1, 0),
        'd': (-1, 0)
    }
    change_dir_of_head = {
        'l': 'g',
        'r': 'd',
        'g': 'r',
        'd': 'l'
    }
    new_dir = change_dir_of_head[direction]
    new_head = (snake[-1][0] + dir_head[direction][0], snake[-1][1] + dir_head[direction][1])
    if new_head in green_a:
        snake1 = list(snake)
        snake1.append(new_head)
        snake1 = tuple(snake1)
        update_green = [green for green in green_a if green != new_head]
        update_green = tuple(update_green)
        final_update = (snake1, new_dir,update_green )
        return final_update
    else:
        snake1 = list(snake)
        snake1.append(new_head)
        snake1.pop(0)

        snake1 = tuple(snake1)
        final_update = (snake1, new_dir, green_a)
        return final_update

class Snake(Problem):
    def __init__(self,initial,r_a):
        super().__init__(initial,goal=None)
        self.r_a = r_a
        #self.gridSize = 10

    def successor(self, state):
        successors = {}
        levo = dvizi_levo(state)
        desno = dvizi_desno(state)
        napred = dvizi_napred(state)

        #ako e validen potezot

        if valid_move(levo[0], self.r_a):
            successors["SvrtiLevo"] = levo
        if valid_move(desno[0], self.r_a):
            successors["SvrtiDesno"] = desno
        if valid_move(napred[0], self.r_a):
            successors["ProdolzhiPravo"] = napred

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[-1]) == 0 #if green apples are gone


if __name__ == '__main__':
    N = int(input())
    zeleni = []
    for g in range(N):
        inputt = [int(n) for n in input().split(",")]
        zeleni.append(tuple(inputt))
    snake_pos = ((0,9),(0,8),(0,7))
    M = int(input())
    crveni =  []
    for r in range(M):
        inputt = [int(c) for c in input().split(",")]
        crveni.append(tuple(inputt))

    initiall = (tuple(snake_pos), 'd', tuple(zeleni) )
    start = Snake(initiall,crveni)

    if breadth_first_graph_search(start) is not None:
        print(breadth_first_graph_search(start).solution())
    else:
        print([])
