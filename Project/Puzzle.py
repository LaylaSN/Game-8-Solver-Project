import heapq

class PuzzleState:
    def __init__ (self, board, parent=None, move=None, depth=0 ,cost=0):
        self.board = board
        self.parent = parent 
        self.move = move
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def get_neighbors(self):
        neighbors = []
        zero_index = self.board.index(0)
        x, y = zero_index // 3, zero_index % 3

        directions = {'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}

        for move, (dx,dy) in directions.items():
            nx, ny = x+dx , y+dy
            if 0<= nx < 3 and 0<= ny < 3:
                new_board = self.board [:]
                new_index = nx*3 + ny
                new_board[zero_index], new_board[new_index] = new_board[new_index], new_board[zero_index]
                neighbors.append(PuzzleState(new_board, self, move, self.depth+1, 0))
        
        return neighbors


def distance(board,goal):
    cost=0
    for i in range (1,9):
        xi, yi= divmod(board.index(i), 3)
        xg, yg= divmod(goal.index(i), 3)
        cost += abs (xi - xg) + abs (yi - yg)
    return cost


def a_star(start,goal):
    opened_list = []
    done = set ()
    start_state = PuzzleState (start, cost=distance(start,goal))

    heapq.heappush(opened_list, start_state)

    while(opened_list):
        current = heapq.heappop(opened_list)

        if current.board == goal:
            return current
        
        done.add(tuple(current.board))

        for neighbor in current.get_neighbors():
            if tuple(neighbor.board) in done: continue

            neighbor.cost = neighbor.depth + distance(neighbor.board, goal)
            heapq.heappush(opened_list, neighbor)

    path = []
    state = current.board
    while state:
        path.append((state.move, state.board))
        state = state.parent 
    path.reverse()
    return path


def get_solution_path(state):
    path = []
    while state:
        path.append((state.move, state.board))
        state = state.parent 
    path.reverse()
    return path


def print_solution(path):
    x=0
    for move, board in path:
        print (f'Move Number #{x}')
        x+=1
        for i in range(3):
            print(board[i*3:(i+1)*3])
        print()


def get_input(prompt):
    print(prompt)
    board = []
    for i in range(3):
        row = input().split()
        board.extend(int(num) for num in row)
    return board

initial_state = get_input ("Enter the inital state for the 8-Puzzle board")
goal_state = get_input ("Enter the goal state for the 8-Puzzle board")

solution = a_star (initial_state, goal_state)

if solution:
    solution_path = get_solution_path (solution)
    print_solution (solution_path)
    total = len(solution_path)-1
    print(f"Total number of moves from start to End is {total}")
    print()
else:
    print("No Solutuion Found.")
