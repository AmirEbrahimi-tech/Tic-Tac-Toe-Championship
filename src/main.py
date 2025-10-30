# from grid import Grid
# from piece import Type

# def win_announce(t):
#     if t == Type.O:
#         print("The Winner is \033[1;31mRED\033[0m!")
#     elif t == Type.X:
#         print("The Winner is \033[1;34mBLUE\033[0m!")
#     else:
#         print("Oops! Something Went \033[1;31mWrong\033[0m!")

# def distrib_turn():
#     print("Choose the \033[1;33mfirst player\033[0m's Color :)")
#     print("0 : \033[1;31mO\033[0m (\033[4;31mRED\033[0m)")
#     print("1 : \033[1;34mX\033[0m (\033[4;34mBLUE\033[0m)")
#     while True:
#         try:
#             n = int(input())
#             if n in (0, 1):
#                 break
#         except ValueError:
#             pass
#         print("Chill Dude :) .. Just choose \033[1;33m0\033[0m or \033[1;33m1\033[0m")
#     print("Great!\nSo:")
#     if n == 0:
#         print("\033[1;31mRed\033[0m is the first to play and\n\033[1;34mBlue\033[0m is the second!\nHere We Go")
#     else:
#         print("\033[1;34mBlue\033[0m is the first to play and\n\033[1;31mRed\033[0m is the second!\nHere We Go")
#     return n

# def main():
#     grid = Grid()
#     turn = distrib_turn()
#     grid.display()
#     counter = 0
#     while True:
#         if turn % 2 == 0:
#             grid.input(Type.O, turn)
#         else:
#             grid.input(Type.X, turn)
#         grid.set_all_pieces()
#         grid.display()
#         winner = grid.game_finished()
#         if winner:
#             break
#         turn += 1
#         counter += 1
#     print(f"took {counter} rounds")
#     win_announce(winner)

# if __name__ == "__main__":
#     main()
import pygame
from grid import Grid
from piece import Type

# Initialize Pygame
pygame.init()
W_WIDTH, W_HEIGHT = 400, 600
G_WIDTH, G_HEIGHT = 300, 300
START_POINT = (W_WIDTH - G_WIDTH) // 2
CELL_SIZE = 80
screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
font = pygame.font.SysFont(None, 60)
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 20, 60)
BLUE = (30, 144, 255)

def draw_grid(grid):
    # loading pieces' images
    imgBlue1 = pygame.image.load("media/Blue1.png")
    imgBlue2 = pygame.image.load("media/Blue2.png")
    imgRed1 = pygame.image.load("media/Red1.png")
    imgRed2 = pygame.image.load("media/Red2.png")
    
    # Top-left origin of the grid
    gx, gy = 50, 170
    # The gap between pieces (80(CELL_SIZE)+30(distance between them))
    distance = 110

    
    for row in range(3):
        for col in range(3):
            pygame.draw .rect(screen, BLACK, (gx+row*distance, gy+col*distance,CELL_SIZE,CELL_SIZE), 2)
    
    # Draw pieces centered inside each cell (offset by grid origin)
    for row in range(3):
        for col in range(3):
            piece = grid.get_piece(row, col)
            t = piece.get_type()
            age = piece.get_age()
            if t != Type.NONE:
                img = imgRed1 if t == Type.O else imgBlue1
                if age == 1:
                    img = imgRed2 if t == Type.O else imgBlue2
                center_x = gx + (col-1) * distance
                center_y = gy + (row-1) * distance
                pygame.draw.rect(screen,WHITE,(center_x,center_y,80,80),2)
                screen.blit(img, (center_x, center_y))
                

def get_cell_from_mouse(pos):
    # Convert mouse (x,y) into grid cell indices, accounting for grid offset
    x, y = pos
    # Top-left origin of the grid
    gx, gy = 50, 170
    # Check if click is inside the grid bounds
    if x < gx or x >= gx + G_WIDTH or y < gy or y >= gy + G_HEIGHT:
        return None
    col = (x - gx) // CELL_SIZE
    row = (y - gy) // CELL_SIZE
    return int(row), int(col)

def win_announce(winner):
    if winner == Type.O:
        print("The Winner is RED!")
    elif winner == Type.X:
        print("The Winner is BLUE!")
    else:
        print("Oops! Something went wrong.")

def main():
    grid = Grid()
    turn = 0
    running = True
    winner = None
    img = pygame.image.load("media/background_pixel.png")
    background_img = pygame.transform.scale(img,(W_WIDTH,W_HEIGHT))

    while running:
        
        screen.blit(background_img, (0,0))
        draw_grid(grid)
        pygame.display.flip()
        if winner:
            pygame.time.wait(3000)
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and winner is None:
                cell = get_cell_from_mouse(event.pos)
                if cell is None:
                    # Click was outside the grid
                    continue
                row, col = cell
                if 0 <= row < 3 and 0 <= col < 3 and grid.get_piece(row, col).get_type() == Type.NONE:
                    grid.set_piece(row, col, Type.O if turn % 2 == 0 else Type.X)
                    grid.set_all_pieces()
                    winner = grid.game_finished()
                    turn += 1

        clock.tick(30)
        


    pygame.quit()

if __name__ == "__main__":
    main()
