def game_of_life(m,n,board):
    """
    You start with a two dimensional grid of cells, where each cell is either alive or dead. 
    The grid is finite, and no life can exist off the edges. When calculating the next generation of the grid, follow these four rules:

    1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
    2. Any live cell with more than three live neighbours dies, as if by overcrowding.
    3. Any live cell with two or three live neighbours lives on to the next generation.
    4. Any dead cell with exactly three live neighbours becomes a live cell.    
    """
    # Directions to check the 8 neighbors of a cell (top-left, top, top-right, left, right, bottom-left, bottom, bottom-right)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    
    # Create a copy of the board to store the next generation
    next_gen = [[0] * n for _ in range(m)]
    
    for row in range(m):
        for col in range(n):
            live_neighbors = 0
            for direction in directions:
                new_row, new_col = row + direction[0], col + direction[1]
                if 0 <= new_row < m and 0 <= new_col < n and board[new_row][new_col] == 1:
                    live_neighbors += 1
            
            if board[row][col] == 1:
                # Rule 1 and Rule 2
                if live_neighbors < 2 or live_neighbors > 3:
                    next_gen[row][col] = 0
                    
                 # Rule 3   
                else:  
                    next_gen[row][col] = 1
            else:
                # Rule 4
                if live_neighbors == 3:
                    next_gen[row][col] = 1
    
    return next_gen