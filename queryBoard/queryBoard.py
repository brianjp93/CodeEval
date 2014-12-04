import sys

board = []
for i in range(256):
    board.append(256 * [0])

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip().split()
        if line[0] == "QueryCol" or line[0] == "QueryRow":
            command, loc = line[0], int(line[1])
            if command == "QueryCol":
                total = 0
                for row in board:
                    total += row[loc]
                print(total)
            elif command == "QueryRow":
                total = sum(board[loc])
                print(total)
        else:
            command, loc, x = line[0], int(line[1]), int(line[2])
            if command == "SetCol":
                for row in board:
                    row[loc] = x
            elif command == "SetRow":
                for i in range(len(board[loc])):
                    board[loc][i] = x
