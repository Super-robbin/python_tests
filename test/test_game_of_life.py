from lib.game_of_life import game_of_life

def test_game_of_life_one_cell_dies():
    input_board = [
    [1],
]
    output_board = [
    [0],
]
    assert game_of_life(1, 1, input_board) == output_board
    
def test_game_of_life_cell_with_two_neighbours_lives():
    input_board = [
    [1, 1, 1],
]
    output_board = [
    [0, 1, 0],
]
    assert game_of_life(1, 3, input_board) == output_board
    
def test_game_of_life_cell_with_three_neighbours_lives():
    input_board = [
    [1, 1],
    [1, 1],
]
    output_board = [
    [1, 1],
    [1, 1],
]
    assert game_of_life(2, 2, input_board) == output_board
    
def test_game_of_life_cell_with_four_neighbours_dies():
    input_board = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
]
    output_board = [
    [1, 0, 1],
    [0, 0, 0],
    [1, 0, 1],
]
    assert game_of_life(3, 3, input_board) == output_board
    
def test_game_of_life_dead_cell_with_three_neighbours_becomes_alive():
    input_board = [
    [0, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
]
    output_board = [
    [1, 0, 1],
    [0, 0, 0],
    [1, 0, 1],
]
    assert game_of_life(3, 3, input_board) == output_board
    
def test_game_of_life_all_four_rules():
    input_board = [
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
]
    output_board = [
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
]
    assert game_of_life(4, 4, input_board) == output_board
    