from searching_framework import Problem, astar_search



class Lab2(Problem):
    def __init__(self,initial,kukicka,dzidovi,n):
        super().__init__(initial, goal=None)
        self.kukicka = kukicka
        self.dzidovi = dzidovi
        self.n = n

    def check_valid(self,covece):
        n = self.n
        dzidovi = self.dzidovi
        if covece[0]<0 or covece[0]>=n or covece[1] < 0 or covece[1]>=n:
            return False
        if covece in dzidovi:
            return False
        return True

    def successor(self, state):
        successors = {}
        covece = state
        x_covece = covece[0]
        y_covece = covece[1]
        # gore
        new_covece = (x_covece,y_covece+1)
        if self.check_valid(new_covece):
            successors["Gore"] = new_covece
        #dolu
        new_covece = (x_covece, y_covece - 1)
        if self.check_valid(new_covece):
            successors["Dolu"] = new_covece
        #levo
        new_covece = (x_covece-1, y_covece)
        if self.check_valid(new_covece):
            successors["Levo"] = new_covece
        #desno2
        new_covece = (x_covece+2, y_covece)
        if self.check_valid(new_covece) and (x_covece+1,y_covece) not in dzidovi:
            successors["Desno 2"] = new_covece
        #desno3
        new_covece = (x_covece + 3, y_covece)
        if self.check_valid(new_covece) and (x_covece + 1, y_covece) not in dzidovi and (x_covece+2,y_covece) not in dzidovi:
            successors["Desno 3"] = new_covece

        return successors
    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        return state == self.kukicka
    def h(self, node):
        covece = node.state
        x_covece, y_covece = covece
        x_kukicka, y_kukicka = self.kukicka
        heuristic = 0
        dist = abs(x_covece-x_kukicka)
        if x_covece < x_kukicka:
            if dist == 1:
                return 2
            elif dist % 3 == 0:
                heuristic += dist / 3
            else:
                heuristic += dist // 3 + 1
        if x_covece > x_kukicka:
            heuristic+=dist

        if y_covece !=  y_kukicka:
            dist = abs(y_kukicka - y_covece)
            heuristic += dist

        return heuristic

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    dzidovi = []
    for i in range(m):
        dzidovi.append(tuple(map(int,input().split(','))))
    covece = tuple(map(int,input().split(',')))
    kukicka = tuple(map(int,input().split(',')))

    problem = Lab2(covece,kukicka,dzidovi,n)
    solution = astar_search(problem)
    if solution:
        print(solution.solution())
    else:
        print("[]")
