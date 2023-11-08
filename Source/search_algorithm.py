from collections import deque
import math

def BFS(matrix,start,end):
    Row, Col = len(matrix), len(matrix[0])
    queue = deque() # A queue stores visitable point nearby current point
    queue.appendleft((start[0], start[1])) # Init with Start(x,y)
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[False] * Col for _ in range(Row)]
    path = deque()
    prev = [[0] * Col for _ in range(Row)]

    while len(queue) != 0:
        coord = queue.pop() # Inspect a point from queue
        visited[coord[0]][coord[1]] = True
        
        if (coord[0],coord[1]) == end:
            x, y = end
            path.appendleft(end)
            while True:
                if (prev[x][y] == 0):
                    break
                nx, ny = prev[x][y]
                x, y = nx, ny
                path.appendleft((x,y))
            visitedPoints = [(i,j) for i in range(len(visited)) 
                for j in range(len(visited[0])) 
                if visited[i][j]==True]
            return len(path)-1, path, visitedPoints
            break

        for dir in directions: # Browse all directions to find a visitable point
            nr, nc = coord[0]+dir[0], coord[1]+dir[1]
            if (nr < 0 or nr >= Row or nc < 0 or nc >= Col 
                or matrix[nr][nc] == "x" or visited[nr][nc]): 
                continue
            queue.appendleft((nr, nc)) 
            prev[nr][nc] = (coord[0], coord[1])    
            
def euclid_norm(x, y):
    dx = x[0] - y[0]
    dy = x[1] - y[1]
    return math.sqrt(dx ** 2 + dy ** 2)

def manhattan_norm(x, y):
    dx = x[0] - y[0]
    dy = x[1] - y[1]
    return abs(dx) + abs(dy)

# Find next coordinate
def move(matrix, coord, opn, close):
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    Row, Col = len(matrix), len(matrix[0])
    results = []
    for dir in directions:
        nr, nc = coord[0] + dir[0], coord[1] + dir[1]
        if (matrix[nr][nc] == 'x' or nr < 0 or nr >= Row or nc < 0 or nc >= Col):
            continue
        elif (nr, nc) not in opn and (nr, nc) not in close:
                results.append((nr, nc))
    return results

def GBFS(matrix, start, end, heuristic):
    pq = [[start, 0]] # Creat priority queue with collective heuristic
    close = [] # Init close
    Row, Col = len(matrix), len(matrix[0])
    prev = [[0] * Col for _ in range(Row)]
  
    while len(pq) != 0 and pq[0][0] != end:
        s = pq.pop(0)
        close.append(s[0])
        opn = [i[0] for i in pq] # create open
        nxt = move(matrix, s[0], opn, close) # Find next point
        for i in nxt:
            x, y = i[0], i[1]
            d = heuristic(i, end)
            if prev[x][y] == 0:
                prev[x][y] = s[0]
                pq.append([i, d])
        pq.sort(key = lambda i:i[1])

    if len(pq) == 0:
        return None
    else:
        path = deque()
        x, y = end
        path.appendleft(end)
        while True:
            if (prev[x][y] == 0):
                break
            nx, ny = prev[x][y]
            x, y = nx, ny
            path.appendleft((x,y))
        return len(path)-1, path, close

def DFS(matrix, start, end):
    path = [start] # path là list biểu diễn đường đi, bắt đầu từ start, tiếp theo là các nút có thể mở từ nút trước đó
    close = []
    #lặp khi path không rỗng và phần tử đầu tiên không phải là đích
    while (len(path) != 0 and path[-1] != end):
        top = path[-1] #phần tử đầu tiên là phần tử mới thêm vào (do DFS là hàm cài theo stack)
        s = move(matrix, top, path, close) #expand của top
        if (len(s) == 0): #nếu expand của top rỗng
            temp = path.pop() #loại bỏ top(path), đưa vào list close
            close.append(temp)
        else:
            path.append(s.pop()) #lấy 1 thành viên của expand top(path), loại bỏ nó, thêm vào cuối list đường đi (path)
    if len(path) == 0: #nếu path empty
        return None
    else:
        #trả về các trạng thái trong path
        return len(path) - 1, path, close + path

def A_STAR(matrix, start, end, heuristic):
    pq = {start: [0, euclid_norm(start, end)]} #khởi tạo priority queue
    close = [] #danh sách các điểm đã truy cập
    top, cost, path = None, None, []
    prev = {}
    for i in range (len(matrix)):
        for j in range(len(matrix[0])):
            if (matrix[i][j] == 'x'):
                pass
            else:
                prev[(i, j)] = None
    while len(pq) != 0:
        top = next(iter(pq))
        ss = pq.pop(top)
        if (top == end):
            cost = ss[0]
            break
        opn = [i for i in pq.keys()]
        close.append(top)
        s = move(matrix, top, [], close)
        for i in s:
            dist = heuristic(i, end) #xét k/c là heuristic từ điểm đang xét đến điểm kết thúc
            if prev[i] is None:
                prev[i] = top
                pq[i] = [ss[0] + 1, dist]
            elif ss[0] < pq[i][0]:
                prev[i] = top
                pq[i] = [ss[0] + 1, dist]
        pq = {k: v for k, v in sorted(pq.items(), key=lambda item: item[1][0] + item[1][1])}
    if len(pq) == 0: #nếu pq rỗng, trả về lỗi
        return None
    else:
        current_point = end
        
        while True:
            if current_point is None:
                break
            path.append(current_point)
            current_point = prev[current_point]
        
        path.reverse()
        return cost, path, close