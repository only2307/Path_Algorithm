import os
from utils import *
from search_algorithm import *

def algo_for_noBonusMap(bonus_points, matrix):
    start, end = extract_point(matrix)
    while True:
        print('Selecting a option below:')
        print('1. DFS')
        print('2. BFS')
        print('3. GBFS')
        print('4. A*')
        print('0. Return')
        choice = int(input('You choose: '))
        cost, route, visited = None, None, None
        if choice == 1:
            cost, route, visited = DFS(matrix, start, end)
        elif choice == 2:
            cost, route, visited = BFS(matrix, start, end)
        elif choice == 3:
            print('Choose Heuristic')
            print('1. Manhattan Norm')
            print('2. Euclid Norm')
            t = int(input('You choose: '))
            if t == 1:
                cost, route, visited = GBFS(matrix, start, end, manhattan_norm)
            elif t == 2:
                cost, route, visited = GBFS(matrix, start, end, euclid_norm)
        elif choice == 4:
            print('Choose Heuristic')
            print('1. Manhattan Norm')
            print('2. Euclid Norm')
            t = int(input('You choose: '))
            if t == 1:
                cost, route, visited = A_STAR(matrix, start, end, manhattan_norm)
            elif t == 2:
                cost, route, visited = A_STAR(matrix, start, end, euclid_norm)
        else:
            break
        visualize_maze(matrix, bonus_points, start, end, route, visited)
        input()
        os.system('cls')

def map_no_bonus():
    while True:
        print('Selecting a option below:')
        print('1. Map 01')
        print('2. Map 02')
        print('3. Map 03')
        print('4. Map 04')
        print('5. Map 05')
        print('0. Return')
        choice = int(input('You choose: '))
        if choice == 1:
            bonus_points, matrix = read_file('../maze_map/maze_map_1.txt')
        elif choice == 2:
            bonus_points, matrix = read_file('../maze_map/maze_map_2.txt')
        elif choice == 3:
            bonus_points, matrix = read_file('../maze_map/maze_map_3.txt')
        elif choice == 4:
            bonus_points, matrix = read_file('../maze_map/maze_map_4.txt')
        elif choice == 5:
            bonus_points, matrix = read_file('../maze_map/maze_map_5.txt')
        else:
            break
        os.system('cls')
        algo_for_noBonusMap(bonus_points, matrix)
        os.system('cls')

if __name__ == '__main__':
    while True:
        print('Selecting a option below:')
        print('1. Map no bonus')
        print('2. Map bonus')
        print('0. Quit')
        choice = int(input('You choose: '))
        if choice == 1:
            os.system('cls')
            map_no_bonus()
            os.system('cls')
        elif choice == 2:
            os.system('cls')
            print("Not Implemented! Error!")
            os.system('cls')
        else:
            break
        os.system('cls')