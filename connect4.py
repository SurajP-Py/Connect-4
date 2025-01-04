import pygame

pygame.init()

size = (800, 700)
window_surface = pygame.display.set_mode(size)
pygame.display.set_caption("Connect 4")

font = pygame.font.SysFont('arial', 52, True)

labels = font.render("1       2       3       4       5       6       7", False, "black")
labelsRect = labels.get_rect()
labelsRect.center = (400, 75)

yWin = font.render("Yellow Wins! Press '0' to play again.", False, "black", (255, 255, 0, 100))
rWin = font.render("Red Wins! Press '0' to play again.", False, "black", (255, 50, 50, 100))
yWinRect = yWin.get_rect()
yWinRect.center = (400, 350)
rWinRect = rWin.get_rect()
rWinRect.center = (400, 350)

clock = pygame.time.Clock()
running = True
windowed = True
gameActive = True

turn = 0
grid = [[-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1]]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #X button = endgame
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                #escape = endgame
                running = False
                
            if event.key == pygame.K_1:

                if grid[0][0] == -1:
                    for i in range(5, -1, -1): 
                        if grid[i][0] == -1 and gameActive:
                            grid[i][0] = turn
                            turn = (turn + 1) % 2
                            print(turn)
                            for i in range(6):
                                print(grid[i])
                            break
                    
            if event.key == pygame.K_2:
                
                if grid[0][1] == -1:
                    for i in range(5, -1, -1): 
                        if grid[i][1] == -1 and gameActive:
                            grid[i][1] = turn
                            turn = (turn + 1) % 2
                            print(turn)
                            for i in range(6):
                                print(grid[i])
                            break
                    
            if event.key == pygame.K_3:
                
                if grid[0][2] == -1:
                    for i in range(5, -1, -1): 
                        if grid[i][2] == -1 and gameActive:
                            grid[i][2] = turn
                            turn = (turn + 1) % 2
                            print(turn)
                            for i in range(6):
                                print(grid[i])
                            break
                    
            if event.key == pygame.K_4:
                
                if grid[0][3] == -1:
                    for i in range(5, -1, -1): 
                        if grid[i][3] == -1 and gameActive:
                            grid[i][3] = turn
                            turn = (turn + 1) % 2
                            print(turn)
                            for i in range(6):
                                print(grid[i])
                            break
                    
            if event.key == pygame.K_5:
                
                if grid[0][4] == -1:
                    for i in range(5, -1, -1): 
                        if grid[i][4] == -1 and gameActive:
                            grid[i][4] = turn
                            turn = (turn + 1) % 2
                            print(turn)
                            for i in range(6):
                                print(grid[i])
                            break
                                
            if event.key == pygame.K_6:
                
                if grid[0][5] == -1:
                    for i in range(5, -1, -1): 
                        if grid[i][5] == -1 and gameActive:
                            grid[i][5] = turn
                            turn = (turn + 1) % 2
                            print(turn)
                            for i in range(6):
                                print(grid[i])
                            break
                                
            if event.key == pygame.K_7:
                
                if grid[0][6] == -1:
                    for i in range(5, -1, -1): 
                        if grid[i][6] == -1 and gameActive:
                            grid[i][6] = turn
                            turn = (turn + 1) % 2
                            print(turn)
                            for i in range(6):
                                print(grid[i])
                            break

            if event.key == pygame.K_0:
                grid = [[-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1]]
                turn = 0
                gameActive = True

    # RENDER YOUR GAME HERE
    
    window_surface.fill("blue")

    
    #empty slots
    for i in range(7):
        for j in range(6):
            pygame.draw.circle(window_surface, (255, 255, 255), (i * 108 + 75, j * 110 + 75), 50)

    #slot labels
    window_surface.blit(labels, labelsRect)

    #filled slots
    for i in range(7):
        for j in range(6):
            if grid[j][i] == 1:
                pygame.draw.circle(window_surface, (255, 255, 0), (i * 108 + 75, j * 110 + 75), 50)
            if grid[j][i] == 0:
                pygame.draw.circle(window_surface, (255, 0, 0), (i * 108 + 75, j * 110 + 75), 50)
    
    #win detection:
    #downward diagonal
    for i in range(4):
        for j in range(3):
            if grid[j][i] == 0 and grid[j+1][i+1] == 0 and grid[j+2][i+2] == 0 and grid[j+3][i+3] == 0:
                window_surface.blit(rWin, rWinRect)
                pygame.draw.circle(window_surface, (0, 0, 0), (i * 108 + 75, j * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i+1) * 108 + 75, (j+1) * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i+2) * 108 + 75, (j+2) * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i+3) * 108 + 75, (j+3) * 110 + 75), 25, 10)
                gameActive = False
            if grid[j][i] == 1 and grid[j+1][i+1] == 1 and grid[j+2][i+2] == 1 and grid[j+3][i+3] == 1:
                window_surface.blit(yWin, yWinRect)
                pygame.draw.circle(window_surface, (0, 0, 0), (i * 108 + 75, j * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i+1) * 108 + 75, (j+1) * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i+2) * 108 + 75, (j+2) * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i+3) * 108 + 75, (j+3) * 110 + 75), 25, 10)
                gameActive = False

    #upward diagonal
    for i in range(3,7):
        for j in range(3):
            if grid[j][i] == 0 and grid[j+1][i-1] == 0 and grid[j+2][i-2] == 0 and grid[j+3][i-3] == 0:
                window_surface.blit(rWin, rWinRect)
                pygame.draw.circle(window_surface, (0, 0, 0), (i * 108 + 75, j * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i-1) * 108 + 75, (j+1) * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i-2) * 108 + 75, (j+2) * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i-3) * 108 + 75, (j+3) * 110 + 75), 25, 10)
                gameActive = False
            if grid[j][i] == 1 and grid[j+1][i-1] == 1 and grid[j+2][i-2] == 1 and grid[j+3][i-3] == 1:
                window_surface.blit(yWin, yWinRect)
                pygame.draw.circle(window_surface, (0, 0, 0), (i * 108 + 75, j * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i-1) * 108 + 75, (j+1) * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i-2) * 108 + 75, (j+2) * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i-3) * 108 + 75, (j+3) * 110 + 75), 25, 10)
                gameActive = False
                
    
    #vertical
    for i in range(7):
        for j in range(3):
            if grid[j][i] == 0 and grid[j+1][i] == 0 and grid[j+2][i] == 0 and grid[j+3][i] == 0:
                window_surface.blit(rWin, rWinRect)
                pygame.draw.circle(window_surface, (0, 0, 0), (i * 108 + 75, j * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i) * 108 + 75, (j+1) * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i) * 108 + 75, (j+2) * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i) * 108 + 75, (j+3) * 110 + 75), 25, 10)
                gameActive = False
            if grid[j][i] == 1 and grid[j+1][i] == 1 and grid[j+2][i] == 1 and grid[j+3][i] == 1:
                window_surface.blit(yWin, yWinRect)
                pygame.draw.circle(window_surface, (0, 0, 0), (i * 108 + 75, j * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i) * 108 + 75, (j+1) * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i) * 108 + 75, (j+2) * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i) * 108 + 75, (j+3) * 110 + 75), 25, 10)
                gameActive = False

    #horizontal
    for i in range(4):
        for j in range(6):
            if grid[j][i] == 0 and grid[j][i+1] == 0 and grid[j][i+2] == 0 and grid[j][i+3] == 0:
                window_surface.blit(rWin, rWinRect)
                pygame.draw.circle(window_surface, (0, 0, 0), (i * 108 + 75, j * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i+1) * 108 + 75, (j) * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i+2) * 108 + 75, (j) * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i+3) * 108 + 75, (j) * 110 + 75), 25, 10)
                gameActive = False
            if grid[j][i] == 1 and grid[j][i+1] == 1 and grid[j][i+2] == 1 and grid[j][i+3] == 1:
                window_surface.blit(yWin, yWinRect)
                pygame.draw.circle(window_surface, (0, 0, 0), (i * 108 + 75, j * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i+1) * 108 + 75, (j) * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i+2) * 108 + 75, (j) * 110 + 75), 25, 10)
                pygame.draw.circle(window_surface, (0, 0, 0), ((i+3) * 108 + 75, (j) * 110 + 75), 25, 10)
                gameActive = False
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
