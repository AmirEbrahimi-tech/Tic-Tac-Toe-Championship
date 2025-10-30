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
    imgBlue1 = pygame.image.load("src/media/Blue1.png")
    imgBlue2 = pygame.image.load("src/media/Blue2.png")
    imgRed1 = pygame.image.load("src/media/Red1.png")
    imgRed2 = pygame.image.load("src/media/Red2.png")
    
    # Top-left origin of the grid
    gx, gy = 50, 170
    # The gap between pieces (80(CELL_SIZE)+30(distance between them))
    distance = 110
    
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
                center_x = (col-1) * distance
                center_y = (row-1) * distance
                screen.blit(img, (center_x, center_y))
                

def get_cell_from_mouse(pos):
    # Convert mouse (x,y) into grid cell indices, accounting for grid offset
    x, y = pos
    # Top-left origin of the grid
    gx, gy = 50, 170
    # The gap between pieces (80(CELL_SIZE)+30(distance between them))
    distance = 110
    # Check if click is inside the grid bounds
    allowed_areas = []
    for row in range(3):
        for col in range(3):
            allowed_areas.append(pygame.draw .rect(screen, (0,0,0,0), (gx+row*distance, gy+col*distance,CELL_SIZE,CELL_SIZE), 2))
    for i in allowed_areas:
        if i.collidepoint((x,y)):
            col = (x - gx) // distance
            row = (y - gy) // distance
            return int(row), int(col)
    return None

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
    img = pygame.image.load("src/media/background_pixel.png")
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
